from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

# Files customers can reach. Old Hekla page itself is handled as a redirect separately.
files = [p for p in ROOT.rglob('*') if p.is_file() and p.suffix.lower() in {'.html','.js','.xml'} and '.git' not in p.parts and p.as_posix() != (ROOT/'hekla-saunas/index.html').as_posix()]

for p in files:
    s = p.read_text(encoding='utf-8')
    old = s
    depth = len(p.relative_to(ROOT).parents) - 1
    assets = '../' * depth + 'assets/'
    maax = '../' * depth + 'maax-saunas/'

    # URLs and navigation.
    s = re.sub(r'((?:\.\./)*)hekla-saunas/', lambda m: m.group(1) + 'maax-saunas/', s, flags=re.I)
    s = re.sub(r'(<a\b[^>]*href=["\'][^"\']*maax-saunas/[^"\']*["\'][^>]*>)\s*Hekla\s*(</a>)', r'\1MAAX Saunas\2', s, flags=re.I)

    # Main homepage positioning.
    if p == ROOT/'index.html':
        s = s.replace('Pittsburgh Sauna | Hekla & Cal Saunas','Pittsburgh Sauna | MAAX & Cal Saunas')
        s = s.replace('Premium traditional, infrared and outdoor saunas from Hekla and Cal Saunas. Visit our Monroeville and Wexford showrooms.','Premium infrared and home saunas from MAAX Saunas and Cal Saunas. Visit our Monroeville and Wexford showrooms.')
        s = s.replace("url('assets/site-images/traditionelle-finnish-sauna-hekla-210x-indoor-fur-5-personen-5e88780510.jpg')","url('assets/hero-sauna.svg')")
        s = s.replace(".traditional{background-image:url('assets/site-images/traditionelle-finnish-sauna-hekla-210x-indoor-fur-5-personen-e19f1cc3ff.jpg')}",".traditional{background-image:url('assets/traditional-sauna.svg');background-color:#6d4b32}")
        s = s.replace(".infrared{background-image:url('assets/site-images/hekla-infrared-1280x840.jpg-0523534839.webp')}",".infrared{background-image:url('assets/infrared-sauna.svg');background-color:#5b3832}")
        s = s.replace(".outdoor{background-image:url('assets/site-images/hekla-outdoor-cabin-1280x840.jpg-2a0ae07c0f.webp')}",".outdoor{background-image:url('assets/outdoor-sauna.svg');background-color:#394b3d}")
        s = s.replace(".hekla{background-image:url('assets/site-images/hekla-outdoor-cabin-1280x840.jpg-2a0ae07c0f.webp')}",".maax{background-image:url('assets/infrared-sauna.svg');background-color:#24383b}")
        s = s.replace('class="brandcard hekla" id="hekla"','class="brandcard maax" id="maax"')
        s = s.replace('<div class="brandname">HEKLA</div><p>Scandinavian craftsmanship and design across traditional, infrared and outdoor sauna formats.</p><a class="btn alt" href="maax-saunas/">Explore Hekla →</a>','<div class="brandname">MAAX SAUNAS</div><p>Premium SaunaWellness infrared saunas with multi-spectrum heat, wellness-focused features and 1–4 person options.</p><a class="btn alt" href="maax-saunas/">Explore MAAX Saunas →</a>')

    # Replace visible Hekla-specific imagery in educational pages with neutral category art.
    s = re.sub(r'https://heklasaunas\.com/[^\"\')]+', assets + 'traditional-sauna.svg', s, flags=re.I)
    s = re.sub(r'(?:\.\./)*assets/site-images/[^\"\')]*(?:hekla|traditionelle-finnish-sauna)[^\"\')]*', assets + 'traditional-sauna.svg', s, flags=re.I)
    s = re.sub(r'(?:\.\./)*assets/site-images/[^\"\')]*hekla-infrared[^\"\')]*', assets + 'infrared-sauna.svg', s, flags=re.I)

    # Brand-language cleanup. MAAX is infrared-focused, so traditional/outdoor references become category-neutral.
    replacements = {
        'Hekla & Cal Saunas':'MAAX Saunas & Cal Saunas',
        'Hekla and Cal Saunas':'MAAX Saunas and Cal Saunas',
        'Hekla, when Cal Saunas':'MAAX Saunas, when Cal Saunas',
        'Hekla Traditional':'traditional sauna',
        'Hekla traditional':'traditional sauna',
        'Hekla Infrared':'MAAX infrared',
        'Hekla infrared':'MAAX infrared',
        'Hekla Outdoor':'outdoor sauna',
        'Hekla outdoor':'outdoor sauna',
        'Hekla heater':'sauna heater',
        'Hekla heaters':'sauna heaters',
        'Hekla model':'sauna model',
        'Hekla models':'sauna models',
    }
    for a,b in replacements.items(): s=s.replace(a,b)

    # No obsolete brand should remain in customer-facing copy.
    s = re.sub(r'\bHEKLA\b','MAAX SAUNAS',s)
    s = re.sub(r'\bHekla\b','MAAX Saunas',s)

    # Sitemap migration.
    if p.name == 'sitemap.xml':
        s = s.replace('https://pittsburghsauna.com/hekla-saunas/','https://pittsburghsauna.com/maax-saunas/')

    if s != old:
        p.write_text(s, encoding='utf-8')
        print('updated', p.relative_to(ROOT))
