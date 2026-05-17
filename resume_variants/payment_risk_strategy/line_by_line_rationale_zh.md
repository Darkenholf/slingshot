# Payment Risk Strategy 简历逐行解释 V2

日期：2026-05-16  
版本：`payment_risk_strategy_resume`  
目标岗位：Payment Risk Strategy / Fraud Analytics / Risk Decision Science / Marketplace Integrity DS

## 总体改写逻辑

这一版的核心不是把你硬写成“已经做过 card fraud / chargeback 的人”，而是把你塑造成更强的 payment risk strategy candidate：

1. Goldman Sachs 证明你能做 production-grade risk metric design，而不只是 dashboard monitoring。
2. Blinkle AI 证明你能构建 scoring features、ranking decision signals，并理解 precision / conversion / friction tradeoff。
3. ARB Interactive 证明你有 Payments 场景、abnormal behavior detection、abuse proxy monitoring、policy intervention 和 causal/A/B evaluation。

所以故事线是：你一直在做“在高噪音、高成本、高不确定性的系统里，设计指标、识别异常、构建 scoring/threshold logic，并把结果转化成可解释、可治理、可上线的业务决策”。

## Header

### `Yihan Li`

保留原始姓名，简洁、ATS 友好。

### `yihanli0829@gmail.com | 310-689-8174 | Los Angeles, CA 90024`

保留原始联系方式。Los Angeles 对加州岗位是正向信号，因为目标是回加州做大厂/fintech DS。

## Summary

### `Data Scientist focused on risk decisioning, payment-adjacent analytics, marketplace experimentation, and production-grade metric design.`

这版去掉了 `Target Summary` 标题，也去掉了 `Quant Strategist`。原因是简历顶部最重要的是告诉 recruiter 你要去哪里，而不是重复你现在的 title。

关键词逻辑：

- `risk decisioning`：对应 PayPal / Uber / Block / Ramp / DoorDash 风控策略类 JD。
- `payment-adjacent analytics`：承接 ARB 的 Payments title，但不夸大成直接 chargeback ownership。
- `marketplace experimentation`：承接 Blinkle + ARB，也适合 Uber/DoorDash/Airbnb 这类 marketplace risk。
- `production-grade metric design`：回应你说的重点，你是 quant，不只是 monitor existing metrics，而是能在新业务场景下构建 metrics。

### `Experienced in SQL/Python analysis over large-scale event and transaction-level data, causal inference, backtesting, anomaly detection, scoring logic, and translating ambiguous risk signals into product, operations, and governance decisions.`

这一句是整份简历的 thesis。

新增 `scoring logic` 是为了把 Blinkle 的 ranking/scoring、Goldman 的 risk signal、ARB 的 abnormal behavior 统一到 payment risk 的语言里。  
`product, operations, and governance decisions` 则覆盖三类目标岗位：product/risk strategy、risk ops、金融科技治理/合规。

## Goldman Sachs

### Bullet 1

`Design and own production risk metrics across transaction- and entity-level pricing/liquidity signals for 100+ global entities, defining new diagnostic indicators for evolving business scenarios and analyzing billions of records to detect anomalies, quantify risk shifts, and trigger drill-down investigations.`

这是 v2 里最重要的修正：从 `own monitoring analytics` 改成 `design and own production risk metrics`。

改写理由：

- 体现 quant 能力：不是只看指标，而是设计指标。
- `defining new diagnostic indicators for evolving business scenarios` 表示你能根据新业务场景构建新的 metric / risk signal。
- `transaction- and entity-level`、`100+ global entities`、`billions of records` 保留原始强事实。
- `detect anomalies / quantify risk shifts / trigger investigations` 对应 payment risk 里的 anomaly detection 和 investigation workflow。

### Bullet 2

`Build root-cause decomposition frameworks for abnormal movements in ratio-based risk indicators, separating pricing, funding, balance-sheet, and regional drivers from noisy market moves across multi-billion-record datasets and cross-region cohorts.`

这条强化 root-cause analysis。  

Payment risk 面试里常见问题是：fraud rate / approval rate / dispute rate 变了，到底是 attack pattern 变了、用户 mix 变了、产品策略变了，还是数据问题？这条说明你会把异常拆成 drivers，而不是只报告指标变化。

### Bullet 3

`Apply difference-in-differences and historical backtesting to evaluate policy and market changes, balancing missed-risk vs false-escalation costs and improving confidence in risk-control decisions before stakeholder review.`

这条把 DID/backtesting 写成 risk policy evaluation。

