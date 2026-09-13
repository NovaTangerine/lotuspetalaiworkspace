with open("assets/intelligence.css", "r") as f:
    content = f.read()

# Add the missing variables block to the top of the file
var_block = """
.intelligence-graphic {
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

.intelligence-graphic.theme-blue {
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

if "--theme-grid" not in content:
    content = var_block + content

with open("assets/intelligence.css", "w") as f:
    f.write(content)

with open("intelligence-layer.html", "r") as f:
    html = f.read()

html = html.replace("const container = document.querySelector('.intel-container');", "const container = document.querySelector('.intelligence-graphic');")

with open("intelligence-layer.html", "w") as f:
    f.write(html)
