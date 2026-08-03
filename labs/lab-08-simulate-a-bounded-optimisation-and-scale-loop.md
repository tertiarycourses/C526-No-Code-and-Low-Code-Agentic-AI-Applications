# Lab 8 — Simulate a Bounded Optimisation and Scale Loop

- **Course:** Agentic AI for Facebook Marketing (C526)
- **Topic 4:** Automating and Scaling Facebook Marketing with AI Agents
- **Maps to:** LO6 and LO5: Apply performance, operational, privacy, and customer-impact limits to a human-governed scaling decision
- **Tools:** Approved generative AI assistant, spreadsheet or text editor, scale scenarios, bounded-policy template, Labs 1-7 outputs
- **Duration:** 65 minutes

---

## What You Will Do

You complete the course by converting all prior guardrails into a bounded optimisation policy, then run synthetic scenarios through an agent that may recommend but cannot execute. The final campaign operations pack shows when to hold, pause, investigate, or propose a small scale step and records the evidence behind each decision.

## What You Will Build

C526-campaign-pack/08-bounded-scale-policy.md plus a final manifest linking all eight campaign-pack checkpoints, owners, approvals, stop conditions, and rollback evidence.

## Prerequisites

- Completed all Labs 1-7; this lab reuses the success brief, prompt contract, performance diagnosis, and operations runbook.
- Open labs/resources/harbour-hearth-scale-scenarios.csv and bounded-scale-policy-template.md.
- Use only synthetic scenarios and hypothetical budget values.
- The workflow may recommend actions but may not change a real campaign or send a message.

> **Data note.** Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

## Steps

**1. Open bounded-scale-policy-template.md and save a copy as 08-bounded-scale-policy.md. Fill its primary KPI, guardrail metrics, stop rule, permission table, and human roles from Labs 1, 6, and 7.**

```text
Template: labs/resources/bounded-scale-policy-template.md
Save as: C526-campaign-pack/08-bounded-scale-policy.md
Inputs: 01-success-brief.md | 02-audience-and-prompt-contract.md | 06-performance-diagnosis.md | 07-operations-agent-runbook.md
```

**2. Write the policy with six blocks: eligibility, allowed recommendations, maximum change, cooldown, stop or pause conditions, and approval plus log requirements.**

```text
## Bounded Optimisation Policy
Eligibility: same metric definitions; complete 7-day window; event status healthy; minimum 10 purchases; no unresolved data-quality issue.
Allowed recommendations: HOLD, PAUSE, INVESTIGATE, PROPOSE CREATIVE TEST, PROPOSE BUDGET CHANGE.
Maximum budget recommendation: +15% or -15% per decision cycle.
Cooldown: 72 hours after a material change before another scale recommendation.
Stop or pause: tracking error; unsupported claim; privacy concern; negative feedback rate above 0.03%; fulfilment capacity below forecast demand; negative margin context; missing approver.
Approval and log: named marketing owner approves; record before/after value, evidence, reason, timestamp, expected result, rollback action.
```

**3. Open harbour-hearth-scale-scenarios.csv and read the column definitions. Confirm that Metric_Definition_Version matches the approved version, Event_Status is healthy, and Unresolved_Data_Quality_Issue is no before treating a row as eligible. Keep every row unchanged so classmates work from the same evidence.**

```text
Open: labs/resources/harbour-hearth-scale-scenarios.csv
Eligibility evidence: Metric_Definition_Version = v1 | Event_Status = healthy | Unresolved_Data_Quality_Issue = no
```

**4. Paste the G-C-A-T-E contract, bounded policy, and scenario table into the AI assistant. Make its authority recommendation-only.**

```text
You are a recommendation-only Facebook campaign operations agent. Apply the bounded policy to each synthetic scenario independently.

Return columns:
scenario_id | eligible_yes_no | evidence | guardrail_status | recommendation | proposed_change | human_approval_needed | cooldown_end | rollback_trigger | log_note

Decision order:
1. Validate data and eligibility.
2. Apply privacy, advertising, customer-impact, capacity, and tracking stop rules.
3. Review the primary KPI and value context.
4. Apply the cooldown: when As_Of_Datetime is earlier than Last_Change_Datetime + 72 hours, choose HOLD and make no budget proposal.
5. Choose only one allowed recommendation and cap any budget proposal at 15%.

Never execute a change. When evidence conflicts or is missing, choose INVESTIGATE or HOLD and name the missing evidence.
```

