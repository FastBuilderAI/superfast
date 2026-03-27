---
name: fastmemory
description: Use when needing to maintain long-term cognitive memory of project architecture, components, and logic using the CBFDAE ontology
---

# FastMemory

## Overview

**FastMemory is the horizontal layer of truth for AI agents.**

It provides a structured way to store and retrieve project knowledge using the **CBFDAE** (Component, Block, Function, Data, Access, Event) ontology. This reduces hallucinations by ensuring the agent always references a verified, structured cognitive graph of the codebase instead of relying on transient context.

## When to Use

Use FastMemory whenever you are:
- Designing a new system or feature.
- Documenting existing complex logic.
- Needing to cross-reference architectural decisions from previous sessions.
- Struggling with context limits (FastMemory provides compressed, semantic retrieval).

**Symptoms that you need FastMemory:**
- You keep forgetting how a specific module interacts with another.
- You find yourself "guessing" the names of data structures or events.
- The project is growing too large for the current context window.

## CBFDAE Ontology

| Entity | Description | Example |
|--------|-------------|---------|
| **Component** | High-level logical unit | `AuthService`, `PaymentGateway` |
| **Block** | Functional grouping within a component | `LoginFlow`, `TokenExchanger` |
| **Function** | Specific atomic operation | `validateCredentials`, `issueJWT` |
| **Data** | Data structures or schemas | `UserData`, `AuthResult` |
| **Access** | Permissions and visibility | `Public`, `AdminOnly` |
| **Event** | State changes or notifications | `UserLoggedIn`, `AccessDenied` |

## Implementation

### 1. Extraction

Use the `extract_cbfdae.py` tool to extract structured data from your design markdown.

```bash
python3 skills/fastmemory/extract_cbfdae.py design.md
```

### 2. Integration

When starting a task, query FastMemory for relevant context:

```bash
# Query for Auth component patterns
python3 skills/fastmemory/query_memory.py --query "Component: Auth"
```

## Common Mistakes

- **Too much detail**: Don't map every line of code. Map at the architectural level.
- **Stale memory**: Forget to update the graph after a significant refactor.
- **Flat structure**: Forgetting to link Blocks to their parent Components.

## Real-World Impact

- **30x Speedup**: Delta updates to the cognitive graph are significantly faster than full RAG re-indexing.
- **Zero Hallucination**: Architecture is strictly enforced by the CBFDAE schema.
