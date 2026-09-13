import re

with open("assets/intelligence.css", "r") as f:
    content = f.read()

# Add variables to .intel-container
var_block = """
  /* Theme Variables */
  --theme-grid: rgba(209, 13, 136, 0.4);
  --theme-inactive: #D9C6CE;
  --theme-primary: #D10D88;
  --theme-primary-light: #FFA0DC;
  --theme-primary-bright: #FF66C4;
  --theme-dark-bg: #5A063C;
  --theme-glow-str: rgba(209, 13, 136, 0.6);
  --theme-glow-soft: rgba(209, 13, 136, 0.3);
  --theme-glow-faint: rgba(209, 13, 136, 0.4);
}

.intel-container.theme-blue {
  --theme-grid: rgba(4, 200, 200, 0.4);
  --theme-inactive: #c7fffa;
  --theme-primary: #04c8c8;
  --theme-primary-light: #90fff6;
  --theme-primary-bright: #50f8f0;
  --theme-dark-bg: #0d4f52;
  --theme-glow-str: rgba(4, 200, 200, 0.6);
  --theme-glow-soft: rgba(4, 200, 200, 0.3);
  --theme-glow-faint: rgba(4, 200, 200, 0.4);
}
"""
content = re.sub(r'margin: 40px auto;\n\}', r'margin: 40px auto;\n' + var_block, content)

# Replacements
content = content.replace("rgba(209, 13, 136, 0.4)", "var(--theme-grid)")
content = content.replace("#D9C6CE", "var(--theme-inactive)")
content = content.replace("#FF66C4", "var(--theme-primary-bright)")
content = content.replace("#D10D88", "var(--theme-primary)")
content = content.replace("#5A063C", "var(--theme-dark-bg)")
content = content.replace("rgba(209, 13, 136, 0.3)", "var(--theme-glow-soft)")
content = content.replace("rgba(209, 13, 136, 0.6)", "var(--theme-glow-str)")
content = content.replace("#FFA0DC", "var(--theme-primary-light)")

# We replaced the grid color, but glow-faint is also the same string.
# Actually, the var(--theme-grid) works perfectly for the box-shadow since they share the same rgba string.

with open("assets/intelligence.css", "w") as f:
    f.write(content)