**5. Check the scenario decisions against policy invariants. A tracking error, privacy concern, unsupported claim, negative feedback rate above 0.03%, negative margin context, or capacity shortfall must prevent scaling even when ROAS is strong. A cooldown violation is also decisive: when As_Of_Datetime is earlier than Last_Change_Datetime + 72 hours, the recommendation must be HOLD with no budget proposal. Use SC06 to verify this rule.**

```text
Invariant check columns: Scenario | Trigger present | Required policy effect | Agent effect | Corrected decision
SC06 expected effect: HOLD | Proposed change: none
```

**6. For any incorrect agent decision, identify whether the failure came from missing input, ambiguous policy, wrong calculation, or instruction order. Revise the policy or prompt and rerun only that scenario.**

```text
Correction log: Scenario | Failure type | Evidence | Rule change | New recommendation
```

**7. Choose one eligible healthy scenario and write a human Decision Note. Calculate the proposed daily budget from Current_Daily_Budget_SGD, calculate Cooldown_End from Last_Change_Datetime + 72 hours, and include expected effect, capacity check, guardrails, approver, and rollback trigger.**

```text
Status must remain PROPOSED — AWAITING HUMAN APPROVAL.
```

**8. Create the final campaign-pack manifest. List each numbered artifact, its purpose, authoritative inputs, owner, current status, last review date, and next decision it supports.**

```text
Manifest columns: Artifact | Purpose | Authoritative inputs | Owner | Status | Last review | Next decision
```

**9. Add a 30-day draft-first pilot plan with weekly checkpoints for content quality, metric integrity, response exceptions, customer impact, and policy changes. Keep all public or financial actions under the named owners.**

```text
Week 1: baseline and draft quality
Week 2: exception and correction labels
Week 3: one controlled experiment
Week 4: governance review and authority decision
```

**10. Save 08-bounded-scale-policy.md and confirm the C526-campaign-pack folder contains artifacts 01 through 08, the two Lab 4 image-evidence files, and the metric workbook.**

```text
Final folder: C526-campaign-pack/
Required numbered files: 01, 02, 03, 04, 05, 06, 07, 08
Evidence: 04-control-image-1080.png | 04-phone-preview-360.png | 06-facebook-metrics.xlsx
```

## Test It

Run four invariants: Tracking_Error = yes must block scaling; Negative_Feedback_Rate_Pct > 0.03 must block scaling; a proposed budget change must be no greater than 15%; and As_Of_Datetime earlier than Last_Change_Datetime + 72 hours must produce HOLD with no budget proposal. Record SC06 as the cooldown Test Evidence row. Finally, trace the selected scale recommendation back to its metric row, policy rule, human owner, and rollback trigger.

## Test Evidence

Save a Test Evidence row with the input or case, expected result, observed result, status, reviewer initials, and date. Use status VERIFIED or REVISE; do not rely on memory.

| Input or case | Expected result | Observed result | Status | Reviewer | Date |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Checkpoint for the Next Lab

The completed C526-campaign-pack is your reusable implementation model. Replace synthetic inputs only after your organisation authorises the data, owners, platform access, and operating limits.

## Troubleshooting

- **The agent scales whenever ROAS is high:** Move stop conditions before performance evaluation and require guardrail status to be clear before any scale recommendation.
- **The proposed change exceeds 15%:** Add a deterministic cap calculation and reject any recommendation whose absolute percentage is greater than 15.
- **The policy contains vague terms such as 'enough data':** Replace them with a named window, minimum event count, data-quality condition, owner, and exception path.

## Challenge

Design a second authority level that may automatically pause on a verified tracking outage but still cannot resume or change budget without a person; explain why pause and resume have different risk.

## Reflection

What evidence would you require before increasing this workflow's autonomy beyond recommendation-only mode?

---

[← Lab 7](lab-07-design-the-facebook-operations-agent-runbook.md) · [Labs index →](README.md)
