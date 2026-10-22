"""Check built HTML for broken local URLs, missing images and metadata."""
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit, unquote
import sys

root = Path(sys.argv[1] if len(sys.argv) > 1 else '_site')
errors = []
class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links, self.ids, self.images, self.canonical = [], set(), [], []
        self.title = self.description = self.main = self.h1 = False
    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if 'id' in a: self.ids.add(a['id'])
        if tag == 'a' and 'href' in a: self.links.append(a['href'])
        if tag == 'link' and a.get('rel') in ['stylesheet', 'icon']: self.links.append(a['href'])
        if tag == 'link' and a.get('rel') == 'canonical': self.canonical.append(a['href'])
        if tag == 'img':
            self.images.append(a)
            self.links.append(a.get('src', ''))
        if tag == 'title': self.title = True
        if tag == 'main': self.main = True
        if tag == 'h1': self.h1 = True
        if tag == 'meta' and a.get('name') == 'description': self.description = bool(a.get('content'))

pages = {}
for path in root.rglob('*.html'):
    page = Page()
    text = path.read_text()
    page.feed(text)
    pages[path.resolve()] = page
    if not all([page.title, page.description, page.main, page.h1]): errors.append(f'{path}: missing page structure/metadata')
    if len(page.canonical) != 1 or not page.canonical[0].startswith('https://ahmedfadhluddin.com/'): errors.append(f'{path}: invalid canonical')
    if 'Theoretical Physics student' in text: errors.append(f'{path}: obsolete shared biography')
    for img in page.images:
        if not all(k in img for k in ['alt', 'width', 'height']): errors.append(f'{path}: image missing accessibility/dimensions')
for path, page in pages.items():
    for link in page.links:
        url = urlsplit(link)
        if url.scheme or url.netloc: continue
        target = root / unquote(url.path).lstrip('/') if url.path.startswith('/') else path.parent / unquote(url.path)
        if not url.path: target = path
        if target.is_dir(): target /= 'index.html'
        if not target.is_file(): errors.append(f'{path}: broken link {link}')
        elif url.fragment and target.resolve() in pages and unquote(url.fragment) not in pages[target.resolve()].ids: errors.append(f'{path}: missing fragment {link}')
for route in ['index.html', 'research/index.html', 'projects/index.html', 'about/index.html', 'posts/index.html', 'categories/index.html', 'tags/index.html', 'blog/Welcome-website/index.html', '404.html', 'feed.xml', 'sitemap.xml']:
    if not (root / route).is_file(): errors.append(f'Missing route: {route}')
if errors:
    print('\n'.join(errors)); sys.exit(1)
print(f'PASS: {len(pages)} HTML pages; local links, fragments, image dimensions/alt text, canonical URLs and preserved routes.')
