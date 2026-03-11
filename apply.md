---
title: "Business Financing Application | Nicolas Lescalier"
description: "Submit a structured business financing application to Nicolas Lescalier for working capital, term loans, equipment financing, factoring, SBA, bridge, and mortgage scenarios."
permalink: /apply/
layout: default
---

<section class="section">
  <div class="section-band">
    <div class="section-band__panel">
      <p class="eyebrow">Application</p>
      <h1>Start a structured financing application.</h1>
      <p>This page is designed to give me enough context to review the situation quickly and point you toward the most realistic financing path. It is intentionally more detailed than the contact page, but still cleaner than a full underwriting package.</p>
      <div class="section-band__actions">
        <a class="button" href="#application-form">Start the application</a>
        <a class="button button--secondary" href="/contact/">Prefer a call first?</a>
      </div>
    </div>
    <div class="mini-grid">
      <article class="mini-card">
        <h3>Best use of this page</h3>
        <p>Use it when you already want a real financing review, not just general information.</p>
      </article>
      <article class="mini-card">
        <h3>Security note</h3>
        <p>Do not submit SSN, full tax returns, bank login credentials, or highly sensitive IDs through this public form. If the file is a fit, sensitive documents can be requested separately.</p>
      </article>
    </div>
  </div>
</section>

<section class="section">
  <div class="step-grid">
    <article class="step-card">
      <span class="step-card__number">1</span>
      <h3>Share the basics</h3>
      <p>Tell me who you are, what business needs funding, and what the capital is meant to solve.</p>
    </article>
    <article class="step-card">
      <span class="step-card__number">2</span>
      <h3>Give enough business context</h3>
      <p>Revenue, time in business, ownership, industry, and current constraints usually matter more than broad sales language.</p>
    </article>
    <article class="step-card">
      <span class="step-card__number">3</span>
      <h3>Get a cleaner first review</h3>
      <p>If the scenario is workable, I can respond with a better sense of fit, likely product path, and what to prepare next.</p>
    </article>
  </div>
</section>

