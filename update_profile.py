#!/usr/bin/env python3
import re

# Read the file
with open('index.html', 'r') as f:
    content = f.read()

# Update Contact Section - Replace the entire section id="five"
contact_new = '''			<section id="five">
				<div class="container actions special">
					<h3>Get In Touch</h3>
					<p>Let's connect to discuss backend systems, AI architecture, or collaboration opportunities.</p>
					<ul class="feature-icons">
						<li class="icon solid fa-envelope"><a href="mailto:arun.dakshana17@gmail.com">arun.dakshana17@gmail.com</a></li>
						<li class="icon solid fa-phone">+91-7049245976</li>
						<li class="icon brands fa-linkedin"><a href="https://linkedin.com/in/arun-kumar-bisariya-42599b192" target="_blank">LinkedIn</a></li>
						<li class="icon brands fa-github"><a href="https://github.com/arunkb2000" target="_blank">GitHub</a></li>
					</ul>
				</div>
			</section>'''

# Replace the contact section
content = re.sub(
    r'<section id="five">.*?</section>',
    contact_new,
    content,
    flags=re.DOTALL,
    count=1
)

# Update Projects Section - Replace section id="two"
projects_new = '''			<section id="two">
				<div class="container">
					<h3>Projects</h3>
					<div class="box alt">
						<!-- Featured Projects -->
						<div class="row gtr-50 gtr-uniform">
							<div class="col-6">
								<div style="border: 1px solid #ddd; border-radius: 8px; padding: 16px; background: #f9f9f9;">
									<span class="image proj fit"><img src="https://img.icons8.com/fluency/480/artificial-intelligence.png" alt="AI TTS" /></span>
									<h4 style="margin-top: 12px; margin-bottom: 8px;">Qwen3 Real-time TTS Engine</h4>
									<p style="font-size: 14px; color: #666; margin-bottom: 12px;">CUDA megakernel-backed streaming TTS pipeline integrating RTX 5090 Qwen decoder with Pipecat for frame-by-frame audio delivery.</p>
									<p><a href="https://github.com/arunkb2000/qwen3-tts-megakernel-pipecat" target="_blank" class="button primary small">→ Repository</a></p>
								</div>
							</div>
							<div class="col-6">
								<div style="border: 1px solid #ddd; border-radius: 8px; padding: 16px; background: #f9f9f9;">
									<span class="image proj fit"><img src="https://img.icons8.com/fluency/480/inventory.png" alt="Inventory" /></span>
									<h4 style="margin-top: 12px; margin-bottom: 8px;">Inventory Order Management</h4>
									<p style="font-size: 14px; color: #666; margin-bottom: 12px;">Full-stack web app for products, customers, orders, and stock tracking. FastAPI + React + PostgreSQL + Docker.</p>
									<p><a href="https://github.com/arunkb2000/inventory-order-management-system" target="_blank" class="button primary small">Repository</a> · <a href="https://inventory-order-management-system-khaki.vercel.app/" target="_blank" class="button primary small">Live App</a></p>
								</div>
							</div>
						</div><br>

						<!-- Other Projects -->
						<p style="font-size: 14px; color: #666; margin-bottom: 16px;"><strong>Other Projects</strong></p>
						<div class="row gtr-50 gtr-uniform">
							<div class="col-6"><a href="https://github.com/arunkb2000/OS-Content-Management-System" target="_blank" ><span class="image proj fit"><img src="https://www.theedigital.com/wp-content/uploads/2015/01/reasons-to-use-a-content-management-system.png" alt="CMS" /></span><li class="button primary icon solid fa-arrow-circle-right">OS Content Management System</li></a>
							</div>
							<div class="col-6"><a href="https://github.com/arunkb2000/ToDoList" target="_blank" ><span class="image proj fit"><img src="https://blog.hubspot.de/hubfs/Germany/Blog_images/to-do-listen-apps.png" alt="Todo" /></span><li class="button primary icon solid fa-arrow-circle-right">C-Todo List</li></a>
							</div>
						</div><br>
						<div class="row gtr-50 gtr-uniform">
							<div class="col-6"><a href="https://github.com/arunkb2000/CurrentWeather" target="_blank" ><span class="image proj fit"><img src="https://turkeytravelweb.com/wp-content/uploads/2017/10/weather-496x300.jpeg" alt="Weather" /></span><li class="button primary icon solid fa-arrow-circle-right">WeatherApp</li></a>
							</div>
							<div class="col-6"><a href="https://arunkb2000.github.io/profile/bindex.html" target="_blank" ><span class="image proj fit"><img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRtC5Kc2ShEOvbAGYz7MtbKPVMUPLYHoHfaf-sAqHR-DRzPNq3GCzNnFFi_kq9b7qJGM2I&usqp=CAU" alt="Blog" /></span><li class="button primary icon solid fa-arrow-circle-right">BlogWebsite</li></a>
							</div>
						</div><br>
						<div class="row gtr-50 gtr-uniform">
							<div class="col-6"><a href="https://arunkb2000.github.io/profile/Drindex.html" target="_blank" ><span class="image proj fit"><img src="https://www.pngarts.com/files/3/Yamaha-Drum-PNG-High-Quality-Image.png" alt="Drums" /></span><li class="button primary icon solid fa-arrow-circle-right">DrumSet</li></a>
							</div>
							<div class="col-6"><a href="https://arunkb2000.github.io/profile/form/index.html" target="_blank" ><span class="image proj fit"><img src="https://www.graphicsfuel.com/wp-content/uploads/2013/10/flat-login-register-psd-ui.jpg" alt="Form" /></span><li class="button primary icon solid fa-arrow-circle-right">Registration Form</li></a>
							</div>
						</div>
					</div>
				</div>
			</section>'''

# Replace the projects section (section id="two")
content = re.sub(
    r'<section id="two">.*?</section>',
    projects_new,
    content,
    flags=re.DOTALL,
    count=1
)

# Write back
with open('index.html', 'w') as f:
    f.write(content)

print("✅ Profile updated successfully!")
print("Changes made:")
print("1. ✅ Replaced Typeform contact section with simple contact info")
print("2. ✅ Removed 'Note: Typeform submissions...' message")
print("3. ✅ Restructured projects with featured section on top")
print("4. ✅ Moved Qwen3 TTS and Inventory Management to featured projects")
print("5. ✅ Renamed Megakernel to 'Qwen3 Real-time TTS Engine'")
print("6. ✅ Added styled boxes with visible repo/live links")
print("7. ✅ Reordered other projects below featured section")