`missed-risk vs false-positive escalation costs` 是对 Type I/II error、false positive / false negative、loss function 思路的简历化表达。这里直接保留 `false-positive` 原词，用来匹配 JD，同时不写得像教科书。招聘方会读懂：你知道风险系统不是只追 accuracy，而是要平衡漏报风险和误报成本。

### Bullet 4

`Develop thresholding and investigation-prioritization logic for risk indicators, translating continuous signal movements into actionable review paths and post-rollout monitoring routines for senior stakeholders while reducing low-signal investigation noise.`

这条是为了把 `manual review queue ownership` 这个 JD 关键词转化成你能合理承接的语言。

我没有写你 owned manual review queue，因为那可能太硬；但写了：

- `thresholding`
- `investigation-prioritization logic`
- `actionable review paths`
- `post-rollout monitoring routines`
- `reducing low-signal investigation noise`

这些能对应 fraud/risk team 的 review prioritization、alert triage、false-positive reduction。

### Bullet 5

`Build AI-assisted analytical validation workflows with source traceability, edge-case checks, explainability review, and human-in-the-loop controls, ensuring model-driven insights are auditable, reliable, and governance-ready in high-stakes contexts.`

这条把 AI 使用写得更深入，而不是简单说 “used AI”。

关键词逻辑：

- `source traceability`：AI 输出要能追溯来源。
- `edge-case checks`：处理异常/边界案例，适合 risk 系统。
- `explainability review`：金融/fintech 风控很看重可解释性。
- `human-in-the-loop controls`：说明你知道 AI 不能黑箱自动决策。
- `auditable / governance-ready`：对 Goldman、PayPal、Affirm、Ramp、Capital One 这类环境都有价值。

## Blinkle AI

### Bullet 1

`Designed the core risk and quality metrics framework for a two-sided job marketplace, defining north-star and diagnostic metrics across match quality, recommendation quality, suspicious behavior, and application conversion.`

这条保留 v1 逻辑，写得已经比较稳。  

`two-sided marketplace` 是 Uber/DoorDash/Airbnb 类岗位的桥。  
`risk and quality metrics framework` 把它从普通 product analytics 提升为 marketplace integrity / risk-quality analytics。

### Bullet 2

`Analyzed millions of production user events with SQL and Python to identify low-quality or suspicious behavior patterns that degraded matching quality, surfacing high-risk cohorts and downstream product friction points.`

这条强调 SQL/Python + production events + suspicious behavior。  

虽然不是 payment fraud，但它能自然迁移到 fraud/risk DS：识别坏行为模式、定位高风险 cohort、理解对好用户的 friction。

### Bullet 3

`Built LLM-derived scoring features from resume and job-description signals for screening/ranking pipelines, improving top-match accuracy by 37% and creating structured decision signals for product and review workflows.`

这条是对 `real-time scoring model deployment` 的可迁移写法。

我没有直接写 real-time payment scoring，因为那不真实；但写了：

- `scoring features`
- `screening/ranking pipelines`
- `structured decision signals`
- `product and review workflows`

这足够让 risk DS recruiter 看到 scoring / decisioning 能力，也方便之后面试解释成“我做过 scoring logic，只是场景不是 card transaction”。

### Bullet 4

`Designed holdout and A/B experiments for screening and ranking interventions, quantifying false-match vs missed-match tradeoffs, precision-conversion-friction effects, and increasing application conversion by 41%.`

这条加入了 `false-match vs missed-match tradeoffs`。

这是 payment risk 里 false positive / false negative 的 marketplace 版本：

- false match：把不好的匹配/候选通过了。
- missed match：把好的候选漏掉了。
- precision-conversion-friction：对应 fraud prevention vs good-user experience。

这样写比直接说 Type I/II error 更成熟，也更 product/risk。

## ARB Interactive

### Bullet 1

`Analyzed hundreds of millions of payment-adjacent interaction events from a 2.1M-user live-streaming platform to detect abnormal traffic, creator abuse, and high-risk behavioral cohorts, supporting fraud/abuse proxy monitoring and traffic-control interventions.`

这条是 ARB 的核心 payment/risk anchor。

v2 加入 `fraud/abuse proxy monitoring`，原因是你可以不直接 claim fraud loss/chargeback，但可以把 abnormal traffic、creator abuse、high-risk cohort 合理写成 fraud/abuse proxy。  

这比 “traffic analysis” 更强，也比 “chargeback reduction” 更安全。

### Bullet 2

