import re

# Update HTML
with open("intelligence-layer.html", "r") as f:
    html = f.read()

# Fonts and Icons
html = html.replace(
    '<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">',
    '<link href="https://fonts.googleapis.com/css2?family=DM+Sans:opsz,wght@9..40,400;9..40,500;9..40,600;9..40,700&family=Space+Grotesk:wght@400;500;600;700&family=Geist+Mono:wght@300;400;500;600;700&display=swap" rel="stylesheet">\n  <script src="https://unpkg.com/@phosphor-icons/web"></script>'
)

# Hide found tag
html = html.replace('<div class="intel-tag intel-tag-found">', '<div class="intel-tag intel-tag-found" style="display: none;">')

# Gathering context tag
old_gathering = """        <div class="intel-tag intel-tag-gathering">
          <svg class="intel-processing-icon" viewBox="0 0 16 22" width="16" height="22" xmlns="http://www.w3.org/2000/svg">
            <path d="M1.100 15.050C0.733 14.417 0.458 13.767 0.275 13.100C0.092 12.433 0.000 11.750 0.000 11.050C0.000 8.817 0.775 6.917 2.325 5.350C3.875 3.783 5.767 3.000 8.000 3.000C8.000 3.000 8.175 3.000 8.175 3.000C8.175 3.000 6.575 1.400 6.575 1.400C6.575 1.400 7.975 0.000 7.975 0.000C7.975 0.000 11.975 4.000 11.975 4.000C11.975 4.000 7.975 8.000 7.975 8.000C7.975 8.000 6.575 6.600 6.575 6.600C6.575 6.600 8.175 5.000 8.175 5.000C8.175 5.000 8.000 5.000 8.000 5.000C6.333 5.000 4.917 5.588 3.750 6.763C2.583 7.938 2.000 9.367 2.000 11.050C2.000 11.483 2.050 11.908 2.150 12.325C2.250 12.742 2.400 13.150 2.600 13.550C2.600 13.550 1.100 15.050 1.100 15.050ZM8.025 22.000C8.025 22.000 4.025 18.000 4.025 18.000C4.025 18.000 8.025 14.000 8.025 14.000C8.025 14.000 9.425 15.400 9.425 15.400C9.425 15.400 7.825 17.000 7.825 17.000C7.825 17.000 8.000 17.000 8.000 17.000C9.667 17.000 11.083 16.413 12.250 15.238C13.417 14.063 14.000 12.633 14.000 10.950C14.000 10.517 13.950 10.092 13.850 9.675C13.750 9.258 13.600 8.850 13.400 8.450C13.400 8.450 14.900 6.950 14.900 6.950C15.267 7.583 15.542 8.233 15.725 8.900C15.908 9.567 16.000 10.250 16.000 10.950C16.000 13.183 15.225 15.083 13.675 16.650C12.125 18.217 10.233 19.000 8.000 19.000C8.000 19.000 7.825 19.000 7.825 19.000C7.825 19.000 9.425 20.600 9.425 20.600C9.425 20.600 8.025 22.000 8.025 22.000Z" fillRule="nonzero" fill="currentColor" />
          </svg>
          Gathering context...
        </div>"""
new_gathering = """        <div class="intel-tag intel-tag-gathering">
          <i class="ph ph-asterisk intel-processing-icon" style="font-size: 16px;"></i>
          <span class="intel-shimmer-text">Gathering context...</span>
        </div>"""
html = html.replace(old_gathering, new_gathering)

# Replace SVG in Top Node
top_svg = """          <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor">
            <path d="M3 21h18v-2H3v2zm12-4V5H9v12h6zM5 17h2v-4H5v4zm12 0h2v-8h-2v8z" />
          </svg>"""
html = html.replace(top_svg, '          <i class="ph ph-stack" style="font-size: 24px;"></i>')

# Replace SVG in Mid Node
mid_svg = """          <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor">
             <path d="M3 21h18v-2H3v2zm12-4V5H9v12h6zM5 17h2v-4H5v4zm12 0h2v-8h-2v8z" />
          </svg>"""
html = html.replace(mid_svg, '          <i class="ph ph-chart-bar" style="font-size: 24px;"></i>')

# Replace SVG in Bot Node
bot_svg = """           <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor">
             <path d="M3 21h18v-2H3v2zm12-4V5H9v12h6zM5 17h2v-4H5v4zm12 0h2v-8h-2v8z" />
          </svg>"""
html = html.replace(bot_svg, '          <i class="ph ph-certificate" style="font-size: 24px;"></i>')

# Replace SVG in Output Node
out_svg = """          <svg viewBox="0 0 24 24" width="24" height="24" fill="currentColor">
            <path d="M14 2H6a2 2 0 0 0-2 2v16c0 1.1.9 2 2 2h12a2 2 0 0 0 2-2V8l-6-6zm4 18H6V4h7v5h5v11zM8 15h8v2H8v-2zm0-4h8v2H8v-2z" />
          </svg>"""
html = html.replace(out_svg, '          <i class="ph ph-file-dashed" style="font-size: 24px;"></i>')

with open("intelligence-layer.html", "w") as f:
    f.write(html)

# Update CSS
with open("assets/intelligence.css", "r") as f:
    css = f.read()

css = css.replace("font-size: 12px;", "font-size: 14px;")
css = css.replace("font-weight: 600;", "font-weight: 300;")

old_gathering_css = """.intel-tag-gathering {
  top: 14px;
  left: 320px;
  background-color: #D9C6CE;
  color: #666666;
  animation: float-center 6s ease-in-out infinite 0.5s;
}"""
new_gathering_css = """.intel-tag-gathering {
  top: 14px;
  left: 320px;
  transform: translate(-50%, 0px);
  background-color: #EFEFEF;
  color: #666666;
  animation: float-center 6s ease-in-out infinite 0.5s;
}

.intel-shimmer-text {
  background: linear-gradient(90deg, #666666 0%, #b3b3b3 50%, #666666 100%);
  background-size: 200% auto;
  color: transparent;
  -webkit-background-clip: text;
  background-clip: text;
  animation: text-shimmer 3s linear infinite;
}

@keyframes text-shimmer {
  0% { background-position: 200% center; }
  100% { background-position: -200% center; }
}"""
css = css.replace(old_gathering_css, new_gathering_css)

with open("assets/intelligence.css", "w") as f:
    f.write(css)
