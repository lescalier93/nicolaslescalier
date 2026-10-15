---
layout: default
title: "3-Year Business Term Program | Canada & U.S."
description: "Explore a 36-month business term program at 12–16% APR. Minimum annual revenue: $3M. Apply online with Nicolas Lescalier."
permalink: /services/three-year-term-program/
breadcrumb_title: 3-year term program
term_program: true
---
{% assign program = site.data.term_program %}
<section class="hero">
  <div class="hero__grid">
    <div>
      <p class="eyebrow">Business financing · Canada &amp; United States</p>
      <h1>Three-year business term program.</h1>
      <p class="lede">A {{ program.term_months }}-month business term program at {{ program.apr_min }}–{{ program.apr_max }}% APR for businesses with at least {{ program.revenue_display }} in annual revenue.</p>
      <div class="hero__actions"><a class="button" href="{{ program.application_path }}">Apply for this program</a><a class="button button--secondary" href="/contact/">Discuss your eligibility</a></div>
      <p class="hero-note">Fully online. Subject to underwriting and approval.</p>
    </div>
    <aside class="hero-card">
      <span class="hero-card__label">Program at a glance</span>
      <h2>{{ program.apr_min }}–{{ program.apr_max }}% APR</h2>
      <ul class="check-list"><li>Three-year ({{ program.term_months }}-month) term</li><li>{{ program.revenue_display }}+ annual revenue</li><li>Available in Canada and the United States</li></ul>
      <p>APR is an annual percentage rate. It is not a monthly rate or a guarantee that every applicant will receive the lowest rate.</p>
    </aside>
  </div>
</section>

<section class="section guide-content" markdown="1">
## Who this program is for

Businesses in Canada and the United States with at least {{ program.revenue_display }} in annual revenue. This is a **revenue threshold, not a minimum loan amount**. Approval and final terms depend on underwriting.

Need a different repayment structure? [Other term-loan options](/services/us-term-loans-approach/) offer rates starting at 9% APR, terms up to five years, and possible amortization up to fifteen years, depending on qualifications. Those terms are separate from this three-year program.

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

This is one financing program. The same terms and eligibility rules do not apply automatically to other products. Explore the [Canadian financing guide](/services/canada-business-financing/) or the [term loan guide](/services/us-term-loans-approach/), or [contact me](/contact/) to discuss the business need before choosing a product.
</section>

<section class="section">
  <h2>Questions about the three-year term program</h2>
  <div class="faq-list">{% for item in program.faq %}<details class="faq-item"><summary>{{ item.question | escape }}</summary><p>{{ item.answer | escape }}</p></details>{% endfor %}</div>
</section>

<section class="section">
  <div class="cta-panel"><p class="eyebrow">Next step</p><h2>Discuss whether this program fits your business.</h2><p>I am Nicolas Lescalier, Funding Manager at Premium Merchant Funding. I work online with business owners across Canada and the United States to review financing requests and explain the next steps.</p><div class="cta-row"><a class="button" href="{{ program.application_path }}">Start your program application</a><a class="button button--secondary" href="/contact/">Ask a question</a></div></div>
  <p class="content-note">Program information reviewed {{ program.reviewed | date: '%B %-d, %Y' }} by <a href="/about-nicolas-lescalier-us/" rel="author">Nicolas Lescalier</a>. Availability, approval, and final terms depend on underwriting and the transaction.</p>
</section>
