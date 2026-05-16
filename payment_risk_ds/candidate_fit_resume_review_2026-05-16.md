# Candidate Fit & Resume Review: Payment / Risk / Fraud DS

Date: 2026-05-16

Source resume reviewed: `/Users/richard/Desktop/Yihan Li.pdf`

## 1. 当前简历摘要

Current positioning:

- Goldman Sachs, Quantitative Strategist, Nov 2025 - Present.
- Blinkle AI, Data Scientist (Part-time), Product, Sep 2025 - Jan 2026.
- ARB Interactive, Data Scientist Intern, Payments, Jun 2024 - Sep 2024.
- UCLA Master of Quantitative Economics, July 2025, GPA 4.00/4.00.
- Nanjing University Economics + Math minor, GPA 3.93/4.00.

当前简历已经明显偏 risk/product DS，而不是泛泛 quant resume。对于 payment/risk/fraud DS，这是好事。

## 2. 已经写得好的地方

### Goldman Sachs

强项：
- "production risk metrics monitoring"
- "transaction- and entity-level pricing and liquidity signals"
- "100+ global entities / billions of records"
- "detect anomalies and quantify shifts"
- "DID and historical backtesting"
- "production-grade validation and control frameworks"
- "auditable, reliable, high-stakes governance"

这些都非常接近 fintech risk DS 的语言。尤其是 DID/backtesting、anomaly/risk indicator、governance/model validation，是 payment risk 的核心资产。

### Blinkle AI

强项：
- "two-sided marketplace"
- "risk metrics framework"
- "low-quality or suspicious behavior"
- "LLM-derived unstructured features"
- "holdout and A/B experiments"
- "screening/ranking logic"

这段对 Uber/DoorDash/Plaid/OpenAI 很有价值，因为它把 marketplace、risk、LLM signal extraction、experimentation 放在一起。

### ARB Interactive

强项：
- title 直接有 Payments。
- "hundreds of millions of interaction events"
- "detect abnormal traffic and creator behavior"
- "intervention and traffic-control strategy"
- "causal impact framework"
- "risk-adjusted budget allocation"
- "high-risk cohorts"
- "optimize abuse prevention and user experience trade-off"

这是全简历里最像 payment/fraud/risk DS 的一段，应该进一步强化。

## 3. 当前问题

### 问题 A：缺少 fintech fraud 的标准指标

现在写了 risk、abnormal、false investigation triggers，但还不够像 fraud JD。

建议加入或替换的指标词：
- fraud loss / risk loss
- false positive rate
- precision / recall / PR-AUC
- approval/payment success
- customer friction
- manual review workload
- chargeback / dispute / unauthorized behavior
- decisioning / rules / thresholds

### 问题 B：没有清楚呈现 rules + ML + ops 的闭环

Payment risk JD 常常问：你发现风险以后怎么上线？是 rule？model？manual review？monitoring？谁执行？

当前简历有 analysis 和 strategy，但上线闭环还不够明显。

建议每段至少有一个 bullet 写：
- designed risk rules / scoring logic
- backtested against historical cases
- monitored post-launch drift / loss / FPR
- partnered with engineering / ops to deploy

### 问题 C：Goldman 语境偏 market risk，不是 payment risk

Goldman 经历很强，但需要更清楚地翻译成 fintech 风控能力。

不要过多强调 pricing/liquidity 本身，而要强调：
- high-stakes risk monitoring
- anomaly detection over transaction/entity-level data
- causal/backtesting to separate signal from noise
- governance/auditability
- reducing false alerts / investigation burden

### 问题 D：技术栈还可以更贴 JD

当前 skills 有 Python、SQL、R、Spark、Airflow、AWS、XGBoost，但简历 bullet 里没有充分出现：
- Spark/PySpark
- classification / tree-based models
- model evaluation
- pipeline / monitoring

如果真实做过，应前置到经历 bullet；如果没做过，需要用 project 补。

## 4. Payment Risk 方向的理想简历结构

### Header

保留当前 header。建议加 LinkedIn/GitHub，如果有相关项目。

### Experience order

当前顺序合理：Goldman -> Blinkle -> ARB -> Education -> Skills。

### Skills section 建议重排

建议改成：

- Risk & Payment Analytics: Fraud/Risk Monitoring, Transaction Risk, Anomaly Detection, Risk Scoring, Backtesting, A/B Testing, Causal Inference, DID, Cohort Analysis, False-Positive Analysis
- Machine Learning: Classification, Imbalanced Data, Tree-Based Models (XGBoost), Clustering, Feature Engineering, Model Validation, LLM Feature Extraction
- Data & Engineering: SQL, Python, PySpark/Spark, Airflow, AWS, Tableau, Data Pipelines, Dashboarding
- Statistics: Hypothesis Testing, Regression, Time Series, Optimization, Experimental Design

