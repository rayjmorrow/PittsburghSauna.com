from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]

for html in ROOT.rglob('index.html'):
    rel = html.relative_to(ROOT)
    text = html.read_text(encoding='utf-8')
    # Remove any previous Bubbles include so reruns stay idempotent.
    text = re.sub(r'<script\s+src=["\'][^"\']*assets/bubbles\.js[^"\']*["\']\s+defer></script>\s*', '', text, flags=re.I)
    depth = len(rel.parts) - 1
    prefix = '../' * depth
    tag = f'<script src="{prefix}assets/bubbles.js?v=20260821-1" defer></script>'
    if '</body>' in text:
        text = text.replace('</body>', tag + '</body>', 1)
        html.write_text(text, encoding='utf-8')
        print(f'Installed Bubbles on {rel}')
    else:
        print(f'Skipped {rel}: no </body> tag')
