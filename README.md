# Ahmed Fadhluddin

A small, static personal website built with Jekyll 3.10 and plain CSS. No runtime JavaScript, remote fonts, theme download or runtime logo services.

## Local preview

Use a current Ruby (tested with Ruby 3.4.3) and Bundler:

```sh
bundle config set --local path vendor/bundle
bundle install
bundle exec jekyll serve
```

Open http://127.0.0.1:4000. Restart the server after changing `_config.yml`.
On this Mac, Homebrew Ruby is at `/usr/local/opt/ruby/bin`; prepend it to `PATH` if your shell selects Apple's system Ruby 2.6.

Production verification (stop the preview server first so it doesn't overwrite the build):

```sh
JEKYLL_ENV=production bundle exec jekyll build --strict_front_matter
python3 scripts/check_site.py
```

The link checker uses Python's standard library. It checks local routes and fragments, assets, image dimensions and alt text, page structure, canonical URLs and the historical welcome-post URL.

## Editing

- Homepage copy: `_includes/introduction.html`. `/about/` reuses it, so the two cannot drift.
- Name, portrait and social links: `_data/profile.yml`.
- Research titles, full authors, summaries and source links: `_data/research.yml`. See `docs/research-sources.md` for verification and status provenance.
- Unpublished research titles, dates and availability: `_data/unpublished_research.yml`.
- Projects: `_pages/projects.html`.
- Navigation: `_data/navigation.yml`.
- Typography and layout: `assets/css/main.css`.
- Historical writing: `_posts/`. Keep filenames, categories and the existing permalink pattern to retain URLs. The welcome post is at `/blog/Welcome-website/`; the archive remains at `/posts/`. There is no main Writing link because the repository currently contains only a short welcome post and an empty draft. The draft is preserved untouched and omitted from archive listings; its route still builds.

### Portrait

The supplied `ahmed profille photo.jpeg` has been optimised into `assets/images/ahmed.jpg`. Replace that file, or change `portrait.path` in `_data/profile.yml`. Set `width` and `height` there to the new image's actual dimensions. CSS preserves the image's aspect ratio, with no forced crop. The same path supplies social preview metadata. The original photo remains untouched.

### Organisation logos

Use `{% include organisation.html id="jump" %}` in HTML or Markdown prose. Names, paths and intrinsic dimensions are in `_data/organisations.yml`; actual files live in `assets/logos/`. Keep dimensions accurate, proportions intact and source colours unchanged. The include checks whether the configured file exists and gracefully shows just the text if it does not. Decorative logo images have empty alt text because the visible organisation name is already accessible.

`argo` displays the literal label **&lt;hidden name&gt;**, using the supplied company mark. Its `dark_background` setting provides contrast for the white artwork. No company website is inferred. All eight requested logos are supplied locally; no replacement is required. Provenance is recorded in `docs/asset-sources.md`.

## GitHub Pages deployment

The original repository uses Jekyll at the repository root, with no custom workflow. Its public default branch is `master` and GitHub reports Pages enabled. This redesign retains that build model, the custom domain `https://ahmedfadhluddin.com`, an empty `baseurl`, the existing post permalink pattern and only GitHub Pages-supported plugins (`jekyll-feed`, `jekyll-sitemap`). Local Jekyll and plugin versions match GitHub Pages' published versions. Dependencies are locked for reproducibility.

Work is on `redesign/editorial-personal-site`. **No merge, push or deployment has been performed.** After explicit approval, review and merge the branch into the configured publishing branch. Confirm Settings → Pages uses the intended branch/root; the authenticated Pages settings could not be inspected in this session. GitHub Pages will build the root Jekyll source normally. Do not commit `_site/` or `vendor/`.

## Design and review

The custom layouts replace Minimal Mistakes completely; no theme code or assets were copied. Historical post text is retained. No theme licence file existed in the original checkout, and there is no retained theme code requiring bundled attribution. Organisation trademarks remain their owners' property.

The implementation uses original copy and layout code, with narrow navigation, a readable text column and restrained typography around Ahmed's portrait and biography.

Screenshots and verification notes are in `docs/`. The local browser checks used installed Google Chrome through a temporary Playwright installation; no Node dependency is required to build or serve the website.

Review screenshots: [desktop](docs/screenshots/home-1440.png), [tablet](docs/screenshots/home-768.png), [mobile](docs/screenshots/home-390.png). Full checks and external-access limitations: [verification notes](docs/verification.md).


## Custom domain

`CNAME` contains `ahmedfadhluddin.com`; `_config.yml` uses its HTTPS URL for canonical links, social metadata, feed and sitemap. Set the same custom domain in GitHub Settings → Pages before pointing DNS at GitHub. Publish the configuration changes through the normal branch/PR process.

At the DNS provider, set four apex (`@`) A records to `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, and `185.199.111.153`. Set `www` as a CNAME to `afadhluddin.github.io`. Replace conflicting website records; retain mail and verification records. Enable Enforce HTTPS in Pages once the certificate is ready.
