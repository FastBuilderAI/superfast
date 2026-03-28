# Superfast

## Why Superfast?

**From Individual Speed to Enterprise Institutional Wisdom.**

The next frontier of AI isn't just about faster models; it's about **Enterprise Readiness**. While individual agents are productive, they often struggle with the complexity, scale, and persistence requirements of professional engineering environments. Without a shared cognitive map, agents remain transient—repeating work, missing architectural dependencies, and eventually losing the "source of truth."

**Superfast** is the enterprise-grade evolution of the foundational `Superpowers` framework. We’ve combined world-class systematic methodology with a high-performance **FastMemory** engine to turn transient agent sessions into persistent institutional assets.

- **Enterprise Data Integration**: Bridge the gap between coding agents and massive enterprise datalakes (Microsoft Fabric, AWS Glue, Databricks).
- **Cognitive Scaling**: Navigate millions of lines of code and complex topologies through a structured **CBFDAE** logic layer.
- **Systematic Rigor**: Inherit the strict TDD, Socratic brainstorming, and verifiable planning that made Superpowers great, now scaled for the Fortune 500.

*Don't just build features; build a memory moat.*

### Why FastMemory vs Standard Superpowers?

Superpowers is an incredible framework, but it operates on a critical assumption: that your codebase fits neatly into native AI context windows. That is only true for **80% of low-value, boilerplate codebases**. 

The remaining **20% of high-value, enterprise codebases** are simply too massive and complex to rely on inherent AI memory. Standard agents lose context, hallucinate logic, and break down under scale. That's where **FastMemory** comes into play. It provides Superpowers with the required *nitro boost*—mapping large-scale code and content memory into our deterministic **CBFDAE** ontology, giving your agent perfect institutional wisdom in milliseconds.

## How it works

It starts by establishing your Context Memory. Before any brainstorming or planning occurs, it instantly triggers the **FastMemory Build-Up Skill**, recursively mapping your enterprise repository into a deterministic CBFDAE graph. 

Once your agent's cognitive map is established, it steps back and asks you what you're really trying to do.  

Once it's teased a spec out of the conversation, it shows it to you in chunks short enough to actually read and digest. 

