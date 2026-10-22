# Verification — 22 October 2026

## Implementation and deployment

- Dedicated branch: `redesign/editorial-personal-site`.
- Jekyll retained; custom Liquid layouts and plain CSS replace the remote Minimal Mistakes theme.
- Public repository metadata confirms Pages enabled and default branch `master`. No custom deployment workflow exists in the checkout. Authenticated hosting settings were unavailable because the local GitHub CLI token is invalid.
- No push, merge or deployment performed. Review the local commit/diff; a remote PR was not created because GitHub CLI authentication failed.
- Original welcome post, empty untracked draft and both supplied source images remain untouched. The old portrait remains available at its existing path.

## Browser checks

Real installed Google Chrome, controlled through Playwright with an isolated temporary browser profile. Nine routes checked at **1440, 768, 390 and 320px** (36 page/viewport combinations): homepage, Research, Projects, About, writing archive, historical welcome post, category archive, tag archive and 404 page.

- No horizontal overflow, failed images, browser exceptions or HTTP errors on these local routes.
- Navigation links resolve and show the correct current-page state.
- Keyboard skip link is the first focus target and moves focus into the main content.
- Full-page screenshots saved for the homepage, Research, Projects and historical article at 1440, 768 and 390px.
- Portrait keeps the supplied square framing, at 124px desktop / 112px mobile; mobile navigation is horizontal.
- All eight official organisation marks load beside readable names. Images are decorative to screen readers and have explicit intrinsic dimensions.
- Inspected desktop/mobile screenshots against the rendered reference homepage and article. The reference's main text column measured 647px with 16px type and 27.2px line-height; this design uses a 650px column with the same body size and line-height, adapting the heading/portrait arrangement to Ahmed's introduction.
- Reference article embeds had some rendering failures on the reference website; the text column, headings, spacing and navigation remained inspectable.

Raw local checks: `browser-results.json`. Browser script: `scripts/browser_check.cjs`. To rerun, install Playwright in a temporary tools directory, start Jekyll, then invoke the script with `NODE_PATH` pointing at that tools directory's `node_modules`. It uses installed Chrome and does not add runtime dependencies to the website.

## Build and links

Production Jekyll build with strict front matter and safe mode (GitHub Pages-compatible plugin loading), followed by `python3 scripts/check_site.py`. The checker covers all ten generated HTML pages, including the preserved empty draft route, all local links/fragments, image dimensions/alt text, production canonical URLs and historical routes. Feed and sitemap are generated. `git diff --check` is clean.

External checks: GitHub profile and arXiv respond HTTP 200. LinkedIn returns HTTP 999 and ChemRxiv HTTP 403 to automated clients; these are access restrictions, not confirmed broken links. Exact user-supplied profile and paper URLs are retained. ChemRxiv metadata is verified through its publisher-deposited Crossref DOI record. See `research-sources.md`.

## Remaining limitations

No required assets are missing. The two research links represent distinct preprints, so no duplicate-paper discrepancy exists. “Under review” remains the author's supplied status. Rokos's official compact icon is only 20px, adequate at its 18px display size; a higher-resolution official mark would improve high-DPI sharpness. Full accessibility auditing and authenticated GitHub Pages deployment were outside local verification.
