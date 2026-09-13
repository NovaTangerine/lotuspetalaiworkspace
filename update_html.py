with open("intelligence-layer.html", "r") as f:
    content = f.read()

# Replace SVG colors with variables
content = content.replace('stop-color="#D10D88"', 'stop-color="var(--theme-primary)"')
content = content.replace('stop-color="#FFA0DC"', 'stop-color="var(--theme-primary-light)"')
content = content.replace('stroke="#D9C6CE"', 'stroke="var(--theme-inactive)"')
content = content.replace('stroke="#D10D88"', 'stroke="var(--theme-primary)"')

# Update JS strings
content = content.replace("spigots[currentIndex].setAttribute('stroke', '#D9C6CE');", "spigots[currentIndex].setAttribute('stroke', 'var(--theme-inactive)');")
content = content.replace("spigots[currentIndex].setAttribute('stroke', '#D10D88');", "spigots[currentIndex].setAttribute('stroke', 'var(--theme-primary)');")

# Add the toggle button
toggle_btn = """      <button class="test-btn" id="test-switch-btn">Test Pipeline Switch</button>
      <button class="test-btn" id="test-theme-btn" style="margin-left: 10px; background: #04c8c8; color: #fff;">Toggle Blue Theme</button>"""
content = content.replace('<button class="test-btn" id="test-switch-btn">Test Pipeline Switch</button>', toggle_btn)

# Add the JS for the toggle button
js_toggle = """
    // Theme Toggle Logic
    const themeBtn = document.getElementById('test-theme-btn');
    const container = document.querySelector('.intel-container');
    themeBtn.addEventListener('click', () => {
      container.classList.toggle('theme-blue');
      if (container.classList.contains('theme-blue')) {
        themeBtn.style.background = '#D10D88';
        themeBtn.innerText = 'Toggle Pink Theme';
      } else {
        themeBtn.style.background = '#04c8c8';
        themeBtn.innerText = 'Toggle Blue Theme';
      }
    });
"""
content = content.replace('// Pipeline Switching Logic', js_toggle + '\n    // Pipeline Switching Logic')

with open("intelligence-layer.html", "w") as f:
    f.write(content)
