---
trigger: always_on
description: Ensures the agent never goes out of scope on simple tasks
---

# Strict Scope Adherence

When handling user requests, especially simple or narrowly scoped tasks:
1. **Never go out of scope or add unrequested changes.** Do exactly what is asked and nothing more.
2. **Strictly adhere to stated instructions.** Do not make assumptions or take creative liberties with the user's design, architecture, or codebase unless explicitly asked to do so.
3. **Do not overcomplicate.** If a simple adjustment is requested, make that simple adjustment. Do not attempt unprompted workarounds (e.g., CSS hacks when native solutions are requested).
4. **Ask instead of guessing.** If the exact parameters needed to fulfill a request are unclear or unknown, stop and ask the user for clarification rather than guessing and breaking existing implementations.
