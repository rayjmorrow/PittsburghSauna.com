from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
HTFO = 'https://hottubfactoryoutlet.com/'
PS = 'https://pittsburghsauna.com/'

pattern = re.compile(
    r'<a class="brand" href="[^"]*">(?P<img><img\s+[^>]*htfo-logo-approved\.jpg[^>]*>)(?P<ps><span class="ps">.*?</span>)</a>',
    re.I | re.S,
)

changed = []
for p in ROOT.rglob('*.html'):
    s = p.read_text(encoding='utf-8')
    def repl(m):
        return (
            '<div class="brand">'
            f'<a class="htfo-logo-link" href="{HTFO}" aria-label="Hot Tub Factory Outlet home">{m.group("img")}</a>'
            f'<a class="ps-logo-link" href="{PS}" aria-label="Pittsburgh Sauna home">{m.group("ps")}</a>'
            '</div>'
        )
    out, n = pattern.subn(repl, s)
    if n:
        p.write_text(out, encoding='utf-8')
        changed.append(str(p.relative_to(ROOT)))

print(f'Updated {len(changed)} pages')
for rel in changed:
    print(rel)
