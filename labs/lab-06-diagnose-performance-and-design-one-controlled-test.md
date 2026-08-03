# Lab 6 — Diagnose Performance and Design One Controlled Test

- **Course:** Agentic AI for Facebook Marketing (C526)
- **Topic 3:** Building and Optimising Ad Campaigns with AI
- **Maps to:** LO5: Calculate Facebook metrics, locate a funnel break, distinguish evidence from inference, and recommend one bounded experiment
- **Tools:** Spreadsheet application, approved generative AI assistant, labs/resources/harbour-hearth-facebook-performance.csv, Lab 5 blueprint
- **Duration:** 55 minutes

---

## What You Will Do

You calculate delivery, attention, conversion, and value metrics from a synthetic Facebook result table, then use an AI analyst under the prompt contract to diagnose the pattern. The lab finishes with one controlled next test rather than a bundle of untraceable changes.

## What You Will Build

C526-campaign-pack/06-performance-diagnosis.md plus 06-facebook-metrics.xlsx with date window, CTR, CPC, conversion rate, CPA, ROAS, negative feedback rate, evidence-linked findings, and one experiment card.

## Prerequisites

- Completed 05-campaign-blueprint.md with the hook-angle experiment defined.
- Open the synthetic performance CSV in a spreadsheet application.
- Use one consistent date window, currency, and click definition across all rows.

> **Data note.** Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

## Steps

**1. Open harbour-hearth-facebook-performance.csv. Confirm the columns include Variant, Window_Start, Window_End, Impressions, Reach, Link_Clicks, Purchases, Spend_SGD, Revenue_SGD, and Negative_Feedback.**

```text
Open: labs/resources/harbour-hearth-facebook-performance.csv
```

**2. Check data quality before calculating: no blank variant names, no negative counts, Reach is not greater than Impressions, Spend is positive, and Window_Start and Window_End are identical across rows and span seven days.**

```text
Data-quality log: Check | Result | Row affected | Action taken
```

**3. Add six columns after Negative_Feedback: Negative_Feedback_Rate, Link_CTR, CPC_SGD, Conversion_Rate, CPA_SGD, and ROAS. Enter the formulas in row 2 and fill them down.**

```text
K2 = IF(D2=0,"",J2/D2)
L2 = IF(D2=0,"",F2/D2)
M2 = IF(F2=0,"",H2/F2)
N2 = IF(F2=0,"",G2/F2)
O2 = IF(G2=0,"",H2/G2)
P2 = IF(H2=0,"",I2/H2)
```

**4. Format Negative_Feedback_Rate, Link_CTR, and Conversion_Rate as percentages; show Negative_Feedback_Rate to at least two decimal places so the 0.03% threshold remains observable. Format CPC_SGD and CPA_SGD as currency, and ROAS as a number with two decimal places. Do not replace unavailable values with zero.**

```text
Display rule: unavailable denominator → blank or N/A, never 0.00. Negative_Feedback_Rate display precision: at least 0.00%.
```

**5. Create 06-performance-diagnosis.md. Paste a rounded copy of the completed metric table and record the formulas in a Metric Definitions section.**

```text
File: C526-campaign-pack/06-performance-diagnosis.md
```

**6. Compare the three variants in funnel order: delivery, attention, conversion, value, then quality guard. Write one observed statement per stage without giving a cause yet.**

```text
Observed statement format: Variant <ID> has <METRIC VALUE> versus <COMPARATOR> during the same seven-day window.
```

**7. Paste the G-C-A-T-E contract, metric table, and fixed experiment controls into the AI assistant. Request evidence-linked diagnosis.**

```text
Act as a cautious Facebook performance analyst. Use only the supplied synthetic table and experiment design.

Return:
1. Five observed findings, each citing variant and metric value.
2. A funnel-break table with Stage | Evidence | Possible explanation | What the data does not prove.
3. Data limitations and checks required before action.
4. Exactly three ranked hypotheses.
5. One recommended next experiment that changes one variable.

Rules:
- Do not call correlation a cause.
- Do not declare a winner using CTR alone.
- Use N/A when a denominator is zero.
- Keep spend changes as a human decision.
- Mention Negative_Feedback as a quality guard, not a performance objective.
```

**8. Verify every number in the AI response against your spreadsheet. Correct arithmetic, renamed metrics, unsupported causes, or claims that ignore the primary KPI.**

```text
Verification table: AI claim | Spreadsheet evidence | Correct? | Correction
```

**9. Write one Experiment Card. State the question, hypothesis, single changed variable, controls, primary metric, guardrail, observation window, minimum evidence condition, decision threshold, stop rule, and owner.**

```text
## Experiment Card
Question:
Hypothesis:
Changed variable:
Fixed controls:
Primary metric:
Guardrail metric:
Observation window:
Minimum evidence condition:
Decision threshold:
Stop rule:
Human owner:
```

**10. Save the spreadsheet as C526-campaign-pack/06-facebook-metrics.xlsx and the diagnosis as 06-performance-diagnosis.md.**

```text
Files: C526-campaign-pack/06-facebook-metrics.xlsx
C526-campaign-pack/06-performance-diagnosis.md
```

## Test It

Manually recalculate one row and match the spreadsheet within rounding. Independent benchmark: Freshness_Process CPA = S$11.88 and ROAS = 2.36. Then verify the Experiment Card changes exactly one variable and names at least one condition that would stop or delay the decision.

## Test Evidence

Save a Test Evidence row with the input or case, expected result, observed result, status, reviewer initials, and date. Use status VERIFIED or REVISE; do not rely on memory.

| Input or case | Expected result | Observed result | Status | Reviewer | Date |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Checkpoint for the Next Lab

Lab 7 will use your metric definitions and evidence-linked reporting style; Lab 8 will use the selected guardrail and stop rule in a scaling policy.

## Troubleshooting

- **The spreadsheet shows a divide-by-zero error:** Use the IF denominator check exactly as shown and display N/A rather than inventing a metric.
- **The AI explains performance using facts not in the table:** Move the statement to Possible explanation and add the evidence needed to test it.
- **The next experiment changes copy, audience, and budget:** Choose the highest-priority hypothesis and change only the variable needed to test it.

## Challenge

Add frequency = impressions / reach, then describe one situation where a higher value might indicate useful repetition and another where it might indicate fatigue.

## Reflection

Why can the variant with the best click-through rate still be the wrong choice for the business objective?

---

[← Lab 5](lab-05-design-the-facebook-campaign-blueprint.md) · [Lab 7 →](lab-07-design-the-facebook-operations-agent-runbook.md)
