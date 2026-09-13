import re

with open("assets/intelligence.css", "r") as f:
    css = f.read()

var_block = """  /* Pipeline Energy Theme Variables */
  --stream-primary: #D10D88;
  --stream-light: #FFA0DC;
  --stream-bright: #FF66C4;
  --stream-glow: rgba(209, 13, 136, 0.4);
  --stream-glow-strong: rgba(209, 13, 136, 0.6);
  --stream-glow-zero: rgba(209, 13, 136, 0);
}

.intelligence-graphic.theme-blue {
  --stream-primary: #04c8c8;
  --stream-light: #90fff6;
  --stream-bright: #50f8f0;
  --stream-glow: rgba(4, 200, 200, 0.4);
  --stream-glow-strong: rgba(4, 200, 200, 0.6);
  --stream-glow-zero: rgba(4, 200, 200, 0);
}
"""

css = css.replace("background-color: transparent;\n}", "background-color: transparent;\n" + var_block)

css = css.replace("linear-gradient(135deg, #FF66C4, #D10D88)", "linear-gradient(135deg, var(--stream-bright), var(--stream-primary))")
css = css.replace("box-shadow: 0px 4px 12px rgba(209, 13, 136, 0.4)", "box-shadow: 0px 4px 12px var(--stream-glow)")
css = css.replace("background-color: #D10D88", "background-color: var(--stream-primary)")
css = css.replace("linear-gradient(135deg, #D10D88 0%, #FFA0DC 50%, #D10D88 100%)", "linear-gradient(135deg, var(--stream-primary) 0%, var(--stream-light) 50%, var(--stream-primary) 100%)")
css = css.replace("border-color: #D10D88", "border-color: var(--stream-primary)")
css = css.replace("color: #D10D88", "color: var(--stream-primary)")

# pulse keyframes
css = css.replace("box-shadow: 0 0 0 0 rgba(209, 13, 136, 0.6)", "box-shadow: 0 0 0 0 var(--stream-glow-strong)")
css = css.replace("box-shadow: 0 0 0 15px rgba(209, 13, 136, 0)", "box-shadow: 0 0 0 15px var(--stream-glow-zero)")
css = css.replace("box-shadow: 0 0 0 0 rgba(209, 13, 136, 0)", "box-shadow: 0 0 0 0 var(--stream-glow-zero)")

with open("assets/intelligence.css", "w") as f:
    f.write(css)

with open("intelligence-layer.html", "r") as f:
    html = f.read()

# Update SVG gradients
html = html.replace('stop-color="#D10D88"', 'stop-color="var(--stream-primary)"')
html = html.replace('stop-color="#FFA0DC"', 'stop-color="var(--stream-light)"')

# Update spigot stroke
html = html.replace('stroke="#D10D88"', 'stroke="var(--stream-primary)"')
html = html.replace("spigots[currentIndex].setAttribute('stroke', '#D10D88');", "spigots[currentIndex].setAttribute('stroke', 'var(--stream-primary)');")

# Add the toggle button
toggle_btn = """      <button class="test-btn" id="test-switch-btn">Test Pipeline Switch</button>
      <button class="test-btn" id="test-theme-btn" style="margin-left: 10px; background: #04c8c8; color: #fff; border-color: #04c8c8;">Toggle Blue Pipeline</button>"""
html = html.replace('<button class="test-btn" id="test-switch-btn">Test Pipeline Switch</button>', toggle_btn)

js_toggle = """
    // Theme Toggle Logic
    const themeBtn = document.getElementById('test-theme-btn');
    const container = document.querySelector('.intelligence-graphic');
    themeBtn.addEventListener('click', () => {
      container.classList.toggle('theme-blue');
      if (container.classList.contains('theme-blue')) {
        themeBtn.style.background = '#D10D88';
        themeBtn.style.borderColor = '#D10D88';
        themeBtn.innerText = 'Toggle Pink Pipeline';
      } else {
        themeBtn.style.background = '#04c8c8';
        themeBtn.style.borderColor = '#04c8c8';
        themeBtn.innerText = 'Toggle Blue Pipeline';
      }
    });
"""
html = html.replace('// Pipeline Switching Logic', js_toggle + '\n    // Pipeline Switching Logic')

with open("intelligence-layer.html", "w") as f:
    f.write(html)