<section class="section" id="application-form">
  <p class="eyebrow">Application Form</p>
  <h2>Business financing request</h2>
  <p class="section-intro">Fill in what you know. A precise, coherent summary is more useful than trying to guess every underwriting question perfectly.</p>

  <form class="contact-form" action="https://formspree.io/f/maypkwyo" method="POST">
    <input type="hidden" name="_subject" value="New financing application from nicolaslescalier.com">

    <div class="form-section">
      <h3 class="form-section__title">Applicant contact</h3>
      <p class="form-section__copy">Who should I contact first about this request?</p>
      <div class="form-grid--application">
        <div>
          <label for="first_name">First name</label>
          <input type="text" id="first_name" name="first_name" required placeholder="John">
        </div>
        <div>
          <label for="last_name">Last name</label>
          <input type="text" id="last_name" name="last_name" required placeholder="Doe">
        </div>
        <div>
          <label for="email">Email</label>
          <input type="email" id="email" name="email" required placeholder="email@business.com">
        </div>
        <div>
          <label for="mobile_phone">Mobile phone</label>
          <input type="tel" id="mobile_phone" name="mobile_phone" required placeholder="(305) 555-1212">
        </div>
      </div>
    </div>

    <div class="form-section">
      <h3 class="form-section__title">Business details</h3>
      <p class="form-section__copy">This is the minimum business profile needed for a useful first review.</p>
      <div class="form-grid--application">
        <div>
          <label for="legal_company_name">Legal company name</label>
          <input type="text" id="legal_company_name" name="legal_company_name" required placeholder="Smith Roofing LLC">
        </div>
        <div>
          <label for="business_phone">Business phone</label>
          <input type="tel" id="business_phone" name="business_phone" placeholder="(305) 555-9898">
        </div>
        <div>
          <label for="business_start_date">Business start date</label>
          <input type="date" id="business_start_date" name="business_start_date">
        </div>
        <div>
          <label for="industry">Industry</label>
          <input type="text" id="industry" name="industry" required placeholder="Construction, retail, hospitality, logistics, etc.">
        </div>
        <div>
          <label for="state_of_incorporation">State of incorporation</label>
          <input type="text" id="state_of_incorporation" name="state_of_incorporation" required placeholder="Florida">
        </div>
        <div>
          <label for="entity_type">Entity type</label>
          <input type="text" id="entity_type" name="entity_type" placeholder="LLC, Corp, S-Corp, Sole Prop">
        </div>
        <div>
          <label for="company_website">Company website</label>
          <input type="url" id="company_website" name="company_website" placeholder="https://example.com">
        </div>
        <div>
          <label for="ownership_percent">Ownership percentage</label>
          <input type="text" id="ownership_percent" name="ownership_percent" placeholder="100%">
        </div>
        <div>
          <label for="employees">Number of employees</label>
          <input type="number" id="employees" name="employees" min="0" placeholder="12">
        </div>
        <div>
          <label for="fico_range">Estimated FICO range</label>
          <input type="text" id="fico_range" name="fico_range" placeholder="620-660">
        </div>
      </div>
    </div>

    <div class="form-section">
      <h3 class="form-section__title">Funding request</h3>
      <p class="form-section__copy">This is usually the most important section for product fit.</p>
      <div class="form-grid--application">
        <div>
          <label for="amount_requested">Amount requested</label>
          <input type="text" id="amount_requested" name="amount_requested" required placeholder="$150,000">
        </div>
        <div>
          <label for="timeline">Preferred timeline</label>
          <input type="text" id="timeline" name="timeline" required placeholder="3 days, 2 weeks, 45 days, etc.">
        </div>
        <div>
          <label for="product_interest">Product you think you need</label>
          <input type="text" id="product_interest" name="product_interest" placeholder="MCA, LOC, term loan, equipment, SBA, bridge, mortgage, not sure">
        </div>
        <div>
          <label for="monthly_revenue">Estimated monthly revenue</label>
          <input type="text" id="monthly_revenue" name="monthly_revenue" placeholder="$80,000">
        </div>
        <div class="form-group--full">
          <label for="use_of_proceeds">Use of proceeds</label>
          <textarea id="use_of_proceeds" name="use_of_proceeds" rows="4" required placeholder="What the capital will be used for, why it is needed now, and what happens if the timing slips."></textarea>
        </div>
        <div class="form-group--full">
          <label for="current_constraints">Current constraints or existing debt</label>
          <textarea id="current_constraints" name="current_constraints" rows="4" placeholder="Existing advances, loans, liens, collateral issues, tax issues, seasonality, or anything else that could affect approval."></textarea>
        </div>
      </div>
    </div>

    <div class="form-section">
      <h3 class="form-section__title">Business and owner address</h3>
      <p class="form-section__copy">Enough location detail to understand the operating base and jurisdiction.</p>
      <div class="form-grid--application">
        <div class="form-group--full">
          <label for="address_line_1">Address line 1</label>
          <input type="text" id="address_line_1" name="address_line_1" required placeholder="42 Railroad St">
        </div>
        <div class="form-group--full">
          <label for="address_line_2">Address line 2</label>
          <input type="text" id="address_line_2" name="address_line_2" placeholder="Suite 200">
        </div>
        <div>
          <label for="city">City</label>
          <input type="text" id="city" name="city" required placeholder="Miami">
        </div>
        <div>
          <label for="state">State</label>
          <input type="text" id="state" name="state" required placeholder="Florida">
        </div>
        <div>
          <label for="zip">ZIP</label>
          <input type="text" id="zip" name="zip" required placeholder="33101">
        </div>
        <div>
          <label for="homeowner_status">Do you own home property?</label>
          <input type="text" id="homeowner_status" name="homeowner_status" placeholder="Yes / No / Prefer not to say">
        </div>
      </div>
    </div>

    <div class="form-section">
      <h3 class="form-section__title">Final context</h3>
      <p class="form-section__copy">Short answers here often improve the first review more than extra attachments.</p>
      <div class="form-grid--application">
        <div>
          <label for="card_processing">Do you process credit cards?</label>
          <input type="text" id="card_processing" name="card_processing" placeholder="Yes / No">
        </div>
        <div>
          <label for="multiple_businesses">Do you own multiple businesses?</label>
          <input type="text" id="multiple_businesses" name="multiple_businesses" placeholder="Yes / No">
        </div>
        <div>
          <label for="home_based">Is the business home based?</label>
          <input type="text" id="home_based" name="home_based" placeholder="Yes / No">
        </div>
        <div>
          <label for="best_time">Best time to reach you</label>
          <input type="text" id="best_time" name="best_time" placeholder="Morning, afternoon, after 4pm, etc.">
        </div>
        <div class="form-group--full">
          <label for="additional_context">Anything else that matters?</label>
          <textarea id="additional_context" name="additional_context" rows="5" placeholder="Add anything important that would help me understand the file quickly."></textarea>
        </div>
      </div>
    </div>

    <div class="notice-card">
      <p class="eyebrow">Consent</p>
      <div class="checkbox-list">
        <label for="consent_contact">
          <input type="checkbox" id="consent_contact" name="consent_contact" required>
          <span>I consent to be contacted about this financing request by phone, email, or text.</span>
        </label>
        <label for="consent_truthful">
          <input type="checkbox" id="consent_truthful" name="consent_truthful" required>
          <span>I confirm the information submitted here is accurate to the best of my knowledge.</span>
        </label>
      </div>
      <p class="input-help">Sensitive items such as SSN, full bank statements, tax returns, and IDs should not be submitted through this form unless requested separately through a secure next step.</p>
    </div>

    <div class="cta-row">
      <button class="button" type="submit">Submit application</button>
      <a class="button button--secondary" href="/contact/">Prefer a shorter first message?</a>
    </div>
  </form>
</section>
