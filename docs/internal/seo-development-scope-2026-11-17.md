# Piripi & Sons Real Estate — Internal SEO Development Scope
**Status:** INTERNAL ENGINEERING SCOPE v2 — 2026 technical SEO hardening (not a client proposal, not a public launch approval)  
**Prepared:** 17 November 2026 (NZDT); research-verified update 17 November 2026  
**Site:** https://piripiproperty.com/  
**Repository:** https://github.com/meeeeeooooowwwwwww/piripiproperty.com

## 1. Product outcome and constraints

Build an SEO-first real-estate-agent website capable of generating qualified appraisal and seller enquiries **without** a property portfolio. Main thematic keyword family: **real estate agents**. Commercial priority: **Christchurch home sellers and appraisal requests**; Canterbury secondary; nationwide NZ subject-matter coverage without pretending to have offices or service coverage in unverified locations.

The full public identity is **Piripi & Sons Real Estate** (public brand, legal/agency status not yet independently verified); keep `piripiproperty.com` canonical and preserve supplied five-person artwork and black/gold/silver/ivory design.

**Non-goals in this release:** property listings/search, open homes, sold properties, fabricated testimonials, sales statistics or accolades, an automated online property valuation, nationwide fake location pages, CRM integration, real-estate portal integrations, new paid advertising, new paid third-party tools. Leave no empty Listings navigation item. These may become separate features after actual agency approvals and properties exist.

**Operating model:** independent Cloudflare Pages project `piripiproperty`, static content in `public/`, Pages Function at `functions/api/enquiry.js`, deploy via the existing Wrangler GitHub workflow. Keep the existing Cloudflare Pages/static HTML + Pages Functions hosting model. Evaluate a small static generator versus **Astro static-site generation with type-checked content collections** in a short proof-of-concept; select based on operational simplicity, output parity, SEO correctness, low JS and rollback. Do not introduce a client-side SPA, database or CMS without a proven need; preserve the existing production Wrangler deployment until migration tests pass.

## 2. Benchmark: 20 NZ real estate websites

This is a **qualitative pattern study**, not a measured ranking of the country's 20 best-performing sites. Reviewed publicly accessible website content/navigation on 17 November 2026; patterns only, no copying.

