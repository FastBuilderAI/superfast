---
name: bun-execution
description: Use when running scripts, testing, or building codebases that utilize the Bun JavaScript runtime explicitly, evidenced by bun.lockb or bun execution scripts.
---

# Bun Execution Engine

## Overview

Bun is a high-performance JavaScript runtime, bundler, and test runner. When operating in a high-value enterprise codebase that has chosen Bun over Node.js, standard Node execution commands (`npm run`, `npx`, `node`) will often fail or discard the performance benefits of the Bun engine. This skill defines the deterministic execution patterns required to interact natively with Bun environments.

## When to Use

- Explicitly see `bun.lockb` or `bunfig.toml` in the repository
- `package.json` scripts are explicitly prefixed with `bun`
- Standard `npm install` or `npm run dev` fails due to module resolution or package manager conflicts
- You need to execute TypeScript (`.ts` / `.tsx`) files directly without a standard TSC compilation step

## Core Pattern

When interacting with a Bun repository, the standard Node vocabulary must be aggressively swapped:

| Standard Node.js | Bun Execution |
| ---------------- | ------------- |
| `npm install` | `bun install` |
| `npm run test` | `bun test` |
| `npx tsc` | `bunx tsc` |
| `node script.js` | `bun run script.js` or `bun script.ts` |
| `npm install <pkg>` | `bun add <pkg>` |

## Execution Methodology

1. **Direct TypeScript Execution**
   Bun natively executes `.ts` and `.tsx` files. You do **not** need to invoke `tsc` or `ts-node` to run a script. This massively accelerates the Subagent-Driven Development loop.
   ```bash
   bun run src/index.ts
   ```

2. **Ultra-Fast Testing**
   Bun includes a native test runner heavily compatible with Jest expect patterns. When running Test-Driven Development cycles, always use the Bun test runner instead of booting a Jest process:
   ```bash
   bun test
   
   # Run a specific file
   bun test src/utils.test.ts
   ```

3. **Package Management**
   Bun's package manager is vastly faster than npm/yarn. **Never** use `npm install` inside a Bun repository, as it breaks the resolution lockfile.
   ```bash
   bun add lodash
   bun add -d typescript @types/node
   ```

## Common Mistakes

- **Running `npm install` blindly**: This generates a rogue `package-lock.json` and pollutes the dependency tree, destroying the native `bun.lockb` resolution hierarchy. **Fix**: Delete the `package-lock.json` immediately and run `bun install`.
- **Using `ts-node`**: Executing `npx ts-node script.ts` inside a Bun repository is a critical anti-pattern. Use `bun run script.ts`.
- **Assuming Node APIs are perfectly matched**: While Bun aims for Node compatibility, native Node modules (like `fs`, `path`) have highly optimized Bun counterparts (`Bun.file()`, `Bun.write()`). Only refactor to `Bun.*` APIs if specifically tasked to optimize; otherwise, standard Node modules will usually work.

## Red Flags - STOP and Start Over

If you catch yourself doing any of the following in a Bun repository, stop and immediately pivot to the Bun equivalent:
- Typing `npm install` or `yarn install`
- Setting up `ts-node` or `ts-jest` compilation loops
- Generating a `package-lock.json` file inside a directory containing `bun.lockb`

**Violating the letter of these rules is violating the spirit of high-performance environment execution.**
