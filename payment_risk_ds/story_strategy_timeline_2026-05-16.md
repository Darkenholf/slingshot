# Payment Risk DS Story, Strategy, and Timeline

Date: 2026-05-16

## One-Line Positioning

I am a quant-trained data scientist who has worked on production risk monitoring, marketplace behavior, payment analytics, and experimentation. My edge for payment risk roles is the ability to turn noisy transaction and entity-level signals into decision systems that reduce loss while protecting approval rate, user trust, and business growth.

## Core Career Story

The story should not be "finance person wants to become a DS." It should be:

> I have been working on decision systems under uncertainty. At Goldman, that means production-grade monitoring and validation of risk signals across entities and markets. At ARB, that meant identifying abnormal behavior in a payments and user-interaction environment and evaluating policy interventions. At Blinkle, that meant building risk and marketplace metrics in a two-sided product with LLM-derived signals and experiments. Payment risk is the natural convergence of these experiences: statistical rigor, production monitoring, behavioral data, experimentation, and high-stakes business tradeoffs.

This story has three strengths:

- It makes the transition feel coherent instead of opportunistic.
- It translates Goldman into a tech-company risk language.
- It gives hiring teams a reason to believe the candidate can handle both model quality and business consequences.

## Resume Narrative Arc

### Opening Summary

The resume summary should be short and targeted:

Data Scientist / Quant Strategist with experience in production risk monitoring, payment analytics, marketplace experimentation, and large-scale behavioral data. Strong in SQL, Python, causal inference, anomaly detection, backtesting, and risk decisioning. Targeting payment risk, fraud analytics, and trust/safety data science roles.

### Experience Order Logic

Keep reverse chronological order, but make the first two Goldman bullets do the positioning work:

1. Production risk monitoring at scale.
2. Backtesting / DID / validation framework.
3. Decision-support impact for governance or model validation.

Then use ARB as the direct payments/fraud anchor:

1. Payments/user behavior data.
2. Abnormal traffic or creator behavior detection.
3. Policy intervention evaluation balancing abuse prevention and user experience.

Blinkle should show marketplace and product experimentation:

1. Two-sided marketplace risk metrics.
2. Structured behavioral features from LLM/product events.
3. Holdout or A/B impact on matching/conversion.

## Strongest Selling Points

### 1. Risk DNA

Goldman gives credibility in environments where wrong decisions are costly. For payment risk roles, frame this as comfort with controls, monitoring, validation, delayed feedback, and high-stakes decisions.

### 2. Experimentation Plus Risk

Many candidates are either product DS or risk modelers. The best payment risk teams need both: they must reduce fraud without breaking conversion. The candidate should repeatedly use language like "loss vs approval tradeoff," "fraud prevention vs user experience," and "experiment-backed policy launch."

### 3. Marketplace Behavior

Blinkle and ARB both help tell a story around multi-sided ecosystems. Fraud and risk in payments often emerge through networks of users, merchants, devices, creators, counterparties, and repeated behavior. This is a useful bridge to Uber, DoorDash, Airbnb, Block, and Plaid.

### 4. Production Orientation

The resume should emphasize monitoring, backtesting, validation, dashboards, controls, and operational decision support. This helps distinguish the candidate from school-project DS profiles.

## Main Weaknesses To Fix

### 1. Missing Payment/Fraud Metrics

Current resume language needs more of the standard industry vocabulary:

- fraud loss
- false positive rate
- approval rate
- payment success rate
- chargeback / dispute
- manual review
- step-up verification
- decision threshold
- precision / recall
- recall at fixed FPR
- delayed labels
- policy intervention

Only use metrics that are truthful. If the original work did not have actual chargebacks or fraud loss, describe it as abnormal behavior, abuse prevention, or risk proxy labeling.

### 2. Need A Concrete Fraud Decisioning Project

To compete for Stripe/Plaid/Robinhood/Visa/Socure/Sardine-style roles, add one GitHub project that looks like real payment risk work:

Payment Fraud Decisioning Simulator:

- transaction-level dataset
- entity features: user, card, merchant, device, IP if available
- velocity features: last 1h/24h/7d count and amount
- supervised fraud model
- rule baseline
- threshold policy: approve / review / block
- PR-AUC and recall at fixed FPR
- business simulation: fraud caught vs good users blocked
- drift and monitoring dashboard

This project should produce 2-3 resume bullets and a short interview walkthrough.

### 3. Need Role-Specific Variants

Do not use one generic resume. Maintain:

- `payment_risk_strategy_resume`: PayPal, Uber, DoorDash, Affirm, Ramp, Brex, Chime.
- `payment_fraud_ml_resume`: Stripe, Plaid, Robinhood, Visa, Coinbase, Socure, Sardine.
- `credit_risk_underwriting_resume`: Affirm, Capital One, AmEx, JPMorgan, BNPL/lending roles.
- `identity_trust_risk_resume`: Uber, Airbnb, DoorDash, SentiLink, DataVisor, ATO/synthetic identity roles.

## Interview Story Bank

Prepare 6 reusable stories:

