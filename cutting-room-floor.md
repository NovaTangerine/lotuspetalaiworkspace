# Cutting Room Floor

This file stores ideas, animations, and concepts that were tested but ultimately not used in production.

## Intelligence Layer Animations

### 1. Active Source Node: Rhythmic Surge Fill
Instead of a static gradient, the active source node pulses a bright magenta gradient in perfect synchronization (1.2s) with the pipeline shimmer.

```css
.intel-node-source.active {
  background: var(--stream-core);
  border-color: transparent;
  box-shadow: 0px 4px 12px var(--stream-glow);
  animation: float 6s ease-in-out infinite 1s, rhythmicSurgeColor 1.2s infinite ease-in-out;
}

.intel-node-source.active::before {
  animation: rhythmicSurgeFill 1.2s infinite ease-in-out;
}

@keyframes rhythmicSurgeColor {
  0% { color: white; }
  30% { color: var(--stream-primary); }
  70% { color: var(--stream-primary); }
  100% { color: white; }
}

@keyframes rhythmicSurgeFill {
  0% { opacity: 1; }
  30% { opacity: 0; }
  70% { opacity: 0; }
  100% { opacity: 1; }
}
```

### 2. Active Source Node: Directional Empty (Top-to-Bottom Drain)
The active node acts like a reservoir. When it becomes active, it starts 100% full of the rich gradient, and slowly empties downwards towards the pipeline over exactly 4 seconds (matching the pipeline switch timer).

```css
/* Base inactive nodes get a soft wash so they do not look empty */
.intel-node-source {
  background: var(--stream-bg);
  /* ... existing styles ... */
}

/* Active node base state is the empty state (the soft wash) */
.intel-node-source.active {
  background: var(--stream-bg);
  border-color: transparent;
  color: var(--stream-primary);
  box-shadow: 0px 4px 12px var(--stream-glow);
  animation: float 6s ease-in-out infinite 1s;
}

/* The gradient fill layer that drains out over 4s */
.intel-node-source.active::before {
  opacity: 1;
  background: linear-gradient(135deg, var(--stream-bright), var(--stream-primary));
  animation: directionalEmpty 4s linear forwards;
}

@keyframes directionalEmpty {
  0% { clip-path: inset(0 0 0 0); } /* Full */
  100% { clip-path: inset(100% 0 0 0); } /* Empty (drained down) */
}
```
