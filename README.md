# Piripi & Sons Real Estate

## SEO content system (17 Nov 2026)

The source-controlled `content/pages.json` is built by `python scripts/build_content_pages.py` into ordinary crawlable HTML under `public/`, plus the canonical XML sitemap. The Google Search Essentials and REA/Settled/LINZ notes are small italic asterisk footnotes at the end of relevant content sections. `python scripts/check_seo.py` checks the generated site for broken links, canonical/title/H1/schema/sitemap problems and unverified protected licence wording. GitHub Actions runs these checks on pull requests before any merge; only a push to `main` may run Wrangler deployment. No JavaScript rendering is required for primary content.


A responsive, static-first real estate information and enquiry site for Piripi & Sons, with **17 published canonical pages** at [piripiproperty.com](https://piripiproperty.com).

## Site

- `public/index.html`: desktop image and enquiry form use equal-height columns, with the original photograph fully visible (no crop or vignette); screens at 840px and narrower stack the image above the form, and scrolling keeps the form accessible.
- `public/assets/piripi-and-sons-real-estate.jpg`: Corrie’s supplied team photograph with PIRIPI & SONS REAL ESTATE branding
- The earlier crayon artwork is kept in the repository solely for rollback, and is no longer shown on the site
- `public/assets/site.css`: shared black/gold/silver design system, responsive split-layout homepage and contact-page styles
- `public/assets/enquiry-form.js` and `functions/api/enquiry.js`: same-origin POST can send a validated enquiry through Brevo **only after this Pages project has a configured secret and recipient**. The live readiness check currently reports `ready:false`, so the site prepares an email-app fallback instead. Never claim direct delivery until a test message reaches the intended inbox. No private client mailbox or provider secret is embedded in public JavaScript.
- `public/assets/brand/*`: original vector monogram tracing plus stacked/horizontal brand lockups
- `public/favicon.svg`, `public/favicon.ico`, `public/favicon-32.png`, `public/apple-touch-icon.png`: matching logo-based favicon and touch-icon set
- `public/site.webmanifest`: web app identity/colour tokens
- `public/_headers`: Cloudflare Pages headers

## Current release and QA evidence (18 November 2026)

Read the [authoritative session-close handover](docs/operations/handovers/PIRIPI-SEO-SESSION-CLOSE-2026-11-18.md) before starting new development. The user approved the latest compact portrait and editorial About design.

**Verified production release:** [GitHub Actions 44072449332](https://github.com/meeeeeooooowwwwwww/piripiproperty.com/actions/runs/44072449332) passed with 17/17 published pages HTTP 200, canonical/H1/meta and security checks, pages.dev noindex, healthy `/api/enquiry` GET, all linked static assets, and 18/18 real Chromium mobile/tablet/desktop browser checks. Screenshots are retained as 7-day GitHub Actions artifacts. Nine enquiry unit tests pass, but direct email delivery remains **not configured**.

Run these release checks locally or in GitHub Actions:

```bash
python scripts/build_content_pages.py
python scripts/check_seo.py
node --test tests/enquiry-function.test.mjs
# With Playwright and Chromium installed:
python scripts/audit_responsive.py
# After a real Cloudflare deploy:
python scripts/audit_live.py
```

Avoid duplicating the existing deployment, removing the user-approved layout, or treating self-reported licensing as independent NZ REA verification.

## Independent Cloudflare deployment

This repository deploys **only** to the Cloudflare Pages project `piripiproperty`.
It does not deploy to, or depend on, GRID EATER or any other website's Worker.

- Production URL: https://piripiproperty.com
- Cloudflare Pages project: `piripiproperty`
- Fallback URL: https://piripiproperty.pages.dev
- Configuration: `wrangler.toml`
- Workflow: `.github/workflows/deploy-pages.yml`
- Trigger: each push to `main` and manual workflow dispatch
- Command: `wrangler pages deploy public --project-name=piripiproperty --branch=main`

The Pages project was initially created using **Direct Upload**, and subsequent updates use Wrangler from this repository's GitHub Actions workflow. Do not add a competing Pages Git integration or deploy a different project's files to this Pages project.

The repository secret `PIRIPIPROPERTY_CLOUDFLARE_API_TOKEN` is required. It must be a Cloudflare API token with **Account → Cloudflare Pages → Edit** access, stored in GitHub Actions secrets. No token values are checked into source control.

## Local deploy

Install Wrangler or run via npx, then authenticate with a Cloudflare API token and run:

```bash
npx wrangler pages deploy public --project-name=piripiproperty --branch=main
```

Keep the project name and output directory unchanged; those explicitly isolate this website.

## Social sharing previews

The page declares absolute Open Graph and X/Twitter Card metadata for \`https://piripiproperty.com/\`.
The CI workflow runs \`scripts/build_social_image.py\`, which renders a 1200x630 JPEG at
\`/social-preview.jpg\` from Corrie’s supplied team photograph. The entire photograph, including logo and people,
is preserved inside the social card with blurred side-fill rather than cropping. At build time,
`GITHUB_SHA` is applied to the OG/Twitter image URL as a cache-busting `?v=` query while the
stable `/social-preview.jpg` image remains available to previously published links.

The public pages and assets send `Cache-Control: no-cache, max-age=0, must-revalidate`
during active development. Third-party platforms such as Substack may cache the *page
URL itself*, which no website cache header can forcibly clear. To test a fresh Substack
embed, delete the old card and paste a fresh query URL, for example
`https://piripiproperty.com/?preview=20261113-2`, after a completed deployment.

To refresh a cached Facebook link preview, use https://developers.facebook.com/tools/debug/
and choose **Scrape Again** for https://piripiproperty.com/ .

## Updated site design, portrait and licence research (17 Nov 2026)

The user-approved provisional portrait is kept as `public/assets/corrie-piripi-professional.webp` (~44 KB, 900px wide), backed up in Corrie's Google Drive client folder. It is an AI-assisted enhancement of a 200px original photo and must not be misrepresented as untouched original photography. The site uses it for `/about/`, `/about/corrie-piripi/`, and a modest home trust feature. The supplied five-person homepage brand photo is untouched.

The navigation keeps seven clear content destinations; at mobile widths, the toggle is a three-line icon with an accessible label but **no visible Menu text**. Generated editorial pages use numbered sections, citations as small italic `*` source lines, a verified-name Person entity and an accessible layout with a single H1. The homepage keeps one semantic main landmark and a sourced professional profile feature.

Corrie directly told the site owner that his Australian real estate licence was transferred to NZ. REA confirms formal Trans-Tasman recognition exists, but the exact NZ licence class, conditions and supervising agency are not yet known. See https://www.rea.govt.nz/real-estate-professionals/apply-for-your-licence/if-you-have-an-australian-licence-or-registration/ . Do **not** label him a `licensed real estate agent` until an NZ agent-class licence is verified; generic real estate professional wording remains appropriate.

## Corrie Piripi professional profile

`/about/corrie-piripi/` is generated from public source-backed professional history. The 2016 Real Estate Business profile mentions his role as chief executive of Just Property Management, the 2022 Coronis feature discusses his Australian franchise work, and LinkedIn lists professional development and community volunteer activities. These are *historical* and do not establish current NZ licence or agency authority. The current LinkedIn 200×200 photo URL is not a reliable, rights-cleared high-resolution portrait. Do not substitute a synthetic likeness or externally hotlink the expiring social image. Keep professional photograph addition pending a usable original and Corrie's consent. Expand only when identity, qualifications and personal details are verified.

## Initial public pages

- `/`: branded home with uncropped team photograph and right-side enquiry form on desktop; the form is below the photograph on mobile. The form POSTs to `/api/enquiry`; requires the Cloudflare Pages secret below for live direct delivery.
- `/international/`: low-prominence public information for NZ property enquiries from overseas. This is not a commitment to nationwide travel, investor advice, foreign-buyer eligibility assessments or representation before agency/client verification.
- `/contact/`: Corrie Piripi's phone and business email, including `tel:` and `mailto:` links.
- `/sitemap/`: readable navigation to all published content, services and contact.
- `/sitemap.xml`: canonical machine-readable sitemap, automatically updated to include every generated published content URL.

These pages use the same Google tag and social-preview image as the homepage. International is linked discreetly from the footer and sitemaps; the header navigation remains Home/Contact until Corrie's service authority and geographic coverage are confirmed. Public SEO and structured data use the supplied brand **Piripi & Sons Real Estate** and name Corrie Piripi as a licensed real estate professional. `piripiproperty.com` remains the canonical domain. There is no assertion of a verified legal company name, independent agency/brokerage status, licence number or registered office. Add verified supervising agency and legal particulars once supplied by Corrie.

## Private enquiry delivery (Cloudflare Pages)

The form uses the **independent** Pages Function at `/api/enquiry`, not browser `mailto:`.
Configure **production** variables in Cloudflare > Workers & Pages > `piripiproperty` > Settings > Variables and Secrets, and redeploy after changing them:

- `BREVO_API_KEY` (**encrypted secret, required**): existing Brevo transactional API credential. If a secret of this name is accessible to this **particular GitHub repository**, the deploy workflow attempts to sync it securely to the Piripi Cloudflare Pages project. A key kept only in the separate GRID EATER repository is **not** automatically available to this repository. You can alternatively add the secret directly in Cloudflare Pages. Never place the API key in committed code or browser scripts.
- `ENQUIRY_TO_EMAIL` (**encrypted secret, optional**): Corrie's private Gmail address after it is confirmed. Its value must not appear in the public GitHub repository or static assets. Without this setting, email defaults to `david@americafirst.co.nz` as the temporary inbox.
- `BREVO_FROM_EMAIL` (optional): default `david@grideater.com`, which must remain a verified Brevo sender. This is the sender, not the visitor's reply address.

Brevo does **not** require recipients to click a verification link, but **does** require an authorised sender and API key. The form is **not live direct-send** until `BREVO_API_KEY` is present and an end-to-end test succeeds. If unavailable, visitors receive an explicit error and can use the manual email-app alternative or phone Corrie. Do **not** claim an email was sent without a provider acknowledgement. When Corrie's Google Workspace is ready, change only the private recipient variable.

Abuse controls: same-origin-only JSON POSTs, field allowlist/length checks, minimum completion time and honeypot. Before promoting paid traffic, add Turnstile server-side validation and Cloudflare rate limiting for further abuse resistance.

All visible enquiry fields, including the visitor's phone number and message, are mandatory. Both client and server reject missing values. The layout has a 2-column compact form beside the original photograph; mobile uses one field per row.