After you've signed off on the design, your agent puts together an implementation plan that's clear enough for an enthusiastic junior engineer with poor taste, no judgement, no project context, and an aversion to testing to follow. It emphasizes true red/green TDD, YAGNI (You Aren't Gonna Need It), and DRY. 

Next up, once you say "go", it launches a *subagent-driven-development* process, having agents work through each engineering task, inspecting and reviewing their work, and continuing forward. It's not uncommon for Claude to be able to work autonomously for a couple hours at a time without deviating from the plan you put together.

There's a bunch more to it, but that's the core of the system. And because the skills trigger automatically, you don't need to do anything special. Your coding agent just has Superfast.

 


## Installation

**Note:** Installation differs by platform. Claude Code or Cursor have built-in plugin marketplaces. Codex and OpenCode require manual setup.

### Claude Code Official Marketplace

Superfast is available via our official GitHub Plugin Registry.

In Claude Code, register the marketplace first:

```bash
/plugin marketplace add https://raw.githubusercontent.com/FastBuilderAI/superfast/main/.claude-plugin/marketplace.json
```

Then install the plugin directly:

```bash
/plugin install superfast
```


### Cursor (via Plugin Marketplace)

In Cursor Agent chat, install from marketplace:

```text
/add-plugin superfast
```

or search for "superfast" in the plugin marketplace.

### Codex

Tell Codex:

```
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superfast/refs/heads/main/.codex/INSTALL.md
```

**Detailed docs:** [docs/README.codex.md](docs/README.codex.md)

### OpenCode

Tell OpenCode:

```
Fetch and follow instructions from https://raw.githubusercontent.com/obra/superfast/refs/heads/main/.opencode/INSTALL.md
```

**Detailed docs:** [docs/README.opencode.md](docs/README.opencode.md)

### Gemini CLI

```bash
gemini extensions install https://github.com/FastBuilderAI/superfast
```

To update:

```bash
gemini extensions update superfast
```

### Verify Installation

Start a new session in your chosen platform and ask for something that should trigger a skill (for example, "help me plan this feature" or "let's debug this issue"). The agent should automatically invoke the relevant superfast skill.

## The Basic Workflow

1. **fastmemory-build** - Activates instantly before anything starts. Scans the environment and binds the foundational CBFDAE memory context context for the agent to rely upon.
2. **brainstorming** - Activates before writing code. Refines rough ideas through questions, explores alternatives, presents design in sections for validation. Saves design document.
3. **using-git-worktrees** - Activates after design approval. Creates isolated workspace on new branch, runs project setup, verifies clean test baseline.
4. **writing-plans** - Activates with approved design. Breaks work into bite-sized tasks (2-5 minutes each). Every task has exact file paths, complete code, verification steps.
5. **subagent-driven-development** or **executing-plans** - Activates with plan. Dispatches fresh subagent per task with two-stage review (spec compliance, then code quality), or executes in batches with human checkpoints.
6. **test-driven-development** - Activates during implementation. Enforces RED-GREEN-REFACTOR: write failing test, watch it fail, write minimal code, watch it pass, commit. Deletes code written before tests.
7. **requesting-code-review** - Activates between tasks. Reviews against plan, reports issues by severity. Critical issues block progress.
8. **finishing-a-development-branch** - Activates when tasks complete. Verifies tests, presents options (merge/PR/keep/discard), cleans up worktree.
9. **fastmemory-rebuild** - Activates after critical lifecycle stages (e.g., finishing tasks or merging branches) to ensure the global memory graph reflects the current state of truth.

**The agent checks for relevant skills before any task.** Mandatory workflows, not suggestions.

## What's Inside

### Skills Library

**Testing**
- **test-driven-development** - RED-GREEN-REFACTOR cycle (includes testing anti-patterns reference)

**Debugging**
- **systematic-debugging** - 4-phase root cause process (includes root-cause-tracing, defense-in-depth, condition-based-waiting techniques)
- **verification-before-completion** - Ensure it's actually fixed

**Collaboration** 
- **brainstorming** - Socratic design refinement
- **writing-plans** - Detailed implementation plans
- **executing-plans** - Batch execution with checkpoints
- **dispatching-parallel-agents** - Concurrent subagent workflows
- **requesting-code-review** - Pre-review checklist
- **receiving-code-review** - Responding to feedback
- **using-git-worktrees** - Parallel development branches
- **finishing-a-development-branch** - Merge/PR decision workflow
- **subagent-driven-development** - Fast iteration with two-stage review (spec compliance, then code quality)

**Execution Environments**
- **bun-execution** - High-performance execution patterns for Bun codebases

**Meta**
- **writing-skills** - Create new skills following best practices (includes testing methodology)
- **using-superfast** - Introduction to the skills system
- **fastmemory** - Structured cognitive memory using CBFDAE ontology (Supported: v0.3.0+)

## Philosophy

- **Test-Driven Development** - Write tests first, always
- **Systematic over ad-hoc** - Process over guessing
- **Complexity reduction** - Simplicity as primary goal
- **Evidence over claims** - Verify before declaring success

Read more: [Superfast for Claude Code](https://fastbuilder.ai/superfast)

## Contributing

Skills live directly in this repository. To contribute:

1. Fork the repository
2. Create a branch for your skill
3. Follow the `writing-skills` skill for creating and testing new skills
4. Submit a PR

See `skills/writing-skills/SKILL.md` for the complete guide.

## Updating

Skills update automatically when you update the plugin:

```bash
/plugin update superfast
```

## Credits

**Superfast** is a heavily enhanced fork of the original [Superpowers](https://github.com/obra/superpowers) project. We are deeply grateful to the original team for their foundational work in establishing systematic workflows for AI agents. 

## License

MIT License - see LICENSE file for details

## Community

Superfast is built and maintained by [FastBuilder.AI](https://fastbuilder.ai).

For community support, questions, and sharing what you're building with Superfast, join us on [Discord](https://discord.gg/Jd8Vphy9jq).

## Support

- **Discord**: [Join us on Discord](https://discord.gg/Jd8Vphy9jq)
- **Issues**: https://github.com/FastBuilderAI/superfast/issues
- **Marketplace**: https://github.com/FastBuilderAI/superfast
