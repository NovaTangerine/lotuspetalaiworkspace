with open("assets/intelligence.css", "r") as f:
    css = f.read()

# Make the source nodes smooth
old_node_css = """.intel-node-source {
  width: 74px;
  height: 74px;
  background: white;
  border: 1px solid var(--theme-inactive);
  color: #B3B3B3;
  animation: float 6s ease-in-out infinite;
}

.intel-node-source.active {
  background: linear-gradient(135deg, var(--stream-bright), var(--stream-primary));
  color: white;
  border: none;
  box-shadow: 0px 4px 12px var(--stream-glow);
  animation: float 6s ease-in-out infinite 1s, pulse 3s infinite;
}"""

new_node_css = """.intel-node-source {
  width: 74px;
  height: 74px;
  background: white;
  border: 1px solid var(--theme-inactive);
  color: #B3B3B3;
  animation: float 6s ease-in-out infinite;
  transition: all 1.2s ease-in-out;
  position: relative;
}

.intel-node-source > * {
  position: relative;
  z-index: 1;
}

.intel-node-source::before {
  content: "";
  position: absolute;
  inset: 0;
  border-radius: inherit;
  background: linear-gradient(135deg, var(--stream-bright), var(--stream-primary));
  opacity: 0;
  transition: opacity 1.2s ease-in-out;
  z-index: 0;
}

.intel-node-source.active {
  color: white;
  border-color: transparent;
  box-shadow: 0px 4px 12px var(--stream-glow);
  animation: float 6s ease-in-out infinite 1s, pulse 3s infinite;
}

.intel-node-source.active::before {
  opacity: 1;
}"""

css = css.replace(old_node_css, new_node_css)

with open("assets/intelligence.css", "w") as f:
    f.write(css)

with open("intelligence-layer.html", "r") as f:
    html = f.read()

# Make line transitions
html = html.replace('<path id="active-path" class="intel-line-active"', '<path id="active-path" class="intel-line-active" style="transition: d 1.2s ease-in-out, stroke 1.2s ease-in-out;"')
html = html.replace('circle cx=', 'circle style="transition: stroke 1.2s ease-in-out;" cx=')
html = html.replace('circle id="spigot', 'circle style="transition: stroke 1.2s ease-in-out;" id="spigot')

# Slow down setInterval
html = html.replace('setInterval(switchPipeline, 2500)', 'setInterval(switchPipeline, 4000)')

with open("intelligence-layer.html", "w") as f:
    f.write(html)
