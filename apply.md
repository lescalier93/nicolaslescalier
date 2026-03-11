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
      <h1>Start a financing application that feels closer to a real deal intake.</h1>
      <p>This page is designed to feel more like a lender-style first step: structured, fast to scan, and focused on the details that actually help narrow the right capital path. It is intentionally more visual and more guided than the contact page.</p>
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

<script>
  window.addEventListener("DOMContentLoaded", () => {
    const params = new URLSearchParams(window.location.search);
    const form = document.querySelector(".contact-form");
    const scenarioCarryover = document.getElementById("scenarioCarryover");
    const scenarioCarryoverText = document.getElementById("scenarioCarryoverText");

    const setFieldValue = (id, value) => {
      const field = document.getElementById(id);
      if (!field || !value) {
        return;
      }
      field.value = value;
    };

    const setSelectByText = (id, value) => {
      const field = document.getElementById(id);
      if (!field || !value) {
        return;
      }
      const option = Array.from(field.options).find((entry) => entry.value === value || entry.text === value);
      if (option) {
        field.value = option.value;
      }
    };

    const humanizeLeadSource = (value) => {
      const sourceMap = {
        website: "the website",
        mca_calculator: "the MCA calculator",
        term_calculator: "the term calculator",
      };
      return sourceMap[value] || String(value || "the website").replace(/_/g, " ");
    };

    const humanizeScenarioOrigin = (value) => {
      const scenarioMap = {
        payment: "payment-based",
        loanAmount: "loan-amount-based",
        interestRate: "rate-based",
        loanTerm: "term-based",
      };
      return scenarioMap[value] || value;
    };

    setFieldValue("lead_source", params.get("lead_source") || "website");
    setFieldValue("scenario_origin", params.get("scenario_origin") || "");

    if (!params.toString()) {
      form?.addEventListener("submit", () => {
        if (typeof window.nicolasTrack === "function") {
          window.nicolasTrack("application_submit_started", {
            lead_source: "website",
          });
        }
      });
      return;
    }

    const productInterest = params.get("product_interest");
    if (productInterest) {
      const radio = Array.from(document.querySelectorAll('input[name="product_interest"]')).find(
        (input) => input.value.toLowerCase() === productInterest.toLowerCase()
      );

      if (radio) {
        radio.checked = true;
      } else {
        setFieldValue("product_interest_other", productInterest);
      }
    }

    setSelectByText("amount_requested", params.get("amount_requested"));
    setFieldValue("use_of_proceeds", params.get("use_of_proceeds"));
    setFieldValue("additional_context", params.get("additional_context"));

    const leadSource = params.get("lead_source") || "website";
    const scenarioOrigin = params.get("scenario_origin");

    if (scenarioCarryover && scenarioCarryoverText && (leadSource !== "website" || scenarioOrigin)) {
      scenarioCarryover.hidden = false;
      scenarioCarryoverText.textContent = scenarioOrigin
        ? `Calculator context has been carried into this form from ${humanizeLeadSource(leadSource)} using the "${humanizeScenarioOrigin(scenarioOrigin)}" scenario.`
        : `Calculator context has been carried into this form from ${humanizeLeadSource(leadSource)}.`;
    }

    if (typeof window.nicolasTrack === "function") {
      window.nicolasTrack("application_prefill_loaded", {
        lead_source: leadSource,
        product_interest: productInterest || "",
        scenario_origin: scenarioOrigin || "",
      });
    }

    form?.addEventListener("submit", () => {
      if (typeof window.nicolasTrack === "function") {
        window.nicolasTrack("application_submit_started", {
          lead_source: leadSource,
          product_interest: productInterest || "",
        });
      }
    });
  });
</script>

<section class="section">
  <div class="step-grid">
    <article class="step-card">
      <span class="step-card__number">1</span>
      <h3>Choose the likely financing lane</h3>
      <p>Start with the closest fit, even if you are not fully sure yet.</p>
    </article>
    <article class="step-card">
      <span class="step-card__number">2</span>
      <h3>Give enough operating context</h3>
      <p>Revenue, time in business, and the funding problem matter most.</p>
    </article>
    <article class="step-card">
      <span class="step-card__number">3</span>
      <h3>Get a cleaner fit review</h3>
      <p>If it is workable, I can respond with a better next step.</p>
    </article>
  </div>
</section>