## 5. 具体 bullet 改写方向

以下是方向性 draft，不代表事实新增；最终需要基于真实经历确认。

### Goldman Sachs: 更 payment-risk 化

Current idea:
"Owned production risk metrics monitoring..."

Possible rewrite:
- Owned production risk-monitoring framework across transaction- and entity-level pricing/liquidity signals for 100+ global entities, analyzing billions of records to detect anomalies, quantify risk shifts, and trigger drill-down investigations.
- Decomposed abnormal movements in ratio-based risk indicators into pricing, funding, and balance-sheet drivers, separating structural changes from noise across multi-billion-record datasets and cross-region cohorts.
- Applied quasi-experimental methods and historical backtesting to evaluate policy/market changes, reducing false investigation triggers and improving confidence in risk-control decisions.
- Built auditable validation and control workflows for AI-assisted analytical outputs, aligning model outputs with governance, documentation, and high-stakes stakeholder review requirements.

### Blinkle AI: 更 fraud/product decisioning 化

Possible rewrite:
- Defined risk and quality metrics for a two-sided job marketplace, including match quality, recommendation quality, suspicious behavior, and application conversion, creating a shared decisioning framework for product and engineering teams.
- Analyzed millions of user events with SQL/Python to identify low-quality or suspicious behavior patterns degrading matching quality, surfacing high-risk cohorts and product friction points.
- Built LLM-derived structured features from resumes and job descriptions for scoring/ranking pipelines, improving screening precision and top-match accuracy by 37%.
- Designed holdout and A/B experiments for screening/ranking interventions, quantifying precision-conversion-friction tradeoffs and increasing application conversion by 41%.

### ARB Interactive: 最应该强化的一段

Possible rewrite:
- Analyzed hundreds of millions of payment-adjacent interaction events to detect abnormal traffic, creator abuse, and high-risk behavioral cohorts, supporting intervention and traffic-control strategies.
- Developed a causal impact framework using counterfactual baselines and retention modeling to estimate incremental ROI of intervention/incentive policies, improving policy ROI by 18%.
- Built segmentation models using behavioral features and K-Means clustering to identify heterogeneous response and risk patterns, enabling targeted interventions that increased DAU by 12% while reducing unnecessary user friction.
- Designed and analyzed A/B tests for policy interventions, measuring effects on creator retention, content quality, platform health, and abuse-prevention tradeoffs.

## 6. 需要新增的项目 / 经历

为了投 Stripe/Plaid/Robinhood/Coinbase/Visa 这种更模型化岗位，建议新增一个 payment fraud project，项目不需要很花，但要完整体现 industry workflow。

Project A: Real-Time Payment Fraud Decisioning Simulator

Dataset:
- Kaggle IEEE-CIS Fraud Detection, PaySim, Credit Card Fraud, or synthetic transaction data.

Deliverables:
- Feature engineering: user velocity, merchant velocity, amount z-score, device/IP proxies if available, time-of-day, graph degree-like features.
- Model: logistic regression baseline + XGBoost/LightGBM.
- Evaluation: PR-AUC, recall at fixed FPR, precision at review capacity, calibration.
- Decision policy: approve / step-up / manual review / block.
- Backtesting: compare model vs rule baseline on historical slices.
- Monitoring: drift dashboard and alert thresholds.

Resume bullet target:
- Built an end-to-end payment fraud decisioning simulator on imbalanced transaction data, combining rules and XGBoost risk scores to optimize fraud capture under fixed false-positive/manual-review constraints; backtested policies across time-based cohorts and built monitoring dashboards for drift and precision/recall.

Project B: ATO / Identity Risk Graph

Deliverables:
- Construct graph between users, devices, emails, cards, IPs, merchants.
- Detect suspicious connected components / shared instruments.
- Use graph features in classifier.

Project C: Credit Risk / Underwriting

Deliverables:
- Lending Club / Home Credit dataset.
- PD model, expected loss, threshold by risk-return, approval-rate simulation.

## 7. Target resume variants

先做 2 个版本：

1. `payment_risk_strategy_resume`
   - 目标：PayPal, Uber, DoorDash, Affirm, Ramp, Brex, Chime.
   - 强调：risk metrics, backtesting, intervention, false positives, stakeholder strategy, causal inference.

2. `payment_fraud_ml_resume`
   - 目标：Stripe, Plaid, Robinhood, Visa, Coinbase, Capital One, Socure, Sardine.
   - 强调：classification, imbalanced data, model evaluation, model monitoring, rules + ML, feature engineering, production pipeline.

当前简历更接近第 1 个版本；第 2 个版本需要补 project 或更明确的 ML bullet。