1. Production risk monitoring at Goldman: ambiguous signal, scale, controls, stakeholder decision.
2. Backtesting and DID at Goldman: how to validate a risk signal before trusting it.
3. ARB abnormal behavior detection: how to identify risky behavior and avoid hurting good users.
4. ARB policy intervention: how to evaluate a launch when the outcome has tradeoffs.
5. Blinkle marketplace risk metrics: how to design metrics for a two-sided platform.
6. Fraud project: how to build a complete risk decisioning loop from data to model to threshold to monitoring.

Each story should be answerable in STAR format, but told like a business decision:

- What was the decision?
- What data was available?
- What was noisy or delayed?
- What metric tradeoff mattered?
- What recommendation changed?
- What did we monitor after launch?

## Detailed 8-Week Timeline

### Week 1: Positioning And Resume Foundation

Goals:

- Finish Payment Risk Strategy resume.
- Finish Payment Fraud ML resume skeleton.
- Create master bullet bank by theme.

Tasks:

- Rewrite Goldman, ARB, and Blinkle bullets in payment risk language.
- Create a skills section with SQL, Python, experimentation, causal inference, risk metrics, anomaly detection, ML evaluation, dashboards.
- Build a target tracker with A/B/C priority companies.

Deliverables:

- `resume_variants/payment_risk_strategy_resume.md`
- `resume_variants/payment_fraud_ml_resume.md`
- `application_assets/payment_risk_target_companies.md` updated with live roles.

### Week 2: Fraud Project Data And Baseline

Goals:

- Pick dataset.
- Build clean baseline notebook or script.

Tasks:

- Explore class imbalance and label delay assumptions.
- Create transaction-level features.
- Train logistic regression / tree baseline.
- Build rule baseline.
- Evaluate PR-AUC, precision, recall, recall at fixed FPR.

Deliverables:

- GitHub project repo skeleton.
- First project README.
- Initial model evaluation table.

### Week 3: Decisioning And Business Simulation

Goals:

- Make the project look like a real payment risk system.

Tasks:

- Add approve/review/block threshold policy.
- Add manual review capacity assumption.
- Simulate fraud caught, good users blocked, review volume.
- Compare rules-only, model-only, and hybrid strategies.

Deliverables:

- Decisioning dashboard or notebook section.
- 2 resume bullets from project.
- Interview walkthrough draft.

### Week 4: Monitoring, Drift, And Resume Polish

Goals:

- Finish project enough to use in applications.
- Polish resumes.

Tasks:

- Add time-based backtest.
- Add drift monitoring by cohort.
- Add architecture diagram.
- Tailor resumes for 5 real JDs.

Deliverables:

- Final project README.
- Project bullets inserted into ML-heavy resume.
- First 5 tailored application packets.

### Week 5: First Application Wave

Goals:

- Start applying with referrals where possible.

Tasks:

- Apply to 15-20 A-priority roles.
- Send referral messages to alumni and current employees.
- Track every role, source, resume version, and follow-up date.

Deliverables:

- Application tracker v1.
- Outreach template bank.
- First recruiter screen script.

### Week 6: Interview Drill Cycle

Goals:

- Prepare for screens before they arrive.

Tasks:

- 20 SQL drills around payment funnels, rolling windows, fraud rates, cohorts.
- 10 product/risk cases.
- 5 ML system/model evaluation cases.
- Practice 6 story-bank answers aloud.

Deliverables:

- SQL answer bank.
- Product case answer bank.
- Behavioral story bank.

### Week 7: Second Application Wave And Calibration

Goals:

- Increase volume and improve targeting based on response rates.

Tasks:

- Apply to another 20-25 roles.
- Compare response rates by resume variant.
- Adjust summary, top bullets, and project placement.
- Add B-priority companies and adjacent trust/safety roles.

Deliverables:

- Updated tracker with response analytics.
- Resume variant v2.

### Week 8: Interview Mode

Goals:

- Convert screens into onsites.

Tasks:

- For each company, build a 1-page interview brief:
  - business model
  - likely risk problems
  - role-specific keywords
  - 3 questions to ask the team
- Do mock cases for companies with scheduled screens.
- Tighten project walkthrough to 3 minutes and 8 minutes versions.

Deliverables:

- Company interview briefs.
- Finalized behavioral answers.
- Finalized fraud project walkthrough.

## Weekly Operating Rhythm

Monday:

- Refresh target roles.
- Choose 8-10 applications for the week.
- Identify referral targets.

Tuesday-Wednesday:

- Tailor resumes and submit applications.
- Send referral/outreach messages.

Thursday:

- SQL and product case drills.
- Improve one resume/project artifact.

Friday:

- Follow up with recruiters/referrals.
- Review tracker metrics.
- Decide next week's target adjustments.

Weekend:

- Deep work on project or interview stories.

## Application Quality Bar

Before applying to a role, confirm:

- Resume top half contains at least 3 JD-matching keywords.
- Most relevant experience appears in the first 6 bullets.
- The resume variant matches the role family.
- There is one clear payment/risk story to tell in the recruiter screen.
- Tracker includes source, resume version, date, referral status, and follow-up date.

## Best Next Move

The best immediate move is not mass applying yet. The best move is:

1. Build the two payment risk resume variants.
2. Create the fraud decisioning project skeleton.
3. Apply to 10 highly matched roles with tailored resumes and referral outreach.

This gives the search a sharp wedge: credible enough for risk strategy roles immediately, and increasingly credible for model-heavy fraud DS roles after the project is visible.