<section class="section" id="application-form">
  <p class="eyebrow">Application Form</p>
  <h2>Business financing request</h2>
  <p class="section-intro">Fill in what you know. A precise, coherent summary is more useful than trying to guess every underwriting question perfectly.</p>
  <div class="pill-row">
    <span class="pill">Structured for MCA, term, LOC, SBA, equipment, bridge, and CRE</span>
    <span class="pill">Built for faster first review</span>
    <span class="pill">Usually 2-3 minutes to complete</span>
    <span class="pill">No SSN requested on-page</span>
  </div>

  <div class="application-frame">
    <div class="application-intro-card">
      <div>
        <strong>Best results come from concise answers</strong>
        <span>Choose the closest dropdown option and use text fields only where context actually helps.</span>
      </div>
      <div>
        <strong>Goal of this form</strong>
        <span>Get you to the right financing path faster, not bury you in underwriting too early.</span>
      </div>
    </div>
    <div class="notice-card" id="scenarioCarryover" hidden>
      <p class="eyebrow">Carried over from a calculator</p>
      <p id="scenarioCarryoverText">Your calculator scenario has been carried into the application.</p>
    </div>

  <form class="contact-form" action="https://formspree.io/f/mgonknak" method="POST">
    <input type="hidden" name="_subject" value="New financing application from nicolaslescalier.com">
    <input type="hidden" id="lead_source" name="lead_source" value="website">
    <input type="hidden" id="scenario_origin" name="scenario_origin" value="">

    <div class="form-section form-section--accent">
      <div class="form-section__header">
        <span class="form-section__number">1</span>
        <div>
          <h3 class="form-section__title">What are you most likely applying for?</h3>
          <p class="form-section__copy">Pick the closest fit. This does not lock the file into that product.</p>
        </div>
      </div>
      <div class="choice-grid">
        <div class="choice-card">
          <input type="radio" id="product_mca" name="product_interest" value="Merchant cash advance">
          <label for="product_mca">
            <strong>Merchant cash advance</strong>
            <span>Fast working capital and short-term speed</span>
          </label>
        </div>
        <div class="choice-card">
          <input type="radio" id="product_loc" name="product_interest" value="Line of credit">
          <label for="product_loc">
            <strong>Line of credit</strong>
            <span>Flexible repeat-use working capital</span>
          </label>
        </div>
        <div class="choice-card">
          <input type="radio" id="product_term" name="product_interest" value="Term loan">
          <label for="product_term">
            <strong>Term loan</strong>
            <span>Growth, refinance, and fixed repayment</span>
          </label>
        </div>
        <div class="choice-card">
          <input type="radio" id="product_equipment" name="product_interest" value="Equipment financing">
          <label for="product_equipment">
            <strong>Equipment financing</strong>
            <span>Vehicles, machinery, devices, tools</span>
          </label>
        </div>
        <div class="choice-card">
          <input type="radio" id="product_factoring" name="product_interest" value="Factoring or invoice finance">
          <label for="product_factoring">
            <strong>Factoring</strong>
            <span>Receivables-based working capital</span>
          </label>
        </div>
        <div class="choice-card">
          <input type="radio" id="product_po" name="product_interest" value="PO financing">
          <label for="product_po">
            <strong>PO financing</strong>
            <span>Large purchase order fulfillment</span>
          </label>
        </div>
        <div class="choice-card">
          <input type="radio" id="product_sba" name="product_interest" value="SBA 7(a)">
          <label for="product_sba">
            <strong>SBA 7(a)</strong>
            <span>Longer-term lower-cost structure</span>
          </label>
        </div>
        <div class="choice-card">
          <input type="radio" id="product_cre" name="product_interest" value="Bridge or mortgage financing">
          <label for="product_cre">
            <strong>Bridge / mortgage</strong>
            <span>CRE, refinance, acquisition, timing gap</span>
          </label>
        </div>
      </div>
      <div>
        <label for="product_interest_other">Or describe it in your own words</label>
        <input type="text" id="product_interest_other" name="product_interest_other" placeholder="Not sure yet, comparing options, or a more specific scenario">
      </div>
    </div>

    <div class="form-section">
      <div class="form-section__header">
        <span class="form-section__number">2</span>
        <div>
          <h3 class="form-section__title">Applicant contact</h3>
          <p class="form-section__copy">Who should I contact first about this request?</p>
        </div>
      </div>
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
        <div>
          <label for="best_time">Best time to reach you</label>
          <select id="best_time" name="best_time">
            <option value="">Select preferred time</option>
            <option>Morning</option>
            <option>Midday</option>
            <option>Afternoon</option>
            <option>After 4pm</option>
            <option>Text first</option>
            <option>Email first</option>
          </select>
        </div>
      </div>
    </div>

    <div class="form-section">
      <div class="form-section__header">
        <span class="form-section__number">3</span>
        <div>
          <h3 class="form-section__title">Business details</h3>
          <p class="form-section__copy">This is the minimum business profile needed for a useful first review.</p>
        </div>
      </div>
      <div class="form-grid--application">
        <div>
          <label for="legal_company_name">Legal company name</label>
          <input type="text" id="legal_company_name" name="legal_company_name" required placeholder="Smith Roofing LLC">
        </div>
        <div>
          <label for="business_start_date">Business start date</label>
          <input type="date" id="business_start_date" name="business_start_date">
        </div>
        <div>
          <label for="industry">Industry</label>
          <select id="industry" name="industry" required>
            <option value="">Select industry</option>
            <option>Construction</option>
            <option>E-commerce</option>
            <option>Hospitality / restaurant</option>
            <option>Manufacturing</option>
            <option>Medical / healthcare</option>
            <option>Professional services</option>
            <option>Real estate / investor</option>
            <option>Retail</option>
            <option>Transportation / logistics</option>
            <option>Wholesale / distribution</option>
            <option>Other</option>
          </select>
        </div>
        <div>
          <label for="state_of_incorporation">State of incorporation</label>
          <select id="state_of_incorporation" name="state_of_incorporation" required>
            <option value="">Select state</option>
            <option>Alabama</option>
            <option>Alaska</option>
            <option>Arizona</option>
            <option>Arkansas</option>
            <option>California</option>
            <option>Colorado</option>
            <option>Connecticut</option>
            <option>Delaware</option>
            <option>District of Columbia</option>
            <option>Florida</option>
            <option>Georgia</option>
            <option>Hawaii</option>
            <option>Idaho</option>
            <option>Illinois</option>
            <option>Indiana</option>
            <option>Iowa</option>
            <option>Kansas</option>
            <option>Kentucky</option>
            <option>Louisiana</option>
            <option>Maine</option>
            <option>Maryland</option>
            <option>Massachusetts</option>
            <option>Michigan</option>
            <option>Minnesota</option>
            <option>Mississippi</option>
            <option>Missouri</option>
            <option>Montana</option>
            <option>Nebraska</option>
            <option>Nevada</option>
            <option>New Hampshire</option>
            <option>New Jersey</option>
            <option>New Mexico</option>
            <option>New York</option>
            <option>North Carolina</option>
            <option>North Dakota</option>
            <option>Ohio</option>
            <option>Oklahoma</option>
            <option>Oregon</option>
            <option>Pennsylvania</option>
            <option>Rhode Island</option>
            <option>South Carolina</option>
            <option>South Dakota</option>
            <option>Tennessee</option>
            <option>Texas</option>
            <option>Utah</option>
            <option>Vermont</option>
            <option>Virginia</option>
            <option>Washington</option>
            <option>West Virginia</option>
            <option>Wisconsin</option>
            <option>Wyoming</option>
          </select>
        </div>
        <div>
          <label for="entity_type">Entity type</label>
          <select id="entity_type" name="entity_type">
            <option value="">Select entity type</option>
            <option>Corporation</option>
            <option>LLC</option>
            <option>Nonprofit</option>
            <option>Partnership</option>
            <option>S-Corp</option>
            <option>Sole Proprietorship</option>
          </select>
        </div>
        <div>
          <label for="fico_range">Estimated FICO range</label>
          <select id="fico_range" name="fico_range">
            <option value="">Select estimated range</option>
            <option>Below 550</option>
            <option>550-599</option>
            <option>600-649</option>
            <option>650-699</option>
            <option>700-749</option>
            <option>750+</option>
            <option>Not sure</option>
          </select>
        </div>
      </div>
    </div>

    <div class="form-section form-section--accent">
      <div class="form-section__header">
        <span class="form-section__number">4</span>
        <div>
          <h3 class="form-section__title">Funding request</h3>
          <p class="form-section__copy">This is usually the most important section for product fit.</p>
        </div>
      </div>
      <div class="form-grid--application">
        <div>
          <label for="amount_requested">Amount requested</label>
          <select id="amount_requested" name="amount_requested" required>
            <option value="">Select amount range</option>
            <option>Under $25,000</option>
            <option>$25,000-$50,000</option>
            <option>$50,000-$100,000</option>
            <option>$100,000-$250,000</option>
            <option>$250,000-$500,000</option>
            <option>$500,000-$1,000,000</option>
            <option>$1,000,000+</option>
          </select>
        </div>
        <div>
          <label for="timeline">Preferred timeline</label>
          <select id="timeline" name="timeline" required>
            <option value="">Select timing</option>
            <option>Need it in 24-72 hours</option>
            <option>Need it within 1 week</option>
            <option>Need it within 2-4 weeks</option>
            <option>Need it within 30-60 days</option>
            <option>Planning ahead / exploring</option>
          </select>
        </div>
        <div>
          <label for="monthly_revenue">Estimated monthly revenue</label>
          <select id="monthly_revenue" name="monthly_revenue">
            <option value="">Select revenue range</option>
            <option>Under $20,000</option>
            <option>$20,000-$50,000</option>
            <option>$50,000-$100,000</option>
            <option>$100,000-$250,000</option>
            <option>$250,000-$500,000</option>
            <option>$500,000+</option>
          </select>
        </div>
        <div>
          <label for="use_case_priority">What matters most right now?</label>
          <select id="use_case_priority" name="use_case_priority">
            <option value="">Select priority</option>
            <option>Speed</option>
            <option>Lowest payment pressure</option>
            <option>Highest approval odds</option>
            <option>Longer-term structure</option>
            <option>Bridge or timing solution</option>
            <option>Not sure yet</option>
          </select>
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
      <div class="form-section__header">
        <span class="form-section__number">5</span>
        <div>
          <h3 class="form-section__title">Final context</h3>
          <p class="form-section__copy">A few short selectors usually tell me more than a long intake.</p>
        </div>
      </div>
      <div class="form-grid--application">
        <div>
          <label for="state">Operating state</label>
          <select id="state" name="state" required>
            <option value="">Select state</option>
            <option>Alabama</option>
            <option>Alaska</option>
            <option>Arizona</option>
            <option>Arkansas</option>
            <option>California</option>
            <option>Colorado</option>
            <option>Connecticut</option>
            <option>Delaware</option>
            <option>District of Columbia</option>
            <option>Florida</option>
            <option>Georgia</option>
            <option>Hawaii</option>
            <option>Idaho</option>
            <option>Illinois</option>
            <option>Indiana</option>
            <option>Iowa</option>
            <option>Kansas</option>
            <option>Kentucky</option>
            <option>Louisiana</option>
            <option>Maine</option>
            <option>Maryland</option>
            <option>Massachusetts</option>
            <option>Michigan</option>
            <option>Minnesota</option>
            <option>Mississippi</option>
            <option>Missouri</option>
            <option>Montana</option>
            <option>Nebraska</option>
            <option>Nevada</option>
            <option>New Hampshire</option>
            <option>New Jersey</option>
            <option>New Mexico</option>
            <option>New York</option>
            <option>North Carolina</option>
            <option>North Dakota</option>
            <option>Ohio</option>
            <option>Oklahoma</option>
            <option>Oregon</option>
            <option>Pennsylvania</option>
            <option>Rhode Island</option>
            <option>South Carolina</option>
            <option>South Dakota</option>
            <option>Tennessee</option>
            <option>Texas</option>
            <option>Utah</option>
            <option>Vermont</option>
            <option>Virginia</option>
            <option>Washington</option>
            <option>West Virginia</option>
            <option>Wisconsin</option>
            <option>Wyoming</option>
          </select>
        </div>
        <div>
          <label for="time_in_business">Time in business</label>
          <select id="time_in_business" name="time_in_business">
            <option value="">Select time in business</option>
            <option>Under 6 months</option>
            <option>6-12 months</option>
            <option>1-2 years</option>
            <option>2-5 years</option>
            <option>5+ years</option>
          </select>
        </div>
        <div>
          <label for="card_processing">Do you process credit cards?</label>
          <select id="card_processing" name="card_processing">
            <option value="">Select option</option>
            <option>Yes</option>
            <option>No</option>
          </select>
        </div>
        <div>
          <label for="multiple_businesses">Do you own multiple businesses?</label>
          <select id="multiple_businesses" name="multiple_businesses">
            <option value="">Select option</option>
            <option>Yes</option>
            <option>No</option>
          </select>
        </div>
        <div>
          <label for="existing_balance">Any existing advance or loan balance?</label>
          <select id="existing_balance" name="existing_balance">
            <option value="">Select option</option>
            <option>No existing debt</option>
            <option>Yes, manageable</option>
            <option>Yes, heavy payment pressure</option>
            <option>Not sure</option>
          </select>
        </div>
        <div class="form-group--full">
          <label for="additional_context">Anything else that matters?</label>
          <textarea id="additional_context" name="additional_context" rows="4" placeholder="Optional. Add anything important that would help me understand the file quickly."></textarea>
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
        <label for="consent_sms_marketing">
          <input type="checkbox" id="consent_sms_marketing" name="consent_sms_marketing">
          <span>By checking this box, you agree to receive marketing text messages, including payment reminders, promotional offers, and customer care messages, at the mobile number provided. Message frequency varies. Consent is not a condition of any purchase. Message and data rates may apply. Reply STOP to unsubscribe or HELP for assistance. For support, contact us at <a href="tel:+13056993636">(305) 699-3636</a>. Information gathered in this SMS program will not be shared with third parties or affiliates for marketing purposes. I have read and agree to the <a href="/terms-and-conditions/">Terms and Conditions</a> and <a href="/privacy-policy/">Privacy Policy</a>.</span>
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
  </div>
</section>