`Developed a creator-level causal impact framework using counterfactual baselines and retention modeling to estimate incremental ROI of incentive and intervention policies, improving policy ROI by 18%.`

这条对应 risk strategy 里的 policy evaluation。  

`counterfactual baselines` 和 `incremental ROI` 说明你能回答“这个 intervention 到底有没有带来真实增量”，这对 fraud/risk rule launch 很重要。

### Bullet 3

`Built behavioral segmentation models with K-Means clustering to identify heterogeneous response and risk patterns, enabling targeted interventions that increased DAU by 12% while reducing broad, unnecessary user friction.`

这条把 segmentation 写成 risk-aware targeting。

关键词：

- `risk patterns`
- `targeted interventions`
- `reducing broad, unnecessary user friction`

这正好对应 payment risk 的核心 tradeoff：不能为了风险控制把好用户都误伤。

### Bullet 4

`Designed, analyzed, and monitored A/B-tested policy interventions after rollout, measuring impact on creator retention, content quality, platform health, and the tradeoff between abuse prevention and user experience.`

这条作为 ARB 的收束：你能设计 intervention，也能在 rollout 后持续监控效果，并衡量 abuse prevention 和 user experience 的 tradeoff。  

面试里可以把它讲成：如何定义 guardrail metrics，如何避免 intervention 伤害好用户，如何判断策略是否上线。

## Education

### `University of California, Los Angeles | Master of Quantitative Economics | Jul 2025`

保留 UCLA 和 MQE，给 DS/risk/stats 可信度。

### `GPA: 4.00/4.00 | Coursework: Database Management, Machine Learning, Time Series Forecasting, Optimization Methods`

课程选择服务于目标岗位：

- Database Management：SQL/data infra。
- Machine Learning：建模。
- Time Series Forecasting：监控/趋势。
- Optimization Methods：threshold、resource allocation、risk-return tradeoff。

### `Open For Good Project: Used Qualtrics surveys and RNN models to quantify sentiment in sustainability disclosures.`

保留但压缩。它不是 payment risk 主线，但能补 NLP / RNN / text modeling 的宽度。

### `Nanjing University | Bachelor of Economics, Minor in Mathematics | Jul 2023`

保留经济和数学背景，支撑 quant / statistics / risk reasoning。

### `Honors: National Scholarship, Top 1%; First Place, Citi Group Fintech Competition.`

保留 Citi Fintech Competition，因为它对 fintech/risk/payment 方向是一个正向信号。

## Technical Skills

### `Risk & Analytics`

v2 里新增/强化：

- `Risk Scoring`
- `Thresholding`
- `Fraud/Abuse Monitoring`

这回应了 JD 里的 scoring、rules、manual review、fraud/risk language，但仍然保持在你经历能支撑的范围内。

### `Machine Learning`

v2 加入 `Explainability`。  

原因是 Goldman 的 AI validation / governance bullet 需要技能区呼应，而且 fintech risk 很看重可解释性。

### `Tools`

保留 Python、SQL、R、Spark、Airflow、AWS、Tableau、Stata 和常用 Python DS stack。  
SQL/Python 在经历和技能里都出现，是为了 ATS 和 recruiter 快速扫描。

## 对那些敏感关键词的处理方式

用户提到的词里，有些可以直接或间接放进来，有些暂时不建议硬写。

已经通过可解释方式加入：

- `manual review queue ownership` → 写成 `investigation-prioritization logic`、`actionable review paths`、`review workflows`。
- `real-time payment scoring model deployment` → 写成 `scoring features`、`screening/ranking pipelines`、`structured decision signals`。
- `fraud loss reduction` → 写成 `missed-risk vs false-escalation costs`、`fraud/abuse proxy monitoring`、`policy ROI`。
- `account takeover / synthetic identity detection` 的底层能力 → 写成 `abnormal traffic`、`creator abuse`、`high-risk behavioral cohorts`、`anomaly detection`、`risk scoring`。

暂时没有直接硬写：

- `chargeback reduction`
- `account takeover detection`
- `synthetic identity detection`
- `real-time payment scoring model deployment`

原因是这些词在面试里会被追问具体系统、标签、交易流、review queue、model serving、post-launch monitoring。如果没有真实项目支撑，直接写会有风险。更好的打法是：这一版简历先用强转化语言打 risk strategy / fraud analytics；下一步用 Payment Fraud Decisioning Simulator 项目补齐这些硬词，然后第二版 fraud ML 简历就可以更大胆。
