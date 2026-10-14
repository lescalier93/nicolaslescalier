---
layout: default
title: "3-Year Business Term Program | Canada & U.S."
description: "Explore a 36-month business term program at 12–16% APR. Minimum annual revenue: CAD $3M in Canada or USD $3M in the U.S. Apply online with Nicolas Lescalier."
permalink: /services/three-year-term-program/
breadcrumb_title: 3-year term program
term_program: true
---
{% assign program = site.data.term_program %}
<section class="hero">
  <div class="hero__grid">
    <div>
      <p class="eyebrow">Business financing · Canada &amp; United States</p>
      <h1>Three years. A clear starting point for your financing request.</h1>
      <p class="lede">A {{ program.term_months }}-month business term program at {{ program.apr_min }}–{{ program.apr_max }}% APR for businesses with at least {{ program.revenue_display }} in annual revenue. Amounts are CAD in Canada and USD in the U.S.</p>
      <div class="hero__actions"><a class="button" href="{{ program.application_path }}">Apply for this program</a><a class="button button--secondary" href="/contact/">Discuss your eligibility</a></div>
      <p class="hero-note">Fully online. Subject to underwriting and approval.</p>
    </div>
    <aside class="hero-card">
      <span class="hero-card__label">Program at a glance</span>
      <h2>{{ program.apr_min }}–{{ program.apr_max }}% APR</h2>
      <ul class="check-list"><li>Three-year ({{ program.term_months }}-month) term</li><li>Canada: CAD {{ program.revenue_display }}+ annual revenue</li><li>United States: USD {{ program.revenue_display }}+ annual revenue</li></ul>
      <p>APR is an annual percentage rate. It is not a monthly rate or a guarantee that every applicant will receive the lowest rate.</p>
    </aside>
  </div>
</section>

<section class="section guide-content" markdown="1">
## Eligibility and currency

The first eligibility check is your business's annual revenue. The threshold applies in the currency of the country where the borrowing business is based.

<div class="table-scroll" role="region" aria-label="Program eligibility by country" tabindex="0">
<table><thead><tr><th scope="col">Business location</th><th scope="col">Minimum annual revenue</th><th scope="col">Currency for program amounts</th></tr></thead><tbody>{% for market in program.markets %}<tr><th scope="row">{{ market.country }}</th><td>{{ market.currency }} {{ program.revenue_display }}</td><td>{{ market.currency }}</td></tr>{% endfor %}</tbody></table>
</div>

The {{ program.revenue_display }} threshold is **annual business revenue, not the amount you must borrow**. Meeting this threshold does not guarantee approval. The requested amount, business profile, repayment capacity, location, and underwriting still need review.

If your business operates in both countries, identify the entity applying, where it operates, and the currency of its revenues and existing obligations. [View the full Canada and U.S. service coverage](/where-i-operate/).

## What to prepare for the first review

- Business name, country, province or territory or state, and industry.
- Annual revenue, the reporting period it covers, and the currency.
- Requested financing amount, intended use of funds, and desired timing.
- A summary of existing financing obligations and anything unusual in recent cash flow.

Start with the [online application]({{ program.application_path }}), which selects this program for you. The [application checklist](/application-checklist/) explains the financial information commonly discussed during review. Share sensitive supporting documents through the appropriate secure process after the initial discussion.

## What the written offer needs to clarify

The published starting terms are a **{{ program.term_months }}-month term and {{ program.apr_min }}–{{ program.apr_max }}% APR**. Your written offer needs to confirm the approved amount, currency, rate, fees, cash received, total repayment, payment schedule, and any security or guarantee requirements. Review any early repayment conditions before accepting.

Loan amounts, payment frequency, collateral or guarantee requirements, and funding timelines are assessed for the request. They are not promised on this page. The term loan calculator elsewhere on this site is an educational model; it is not a quote for this program.

## Below the revenue threshold or comparing options?

This is one financing program. The same terms and eligibility rules do not apply automatically to other products. Explore the [Canadian financing guide](/services/canada-business-financing/) or the [U.S. term loan guide](/services/us-term-loans-approach/), or [contact me](/contact/) to discuss the business need before choosing a product.
</section>

<section class="section">
  <h2>Questions about the three-year term program</h2>
  <div class="faq-list">{% for item in program.faq %}<details class="faq-item"><summary>{{ item.question | escape }}</summary><p>{{ item.answer | escape }}</p></details>{% endfor %}</div>
</section>

<section class="section">
  <div class="cta-panel"><p class="eyebrow">Next step</p><h2>Discuss whether this program fits your business.</h2><p>I am Nicolas Lescalier, Funding Manager at Premium Merchant Funding. I work online with business owners across Canada and the United States to review financing requests and explain the next steps.</p><div class="cta-row"><a class="button" href="{{ program.application_path }}">Start your program application</a><a class="button button--secondary" href="/contact/">Ask a question</a></div></div>
  <p class="content-note">Program information reviewed {{ program.reviewed | date: '%B %-d, %Y' }} by <a href="/about-nicolas-lescalier-us/" rel="author">Nicolas Lescalier</a>. Availability, approval, and final terms depend on underwriting and the transaction.</p>
</section>
