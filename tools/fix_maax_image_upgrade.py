from pathlib import Path
p=Path(__file__).resolve().parents[1]/'maax-saunas/index.html'
s=p.read_text(encoding='utf-8')
s=s.replace('</div></article></div></article>','</div></div></article>')
s=s.replace("<title>MAAX Saunas Pittsburgh | SaunaWellness Infrared Saunas</title>","<title>MAAX Saunas Pittsburgh | Indoor & Outdoor Saunas</title>")
s=s.replace('content="Explore MAAX SaunaWellness infrared saunas in Pittsburgh. Compare 1, 2, 3 and 4 person MAAX infrared sauna options at Pittsburgh Sauna in Monroeville and Wexford."','content="Explore MAAX Saunas in Pittsburgh, including premium indoor infrared and SX Outdoor sauna options at Pittsburgh Sauna in Monroeville and Wexford."')
s=s.replace("<div class=\"model-photo\" style=\"background-image:url('../assets/site-images/Solara-Outdoor-product-img-2-a97e1336a8.webp');background-size:cover\"></div>","<div class=\"model-photo\" style=\"background:linear-gradient(135deg,#30251d,#8d6b4a);display:grid;place-items:center;color:#fff;font:700 28px Georgia,serif;text-align:center;padding:20px\">MAAX SX<br>OUTDOOR SERIES</div>")
p.write_text(s,encoding='utf-8')
print('fixed MAAX page markup and outdoor placeholder')
