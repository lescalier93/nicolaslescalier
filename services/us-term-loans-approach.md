---
title: "Business Term Loans | Rates From 9% APR"
description: "Discuss term loans with Nicolas Lescalier: rates from 9% APR, terms up to 60 months, and amortization up to 15 years on qualifying Canada and U.S. requests."
layout: default
permalink: /services/us-term-loans-approach/
breadcrumb_title: Term loans
financing_key: term_loans
redirect_from:
  - /blog/term-loans-vs-mca.html
  - /us-term-loans-approach/
  - /us-term-loans-approach.html
  - /term-loans/
  - /term-loans.html
faq:
  - question: "Do all applicants receive 9% APR?"
    answer: "No. Term-loan rates can start at 9% APR. The offered rate and structure depend on qualifications, including credit profile, repayment capacity, and underwriting."
  - question: "Is a fifteen-year amortization a fifteen-year loan?"
    answer: "No. The loan term can be up to five years, while the payment schedule may use an amortization of up to fifteen years. A balance may remain due at maturity; the written offer must explain how it will be repaid."
  - question: "Does the $3 million revenue threshold apply to every term loan?"
    answer: "The published $3 million minimum annual revenue applies to the separate three-year program at 12–16% APR. Other term-loan options have their own eligibility criteria."
---
{% assign terms = site.data.financing_programs.term_loans %}
<section class="hero hero--simple">
  <p class="eyebrow">Canada &amp; United States</p>
  <h1>Business term loans.</h1>
  <p class="lede">Finance expansion, equipment, an acquisition, or refinancing with a repayment structure that fits your business.</p>
  <div class="hero__actions"><a class="button" href="/apply/?product_interest=Term%20loan">Discuss a term loan</a></div>
  <p class="hero-note">Reviewed directly with Nicolas Lescalier. Fully online.</p>
</section>

<section class="section program-feature">
  <h2>More room to structure repayment.</h2>
  <dl class="program-facts">
    <div><dt>Starting rate</dt><dd>{{ terms.apr_min }}% APR</dd></div>
    <div><dt>Loan term</dt><dd>Up to {{ terms.max_term_months }} months</dd></div>
    <div><dt>Possible amortization</dt><dd>Up to {{ terms.max_amortization_years }} years</dd></div>
  </dl>
  <p class="quiet-note">Rates and available terms depend on qualifications and underwriting. These are available starting and maximum terms, not a promise that every request qualifies for all three.</p>
</section>

<section class="section split">
  <div class="panel">
    <h2>Loan term and amortization are different.</h2>
    <p>The loan term is the time until the loan matures. Amortization is the schedule used to calculate repayment. A five-year term can have payments based on a longer amortization.</p>
    <p>That can leave a balance due at maturity. Review the final payment and how any remaining balance must be repaid before accepting an offer. The <a href="https://www.consumerfinance.gov/ask-cfpb/what-is-a-balloon-payment-when-is-one-allowed-en-104/">CFPB explains balloon payments</a>.</p>
  </div>
  <aside class="simple-aside">
    <h3>A separate three-year program</h3>
    <p>For businesses with $3 million or more in annual revenue: a 36-month program at 12–16% APR.</p>
    <a class="text-link" href="/services/three-year-term-program/">Review three-year program eligibility</a>
  </aside>
</section>

<section class="section">
  <h2>Start with the essentials.</h2>
  <p>Share your business location, requested amount, use of funds, annual revenue, and existing debt. I’ll help you compare the available repayment options.</p>
  <p>The <a href="/term-loan-calculator.html">term loan calculator</a> models fully amortizing loans. It does not calculate a balloon balance or quote a financing offer.</p>
  <div class="faq-list">{% for item in page.faq %}<details class="faq-item"><summary>{{ item.question | escape }}</summary><p>{{ item.answer | escape }}</p></details>{% endfor %}</div>
</section>
{% include review_cta.html %}