| # | Website | Page inspected / verified pattern | Take into Piripi |
|---|---|---|---|
| 1 | [Harcourts](https://harcourts.net/nz/) | [Find people](https://harcourts.net/nz/people), [seller guide](https://harcourts.net/nz/resources/selling/how-to-become-a-more-savvy-seller) | Search intent around selecting a salesperson, educational seller FAQs and evidence-based appraisals |
| 2 | [Ray White NZ](https://www.raywhite.co.nz/) | Find an agent, Insights and Property Appraisal visible in national navigation | Simple distinct trust and lead routes |
| 3 | [Bayleys](https://www.bayleys.co.nz/) | Free appraisal CTA, residential services and premium brand positioning | Prominent appraisal conversion and understated premium visuals |
| 4 | [Barfoot & Thompson](https://www.barfoot.co.nz/) | Buy/Sell structure, seller advice, local market reporting | Clear service taxonomy and regional information |
| 5 | [Property Brokers](https://www.propertybrokers.co.nz/) | Prominent "How can we help?" with appraisal vs general enquiry | Intent-based intake, adapted to no portfolio |
| 6 | [Tall Poppy](https://www.tallpoppy.co.nz/) | Book Appraisal and transparent marketing value proposition | One obvious seller action, plain-language offer |
| 7 | [Arizto](https://www.arizto.co.nz/) | What's Included / Our People / Book a Free Appraisal | Communicate what service entails before asking for a lead |
| 8 | [NZ Sotheby's International Realty](https://www.nzsothebysrealty.com/) | Segmented Sell / Agents / Regions / Insights | Elegant segmentation, not imitation of luxury claims |
| 9 | [LJ Hooker NZ](https://www.ljhooker.co.nz/) | Extensive selling/buying checklists, guides and appraisals | Resource clusters linking naturally into seller services |
| 10 | [Professionals](https://www.professionals.co.nz/) | Sell > Online Valuation / Market Appraisal / Selling Property | Explain appraisal vs valuation honestly; no fake instant valuations |
| 11 | [Tremains](https://www.tremains.co.nz/) | Sell > Request Appraisal / Our Agents / Advice & Guides | Seller-led navigation and guides |
| 12 | [EVES](https://www.eves.co.nz/) | Sell > Appraisal, preparing home, staging, auction, process | Practical consumer education rather than thin SEO pages |
| 13 | [Lodge](https://lodge.co.nz/) | Sell, appraisal, market reports, suburb info and FAQs | Local-market authority and recurring original insights |
| 14 | [Tommy's](https://tommys.co.nz/) | Sell/Marketing, FAQs, local community | Human, local service story and transparent process |
| 15 | [Lugtons](https://www.lugtons.co.nz/) | Repeated market-appraisal CTA and local market-stat commentary | Offer appraisal in multiple relevant sections, data with provenance |
| 16 | [Century 21 NZ](https://www.century21.co.nz/) | Sell > Appraisal / First Steps / Marketing Plan / Completing Sale | Selling-process hub with logical child topics |
| 17 | [First National NZ](https://firstnational.co.nz/) | Sell > Appraisal / Sellers Guide / Auction, resource glossary | Glossary and educational content architecture |
| 18 | [Ray White Metro Christchurch](https://rwmetro.co.nz/) | Local Sell > Strategies / Tips / Appraisal | Useful Christchurch-specific service context |
| 19 | [Kelleher Real Estate](https://kelleher.co.nz/) | Concise Selling, Buying, About & Contact | Independent-boutique clarity without enormous menus |
| 20 | [Vivacity Christchurch](https://www.vivacity.nz/) | Focused Christchurch Central market positioning and Sell/Buy paths | Strong genuine geographic specificity beats boilerplate suburb spam |

**Shared lessons:** seller pathways, trustworthy personal identity, an appraisal CTA, helpful guides, local context and functional contact are valuable **before** property inventory. Do not reproduce competitor copy/branding or their portfolio-dependent navigation.

## 3. Information architecture

Primary header:
- **Home**
- **Sell** (overview, Property Appraisal, Selling a House, Selling Costs, Methods of Sale, Preparing for Sale)
- **Buy** (overview, First-Home Buyer Guide, Buying Process)
- **Areas** (Christchurch, Canterbury, later only original and verified sub-areas)
- **About** (approach, Corrie profile)
- **Guides**
- **Contact**
- Persistent gold CTA: **Request an Appraisal**. On mobile provide visible menu and CTA, accessible keyboard operation.

The homepage should remain premium, with the supplied photograph shown entirely on desktop and mobile. Unlike the holding page, support natural scrolling for substantive sections: concise search-intent-led hero, sell/buy choices, appraisal value proposition, approach/Corrie credibility, regional coverage, 3–5 helpful FAQs, latest verified guides and contact CTA. Do not force a one-screen layout when content grows.

Page/keyword map (proposed; final wording and overlapping keyword intents to be validated before drafting):

| Route | Primary user intent | Priority |
|---|---|---|
| `/` | Brand plus real-estate-agent service entry; Christchurch launch context | P0 |
| `/sell/` | Sell my house / selling property in Christchurch and NZ | P0 |
| `/sell/property-appraisal/` | Request property appraisal Christchurch | P0 |
| `/about/` | Who is Piripi & Sons; approach and licence attribution | P0 |
| `/about/corrie-piripi/` | Who is Corrie; verified skills and role | P0 |
| `/areas/christchurch/` | What Corrie offers in Christchurch, accurate local details | P0 |
| `/contact/` | Send enquiry / call / email | P0 (existing route to improve) |
| `/buy/` | Home buyer guidance and enquiry (no property results) | P1 |
| `/real-estate-agents/` | Educational: choosing/working with NZ real estate professionals | P1 |
| `/sell/selling-your-house/` | NZ seller process and timeline | P1 |
| `/sell/costs-of-selling/` | Costs and commission explained, no invented fees | P1 |
| `/sell/methods-of-sale/` | Auction vs deadline vs negotiation/tender | P1 |
| `/sell/preparing-for-sale/` | Preparation checklist | P1 |
| `/areas/canterbury/` | Verified service areas and regional context | P1 |
| `/buy/first-home-buyers/` | First-home buyers NZ informational guide | P2 |
| `/buy/buying-process/` | Step-by-step offer, due diligence and settlement guide | P2 |
| `/guides/` | Articles index with real content, never empty placeholder | P2 |

Keep `/sitemap/` as quiet footer utility; regenerate `/sitemap.xml` with **only live indexable URLs**. Publish initial group first and add remaining pages only when their original copy is accurate and complete. A single SEO head term on every page is counterproductive: assign distinct search intent and avoid cannibalisation between homepage, national educational hub and local Christchurch page.

Suggested original guide backlog (editorial, not automatically publishable):
1. How do I choose a real estate agent in New Zealand?
2. What happens during a property appraisal?
3. What does it cost to sell a house in NZ?
4. Auction vs deadline sale vs negotiation.
5. Preparing your Christchurch home for sale.
6. Questions to ask before signing an agency agreement.
7. First-home buyer due diligence in NZ.
8. A dated Canterbury market update, only with attributed and licensed/permitted data.

Each guide must add original, genuinely useful analysis, current NZ guidance, references and an appropriate review date. Corrie should fact-check industry-specific advice and first-person claims. No scraping/rephrasing competitors into low-value filler.

## 4. Work packages and acceptance criteria

### PP-SEO-01 — Baseline audit and compliance gate (P0, blocking public expansion)
- Capture current Search Console index status (access-dependent), site crawl, PageSpeed/Core Web Vitals, lighthouse/accessibility baselines, redirect/canonical behaviour, GTM/GA4 event state and direct-enquiry status.
- Verify the exact REA licence type held by Corrie, supervising licensed agency, authorised trading presentation, name/legal details and required licence statements. **Do not present a salesperson as a "licensed real estate agent".** The current `/contact/` contains that phrase and the hidden homepage H1 also says "licensed real estate agent". Replace only when the accurate classification is verified.
- Verify owned brand artwork/image rights and the website-facing privacy notice.
**Done when:** documented audit plus compliance-approved public wording; no unsupported business-entity schema or office address.

### PP-SEO-02 — Static site build system and navigation (P0)
- Preserve `public/` output and existing deployment workflow; introduce simple shared header/footer/nav/SEO metadata generation to avoid page divergence.
- Add accessible responsive desktop/mobile navigation, current-page state, keyboard focus, sensible breadcrumbs and a repeated appraisal action.
- Use a content manifest with page URL, title, description, image, H1, category and indexability; generate navigation and both sitemaps from it.
**Done when:** menu reaches all public pages without broken links; only complete live routes in sitemap; header active state and mobile navigation tested at 320/375/768/1280px.

### PP-SEO-03 — High-intent pages (P0)
- Build complete, original `/sell/`, `/sell/property-appraisal/`, `/areas/christchurch/`, `/about/` and Corrie profile; update home and contact.
- Each page has a unique intent, helpful copy, one canonical H1, clear CTA and contextual internal links.
- Appraisal form asks for property location, contact details, enquiry details and consent wording; **does not** claim to estimate price automatically.
**Done when:** no empty page or unsupported claim; seller can reach and submit an appraisal enquiry from 3 navigation paths.

### PP-SEO-04 — Enquiry reliability and abuse protection (P0)
- Existing browser client and Cloudflare Pages Function already implement API-backed Brevo transactional delivery **if** required secrets are configured. JS switches to `mailto:` when GET readiness probe reports unavailable. Do not rebuild blindly.
- Verify production `BREVO_API_KEY` secret, `ENQUIRY_TO_EMAIL` recipient configuration, sender authorisation and actual successful end-to-end delivery; no public/private Gmail or secret leaks.
- Preserve existing required-field validation, honeypot and minimum form completion checks; implement server-side Turnstile verification and sensible rate limits before paid traffic; avoid overlogging personal data.
- Correctly distinguish accepted provider receipt from actual recipient delivery in operations checks.
**Done when:** real test inquiry lands in agreed inbox; success UI only after API acknowledgement; failure/fallback works; repeat/spam tests and abuse controls pass.

### PP-SEO-05 — Core technical SEO (P0)
- Unique readable titles, descriptions and canonical URLs; semantically correct H1/H2s; open-graph previews; appropriate image sizes, lazy loading except hero and stable URL design.
- Regenerate `robots.txt`, `sitemap.xml`, human sitemap; add safe JSON-LD WebSite/WebPage/Person and accurate BreadcrumbList as appropriate. RealEstateAgent/LocalBusiness only after verified agency/entity/physical/service-area details.
- Include noindex for truly non-public or duplicate material only; avoid unsubstantiated schema FAQ rich-result expectations.
**Done when:** automated sitemap/metadata/link/schema checks pass; no orphan P0 pages; Search Console inspection after launch confirms Google can fetch priority pages (indexing not guaranteed).

### PP-SEO-06 — Measurement and reporting (P0)
- Audit GTM ID `GTM-555PWRPR`, GA4 events and consent requirements; do not assume existing tag means conversions work.
- Instrument `appraisal_form_success`, `general_enquiry_success`, `phone_click`, `email_click` and primary CTA click; deduplicate and never leak message, phone, email or address as event parameters.
- Capture baseline impressions, clicks, indexed pages, organic landings and measured enquiries; report monthly changes, noting small-sample uncertainty.
**Done when:** verified test events appear in real-time/debug tooling; real success event only follows API acknowledgement.

### PP-SEO-07 — Content cluster build (P1/P2)
- Create remaining selling guides and education-led buyer pages; publish Canterbury only once area claims and original content are verified.
- Establish internal link rules: each guide points to its parent pillar, relevant sibling and natural seller/appraisal CTA; parent pages list useful children.
- No mass-generated suburbs, no scraped third-party photos or unlicensed market statistics, no obsolete market dates. Publish only pages that genuinely differ in intent and locally substantiated utility.
**Done when:** each route is editorially complete, reviewed, original, mobile-readable and has a clear next step.

### PP-SEO-08 — QA, security and staged production rollout (P0)
- Build preview deployment or equivalent pre-prod validation before applying live changes. Existing site is a separate Direct Upload Cloudflare Pages project; keep Wrangler workflow and project isolation.
- Test small devices and very short heights; accessible labels, focus traps/escape, contrast, text zoom, image cropping, no horizontal overflow, no clipped form controls.
- Run automated smoke and link checks, pre/post-deploy curl checks, and form submission tests. Do not publish a false list of achievements or placeholder testimonials.
**Done when:** production pages pass smoke and manual responsive checks, existing branding preserved and rollback path documented.

## 5. Delivery order and dependencies

**Release 0: unblock and measure.** PP-SEO-01, email/function readiness checks, compliance sign-off; collect baseline and screenshot samples. No claims about client licence, supervising agency or service coverage without verification.

**Release 1: high-value acquisition site.** PP-SEO-02/03/04/05/06; launch high-intent core navigation and seller/appraisal pages, profile, Christchurch and contact. Do not ship unreviewed placeholder content.

**Release 2: organic authority.** PP-SEO-07 plus P1 pages, then carefully selected P2 guides; verify content, citations and area accuracy; resubmit sitemap and inspect index coverage.

**Ongoing optimisation.** Use Search Console query data and genuine enquiry outcomes to prioritise improvements; test CTA placement, readability, mobile performance and relevant internal links, not vanity page counts.

### Release-level success measures
- All P0 pages are present, indexable and crawlable; no listings navigation without inventory.
- Clear seller journey: homepage → seller information → appraisal request → **verified** inbox receipt.
- No false licence/title or entity claim and no unverified office/address coverage.
- GA4 conversion actions are tested and Search Console is configured for relevant URLs.
- Zero dead internal links, no duplicate canonical routes, usable mobile navigation and accessible forms.
- Technical changes remain independent of GRID EATER's unrelated deployment systems.

## 6. Authoritative implementation references
- Current source: https://github.com/meeeeeooooowwwwwww/piripiproperty.com
- REA advertising/licence rules: https://www.rea.govt.nz/real-estate-professionals/obligations/marketing-as-an-individual-or-company/
- Google's SEO Starter Guide: https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- Google's helpful-content guidance: https://developers.google.com/search/docs/fundamentals/creating-helpful-content

**Scope-control rule:** this engineering plan is an internal development roadmap. Do not overwrite the 13 November client SOW, create an invoice, change commercial terms, contact Corrie or start paid advertising as part of adopting it.

## 7. Deep technical SEO architecture: required baseline (research update, 17 Nov 2026)

**Decision:** Treat the production site as a small, high-trust **static-first publishing system**, with a separately verified transaction endpoint for enquiries. A site architecture is modern because it is maintainable, robust, accessible, measurable and crawler-friendly, not because it installs a new frontend framework.

### 7.1 Versioned content and URL contract
Create a validated source-of-truth manifest/content collection with:
- `route`, `contentType`, `intentCluster`, `pageTitle`, `metaDescription`, `h1`, `canonical`, `language=en-NZ`, `publicationStatus`, `indexable`, `sitemap`, `lastSubstantialChange`, `ogImage`, `author`, `reviewer`, `lastReviewed`, `sourceRefs`, `claimsApproved`, `parentRoute`, `crossLinks`, `geoScope`, `serviceStatus`, `ctaKind`.
- Support explicit `draft | review | approved | published | retired` publication states; only approved/published may produce production HTML, sitemap or internal discovery links. Drafts should not be public behind a mere robots exclusion; keep them unpublished or access-controlled.
- Reusable build-time components generate consistent header/footer, accessible navigation, breadcrumbs, article citations, title/description, OG metadata, JSON-LD, XML and human sitemaps.
- Fail the build if duplicate canonical/title/intent targets, empty descriptions, broken references, fake/inconsistent entity facts, unapproved pages or mismatched canonical-sitemap links.
- Use clean permanent URLs; maintain 301 redirects for renamed/deleted routes, no redirect chains or soft-404s. Canonical production origin is `https://piripiproperty.com` (no www). Audit HTTP/www/`pages.dev` alternate behaviour separately. A canonical link alone does **not** eliminate all duplicated domains.
- Include only canonical indexable HTTP 200 pages in `sitemap.xml`. Set XML `lastmod` only for real content/structured-data/link changes, not every build or footer date. Do not bother with ignored sitemap `priority`/`changefreq`.
- Use native HTML links (`<a href>`) and essential full copy rendered in deploy-time HTML. JS enhances interactions, not content discovery. Mobile version exposes the same important content and links; do not gate menus behind broken JS.

### 7.2 Semantic entity and structured data design
- Single consistent identity graph IDs for `WebSite`, approved `Brand`, verified `Person`, and each `WebPage`/appropriate article; cite/source public factual claims. Use article byline, accurate review/modified date, editorial context and verifiable professional licence as available.
- Add `BreadcrumbList` for hierarchical pages that show navigable breadcrumbs. Use `Article` for substantively authored guides. Make JSON-LD match publicly visible facts; validate JSON schema and Rich Results Test where Google supports the type. Rich-result display is never promised.
- `RealEstateAgent`/`LocalBusiness`/organisation business address/phone/service area/profile/entity markup only after legal agency status, public display rules, genuine location and operation are checked. Never invent offices, licence class, accolades, sales, reviews, star ratings or achievements.
- Provide useful on-page FAQs for readers, but do not promise a FAQ rich result: Google discontinued FAQ rich-result support in 2026. Avoid unnecessary schema.
- Do **not** implement `hreflang` simply because some leads are based overseas. `en-NZ` HTML and NZ-focused content are appropriate for a single English website. Add `hreflang` only when genuine alternate-language/locale URL versions exist.
- No requirement for `llms.txt`, "AI-specific schema", mass AI summaries, keyword-density targets, fabricated author identities or arbitrary minimum word counts. Google's 2026 AI search guidance explicitly prioritises existing Search Essentials and original non-commodity content.

### 7.3 Performance, cache, images and accessibility
- Target the 75th percentile of *field* experience: **LCP ≤2.5s, INP ≤200ms, CLS ≤0.1** (mobile primary, desktop also tested). Lab budgets are diagnostic, not field data substitutes. Track median and p75 only when sample size adequate; display insufficient-data state honestly.
- Optimise responsive hero and article images using modern formats (AVIF/WebP with safe fallbacks if supported), `srcset`/`sizes`, explicit dimensions/aspect ratio, appropriate fetch priority for only the hero, deferred offscreen images, compression, minimal request chains. Preserve Corrie's supplied five-person artwork and all faces/branding; never crop as a performance hack.
- HTML should be cache-correct and deployable atomically; fingerprint CSS/JS/images and use long immutable asset caching, with HTML revalidation/short-cache policy. Current global `Cache-Control: no-cache` is good for active development but not the final optimised asset policy. Changing caching must include preview and rollback tests.
- Keep JS small: accessible menus, forms, consent and optional progressive enhancements only. Self-host/subset fonts or use performant fallbacks where practical; avoid heavy carousels, autoplay overlays, third-party scripts and intrusive pop-ups.
- Accessibility acceptance **WCAG 2.2 AA**: keyboard menu, visible focus, skip-to-main, logical landmarks/H headings, readable 200% text zoom, comfortable touch target sizes, contrast, descriptive form errors/status, reduced-motion settings, accessible consent and mobile viewport fit. Test 320, 375, 768, 1280 px plus narrow-height viewports; no clipped contact form.
- Use responsive *content parity*, not just responsive styling; Google indexes primarily the mobile experience.

### 7.4 Cloudflare and security engineering
- Keep original `piripiproperty` Pages project, `public/` output, `wrangler.toml` and existing Wrangler GitHub workflow; no second Git integration or deployment into GRID EATER.
- Audit all `public/_headers` policies, including CSP, X-Content-Type-Options, Referrer-Policy, clickjacking protections and safe font/analytics origins. **Cloudflare `_headers` rules do not apply to Pages Functions responses.** Attach suitable security and `Cache-Control: no-store` directly to API responses.
- Set `X-Robots-Tag: noindex` on actual `*.pages.dev` preview hosts where appropriate; prefer access control for confidential drafts, not robots as a security mechanism. Verify headers on response, not only repo source. Never block the main production host.
- GET readiness of the enquiry endpoint is **not** a delivered lead: confirm secret presence, server Brevo acceptance, provider log, verified inbox receipt and fallback on failure. Validate CORS/origin, body bounds, abuse controls and Turnstile server-side. Keep secrets server-only; no form values logged into public analytics, URLs or exception traces.
- Retain the existing CI tests but remove **brittle exact CSS/HTML string assertions** before switching to shared templates; replace with semantic assertions and screenshot regression coverage. Existing CI currently hard-codes homepage markup, CSS values, date-tagged assets and the original navigation: changing navigation without updating these tests will fail deployment.

### 7.5 Release pipeline and measurable checks
For every PR/build:
1. Lint and typecheck generator/content schema; validate all publication-state and factual-claim gates.
2. Generate the entire static site; smoke-test final generated output, not only source.
3. Crawl generated pages; flag broken internal links, redirects, errors, non-200 canonical URLs, orphan pages, duplicate titles/H1s, inconsistent canonical/OG/JSON-LD, missing article source/author metadata, unexpected `noindex` or sitemap pages.
4. Accessibility automation (axe or equivalent) plus manual keyboard/mobile visual checks. Run Lighthouse CI mobile and desktop, record deltas; initially warn on targets and fail serious regressions once a measured baseline is established.
5. Unit-test Pages Function including bad input, honeypot, rate limit, Turnstile failure, upstream timeout, acknowledgement and email fallback. Never send real emails from routine CI.
6. Preview with proper noindex/access, compare screenshots of branding and faces; approval gate for commercial/licence claims; deploy by existing Wrangler route, then production HTTP/canonical/schema/sitemap/analytics checks.
7. Keep rollback instructions and prior artifact reference. Enable routine Search Console coverage, CWV and GA4 conversion health review; do not assert immediate or guaranteed indexing.

## 8. NZ geographic growth model: design nationwide, publish only verified claims

**Working hypothesis supplied 17 Nov:** Corrie is based in Christchurch and may consider travelling nationwide for sufficiently valuable engagements, especially where an owner/client is offshore. This is **unconfirmed**. Do not publicly market nationwide travel or high-end specialism as an established offering.

Separate three concepts in content data and UX:
1. **Base location:** Christchurch (subject to verified public office/agency location rules).
2. **Normal service area:** only areas Corrie/agency explicitly accepts and is able to service; Canterbury is the initial planning focus, not a compliance-verified public statement.
3. **Discretionary assignments:** potential nationwide work requiring prequalification, project suitability, supervising-agency authority, professional oversight, travel and resource availability and written agreement. **No auto-acceptance**, no automatic mileage or price cutoff.

Define statuses `verified_local`, `conditionally_available`, `unconfirmed` and `unsupported` in internal data. Publication rules should allow service promises only after verification. A conditional national possibility does **not** justify dozens of city SEO landing pages, GBP offices or local-business schemas.

**Future route (do not publish until approved):** `/services/specialist-property-enquiries/` or `/services/nationwide-property-consultation/`; strong intent-specific explanation of fit and a private qualification form, *not* a "real estate agent in Wellington/Auckland" doorway page.

Build a reusable geographic taxonomy (country → region → city → actual serviced subareas) now, but only create indexable location pages containing original and genuinely relevant local expertise. Each page should have distinct data and a useful user path; never copy a Christchurch page and replace the place name.

**Google Business Profile:** reflect the real eligible office/practitioner and permitted service area only; no fictitious offices, addresses, nationwide listing spam or virtual addresses. One coherent local profile and verified name/address/contact is preferable to location duplication.

## 9. High-value and overseas lead architecture

Different intents (keep separate so we do not conflate seller, investor or buyer rules):
- **NZ residents/owners selling locally:** primary appraisal journey.
- **People based abroad who own NZ property:** potentially strong content opportunity, e.g. `/guides/selling-new-zealand-property-from-overseas/`, with practical owner-to-agent communication, time zones, agency agreements, legal adviser and identity verification signposts, only after factual review.
- **Potential premium/specialist vendors anywhere in NZ:** conditional consultation gate, not an unconditional travel promise.
- **Prospective overseas purchasers/investors:** legally sensitive eligibility and property acquisition information. **Not** an open nationwide foreign-buyer promise, and not the primary launch lead funnel.

**Important 2026 legal change:** On 6 March 2026 overseas-investment reforms took effect. Certain holders of Active Investor Plus/Investor 1/Investor 2 visas may apply for consent for residential property worth more than **NZ$5 million** (subject to the specific pathway/conditions); broader foreign-buyer restrictions remain. This is a specialist **editorial/partnership research topic**, not a general sales-service eligibility claim. Refer enquiries to qualified NZ legal/immigration advice and current LINZ guidance. Never present the exception as permission for all wealthy offshore buyers.

**Candidate high-value enquiry schema (future, privacy reviewed):**
- relationship: `seller/owner`, `buyer`, `authorised representative`, `general advice`;
- property city/region (not compulsory exact street address at first contact); property category (residential, lifestyle, commercial etc **only if service is actually authorised**);
- broad *optional* value band (including "prefer not to say") and estimated timing, time zone/country and preferred contact method;
- short description, contact details, acknowledgement of purpose/privacy notice;
- for out-of-area enquiry: opt-in to a preliminary remote consultation and conditional suitability assessment.

Avoid collection of passports, IDs, title deeds, visa numbers, AML documents or sensitive financial proof via a casual web form. Separate regulated identity/eligibility checks into secure approved workflow when there is a legitimate engagement. Do not automatically reject low-value enquiries based on an invented threshold; ask Corrie to agree objective criteria and the process.

**Qualification rule before travel (internal draft, not client policy):** ownership/authority and purpose clarified → approximate value/complexity and commercial viability assessed → remote conversation → correct supervising agency approval and specialist/legal support assessed → only then consider travel and fees. Keep actual thresholds blank pending confirmation.

## 10. Privacy, trust, business legitimacy and accountability

- Verify REA public register licence class and licensed supervising agency/entity before going beyond the preliminary holding page. REA distinguishes a **licensed salesperson** from a **licensed agent**; a salesperson must not advertise themselves as a "licensed real estate agent". Current site uses that phrase in the contact page and hidden H1; correct in its own compliance-gated change.
- Section 121 REAA requires the relevant licensed agent, "licensed under the Real Estate Agents Act 2008" and any different trading name on the business website/advertising as applicable. Obtain agency legal review rather than inventing a licence class or company registration.
- Do not market an actual property without the required client authorisation/agency agreement; never fabricate sold-property evidence or endorsements. Use approval workflow for property photos and customer testimonials once those are available.
- Lead collection notice: purpose, recipient(s), use, retention, contact/privacy rights, nature of third-party providers and any overseas disclosures; separate permission for marketing subscriptions. Review NZ Privacy Act Principle 3 and Principle 12 for overseas processors/disclosures. Use transport security, limited access, sensible retention/deletion and breach response.
- **Google Analytics must not receive names, email addresses, phones, property street addresses, exact enquiry text, IDs or URL parameters containing personal information.** Design event schema accordingly. Use analytics consent/notice appropriate to provider and user jurisdictions, with a clean mode for later Google Ads; track provider-acknowledged form success and actual delivery outcomes separately.
- Source property law, tax, buying restrictions and sale-process explanations to REA, LINZ, IRD and specialist advisers as appropriate; article author/reviewer, published/updated dates, claim/source audit record and periodic review. Do not "freshen" a date without substantial content revision.
- Trust-building must be genuine: no fake offices, fake sales count, fictional years in business, unsourced price predictions, unverified qualifications or generalised "NZ's leading" claims.

## 11. Decision register / proof before adoption

| ID | Decision | Default / verification requirement |
|---|---|---|
| ARC-01 | Static generation | Prototype small typed source-of-truth generator **vs Astro SSG content collections**. Choose the simplest with reproducible output, CI, metadata and rollout parity. Existing Pages remains unchanged until tests pass. |
| ARC-02 | Content management | Source-controlled content/Markdown and reviewed source references first; no CMS/database by default. |
| ARC-03 | Internationalisation | One `en-NZ` canonical English site; no unnecessary translated clones or `hreflang` until real versions exist. |
| ARC-04 | Taxonomy | National region/city schema can exist internally but public location pages require unique approved service-area evidence and user value. |
| ARC-05 | High-value | A premium/nationwide consultation workflow is a gated hypothesis; no service-level promise or numerical value threshold until Corrie approves it. |
| ARC-06 | Offshore | Distinguish offshore NZ owners selling from regulated overseas buyers. Legal review and source citations before any foreign-investment landing page. |
| ARC-07 | Maps/GBP | Only verified eligible real-world locations and authorised coverage; no multiple fictitious Google profiles. |
| ARC-08 | Technical baseline | Collect field/lab measurements, accessibility audit, Search Console indexing and real lead readiness **before** announcing SEO readiness. |
| ARC-09 | SEO controls | Standard page types; auto-build sitemap and canonical graph, error budgets and monitoring; zero guaranteed rankings. |
| ARC-10 | Deployment | Existing Direct Upload Pages + Wrangler is authoritative; no unrelated project migration or surprise API/hosting bill. |

## 12. Research register — high-authority current sources (checked 17 Nov 2026)

Google Search Essentials and AI Search (2026):
- https://developers.google.com/search/docs/essentials
- https://developers.google.com/search/docs/fundamentals/seo-starter-guide
- https://developers.google.com/search/docs/fundamentals/ai-optimization-guide
- https://developers.google.com/search/blog/2026/05/a-new-resource-for-optimizing
- https://developers.google.com/search/docs/fundamentals/creating-helpful-content
- https://developers.google.com/search/docs/essentials/spam-policies
- https://developers.google.com/search/docs/crawling-indexing/mobile/mobile-sites-mobile-first-indexing
- https://developers.google.com/search/docs/crawling-indexing/consolidate-duplicate-urls
- https://developers.google.com/search/docs/crawling-indexing/sitemaps/build-sitemap
- https://developers.google.com/search/docs/appearance/structured-data/breadcrumb
- https://developers.google.com/search/docs/appearance/structured-data/local-business
- https://developers.google.com/search/docs/specialty/international/managing-multi-regional-sites/
- https://developers.google.com/search/docs/appearance/core-web-vitals
- https://developers.google.com/analytics/devguides/collection/protocol/ga4/policy

Infrastructure / accessibility:
- https://developers.cloudflare.com/pages/configuration/headers/
- https://developers.cloudflare.com/pages/configuration/redirects/
- https://docs.astro.build/en/guides/content-collections/
- https://www.w3.org/TR/wcag/
- https://support.google.com/business/answer/3038177

New Zealand:
- https://www.rea.govt.nz/real-estate-professionals/obligations/marketing-as-an-individual-or-company/
- https://www.rea.govt.nz/buyers-and-sellers/find-an-agent/
- https://www.rea.govt.nz/real-estate-professionals/industry-guidance-and-information/listing-a-property/agency-agreements/
- https://www.linz.govt.nz/news/2026-03/overseas-investment-act-has-changed
- https://www.linz.govt.nz/guidance/overseas-investment/ways-invest/pathways-migrants-and-visa-holders/investing-residential-land-over-5-million
- https://www.linz.govt.nz/guidance/overseas-investment/buying-residential-property-live
- https://www.privacy.org.nz/privacy-principles/3/
- https://www.privacy.org.nz/privacy-principles/12/

**Change management:** This v2 document is internal-only; it does not mean the commercial proposal was amended, the client's approvals were secured, or the production site was modified. The next engineering deliverable is a reversible static-generation and site-crawl quality-gate proof of concept; public publication of claims stays behind the verification gates above.

## 13. Approved internal international-investor direction — 17 November 2026

**Owner decision:** International and overseas-investor positioning is a desired part of the long-term Piripi & Sons strategy. Introduce a **small, factual international section now**, but **do not** elevate it to primary navigation, promise investor services, nationwide travel, luxury sales expertise, visas, investment returns, acquisition eligibility, or an accepted high-value client programme until Corrie's direct confirmation and the appropriate legal/agency review.

### Phase A — discreet launch
- Publish `/international/` as an informative **New Zealand property enquiries from overseas** landing page; link it quietly from the footer and human/XML sitemaps. Existing Home/Contact header and supplied artwork are unchanged.
- The page explicitly addresses **overseas investors and prospective buyers**, plus **existing NZ property owners living abroad**. It references the NZ overseas-buying restrictions and conditional, consent-required 2026 investor-visa pathway, and links directly to current LINZ sources.
- State only that a preliminary enquiry can be made. Do not claim Corrie personally qualifies investors, provides legal/financial/immigration advice, arranges travel, has national agency offices or can accept every overseas buyer. Out-of-area availability is **not assured**.
- Direct to existing general website enquiry/contact pathways, without collecting passports, visa numbers, funds evidence or detailed personal finance.
- Use real content, unique metadata, canonical URL, consistent non-fabricated Person/Brand/WebPage JSON-LD, mobile-readable design and a crawlable internal path.
- Check current site's exact licence claims and supervising-agency disclosures separately; the international addition does not authorise an incorrect role statement elsewhere.

### Phase B — client discovery and commercial qualification (not approved for public promise)
Discuss with Corrie:
1. His licensed role, supervising agency, and authorisation to act for overseas buyers, NZ owners abroad, specific property classes, and out-of-region transactions.
2. Whether he wants to work with non-resident owners selling in NZ, eligible investor-visa purchasers, or both; referral support and relevant specialist counsel.
3. What property types, indicative value/commission bands, location, seller or buyer authority, commercial fit and workload justify a nationwide engagement, and who covers travel.
4. Whether a remote introductory conversation can screen leads before travel; whether separate private legal/AML documentation handoff is needed; preferred international contact process and time zones.
5. What independently verifiable experience and professional partners can be shown publicly, with permission.

### Phase C — after confirmation
- Upgrade navigation from footer-only to a clearly labelled **International** or **Overseas Investors** main entry only when service scope is confirmed; avoid pretending to operate multiple NZ branches.
- Expand `/international/` into distinct pages for (a) overseas owners selling in NZ, (b) eligible overseas investor purchasing pathways, (c) conditional nationwide/premium-property consultation, each with properly reviewed, substantively distinct information.
- Add a privacy-reviewed qualified lead form with **optional** property region/type/value band, relationship, time zone and remote consultation request; no hard-coded eligibility verdict or invented value cutoff. Maintain clear signposting to current LINZ and lawyer advice.
- Add reputable original articles with dated references; review legal details at least each material policy change. No automated generic city pages or fabricated sales history.
- Future analytics: aggregate traffic and conversions for the international hub, without personal data in GA4. Do not count enquiries as accepted clients.

**Release gate:** Phase A is approved as a restrained informational/SEO seed. Promotion or claims of an established premium or national/investor service remain pending Corrie's consultation, licence and agency verification.

## 15. Corrie Piripi professional profile research — 17 Nov 2026

**New user direction:** Create a professional, slightly personal biographical portfolio based on his linked public profile, not a gallery of property listings. A generated SEO page `/about/corrie-piripi/` now takes historical property leadership and community service as its evidence-led themes. Subject to final client approval, small italic `*` footnotes lead to each public source.

**Independent background evidence:**
- Real Estate Business (25 Jan 2016): names Corrie Piripi chief executive of Just Property Management in Bunbury and discusses assistance to Yarloop bushfire-affected families. https://www.realestatebusiness.com.au/industry/15165-agency-uses-rent-roll-to-aid-bushfire-victims
- Real Estate Business / Coronis (17 May 2022): reports he started his own Coronis franchise business in 2021 and quotes him on real-estate sales, investment properties and property-management relationships. This is an attributed vendor-contributed article, not independent verification of all claims. https://www.realestatebusiness.com.au/sales/23478-our-sales-franchises-are-gaining-multiple-income-streams-and-building-a-salable-asset-are-you
- REIWA historical records associate him with Western Australian property sales for Coronis; do not reproduce old property listings in the new branded website without permission. https://reiwa.com.au/99-manning-road-bentley-4768395/
- His public LinkedIn self-reports a 2017 Australian Diploma in Property Services, previous Australian real-estate registration, youth-work education, cultural/community mentoring and leadership roles. These must be reconfirmed before asserting active licensing, current roles or achievements. https://au.linkedin.com/in/corrie-piripi-84a23124
- NZ REA public register and supervising agency confirmation remain required: https://www.rea.govt.nz/buyers-and-sellers/find-an-agent/

**Portrait status:** The requested 200×200 LinkedIn thumbnail URL could not be securely downloaded as a reliable source. An AI studio-style concept is not proof of likeness and must not be presented as a real portrait. Obtain a local original photograph or confirmed permission and appropriate photo-quality input before deploying an edited image; use professional lighting and neutral charcoal/gold background consistent with the brand without changing facial identity.

**Client checklist:** Updated the internal Google Drive question document with additional biography and photo-approval checks. Historical public evidence does not substitute for Corrie's approval to present personal family, cultural or community background.

## 16. Release and evidence checkpoint — 17 November 2026

- PR #2 merged `c3296386592f6e89462e0bf7bb9955b3fe1aa75d`: static SEO generator, 12 new source-controlled routes, canonical sitemap build, internal-link/JSON-LD validation, homepage sections, responsive navigation, privacy page and server API security headers. Subsequent PR #4 merged `d79ab9b59b14bf392bb758f120b668c9317bc02b`: Corrie's source-backed About profile and human sitemap.
- The PR #3 premerge workflow **passed**: https://github.com/meeeeeooooowwwwwww/piripiproperty.com/actions/runs/44059113352 . The PR #4 workflow also **passed**: https://github.com/meeeeeooooowwwwwww/piripiproperty.com/actions/runs/44060101205 . Those pull-request runs intentionally **skip Cloudflare deployment**. A push-to-main deployment is separately triggered by the existing GitHub Actions workflow and should not be described as verified without a main-run outcome and live HTTP readback.
- Corrie's internal checklist and evidence record is located in his existing Google Drive client folder: https://docs.google.com/document/d/1ZVdxkdj46sSiiEUPfhsIwLotP0E2WoSTS-59FWO8Rvk/edit . Original checklist and six extra biography/photo questions are included. The document is internal and should not be sent as a client-approved representation of answers.
- Publication pending evidence: precise NZ REA licence and supervising agency disclosure, domain/brand authorisation, relevant approved services, international availability, actual Brevo inbox delivery, consent/privacy policy, and a high-quality genuine portrait image with permission.

## 17. Design, source-backed biography, portrait and licence-status update — 17 Nov 2026

User approved the interim AI-assisted studio portrait derived from Corrie's supplied 200px LinkedIn photograph. Optimised 900px wide WebP asset stored at public/assets/corrie-piripi-professional.webp (approx. 44 KB) and Corrie's Google Drive folder. This is a retouched, upscaled image, not original high-resolution photography. Use it until Corrie supplies a better original; user has authorised this interim choice.

**New licence information:** Corrie told the site owner he transferred his Australian real estate licence to New Zealand. The NZ REA confirms a Trans-Tasman Mutual Recognition process exists for equivalent licences. However, his exact current NZ class (salesperson, branch manager or agent), conditions and supervising agency remain unverified. Official guidance: https://www.rea.govt.nz/real-estate-professionals/apply-for-your-licence/if-you-have-an-australian-licence-or-registration/ . REA register: https://www.rea.govt.nz/buyers-and-sellers/find-an-agent/ . The website must not identify him as a licensed agent without evidence of an NZ agent-class licence; obtain licensed-agency details before final regulatory sign-off.

**Development changes:** professional split-portrait biography pages, sourced career milestones, better editorial chapter and section hierarchy, stronger homepage Meet Corrie feature, responsive single-main layout, accessible icon-only navigation without a visible Menu word, About breadcrumbs, updated Person structured data image, tiny italic source references and stronger CI checks for navigation and image resources. Preserve original team photo, home enquiry form, canonical domain, Cloudflare Pages Direct Upload, and international section.

**Evidence highlights:** Just Property Management chief executive and Yarloop fire response reported in January 2016 (https://www.realestatebusiness.com.au/industry/15165-agency-uses-rent-roll-to-aid-bushfire-victims); Coronis franchise interview May 2022 (https://www.realestatebusiness.com.au/sales/23478-our-sales-franchises-are-gaining-multiple-income-streams-and-building-a-salable-asset-are-you); Corrie's public LinkedIn self-reported youth mentoring, community roles, professional study (https://au.linkedin.com/in/corrie-piripi-84a23124). Keep historical roles historical and do not publish sensitive personal details.

**QA pending:** pull request CI with static generator, SEO validation and enquiry tests; main branch Cloudflare deploy and live URL readback; mobile and keyboard inspection; accurate licence and supervising agency disclosures; actual Brevo inbox delivery. The Corrie Drive checklist contains questions and evidence requirements.
