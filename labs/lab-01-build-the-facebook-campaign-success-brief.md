# Lab 1 — Build the Facebook Campaign Success Brief

- **Course:** Agentic AI for Facebook Marketing (C526)
- **Topic 1:** Getting Started with Agentic AI for Facebook Marketing
- **Maps to:** LO1: Connect a Facebook marketing workflow to a measurable business objective, customer action, KPI, and guardrails
- **Tools:** Web browser, approved generative AI assistant, text editor, labs/resources/harbour-hearth-brand-brief.md
- **Duration:** 50 minutes

---

## What You Will Do

You begin the connected Harbour & Hearth scenario by turning an approved brand brief into a concise success brief of no more than 600 words. The lab establishes the objective, customer action, evidence, limits, and decision metrics that every later content, campaign, and automation artifact must follow.

## What You Will Build

C526-campaign-pack/01-success-brief.md of no more than 600 words containing the campaign decision chain, approved facts, KPI definitions, guardrails, stop conditions, and retained Test Evidence.

## Prerequisites

- Create a local folder named C526-campaign-pack.
- Open labs/resources/harbour-hearth-brand-brief.md in a text editor.
- Use a new AI chat that contains no real customer or account data.

> **Data note.** Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

## Steps

**1. Create the campaign-pack folder. Inside it, create a blank text file named 01-success-brief.md.**

```text
Folder: C526-campaign-pack
File: C526-campaign-pack/01-success-brief.md
```

**2. Read the Harbour & Hearth brand brief once without using AI. Highlight the offer, approved facts, target action, constraints, and facts that are explicitly unknown.**

```text
Open: labs/resources/harbour-hearth-brand-brief.md
```

**3. Start a new AI chat. Paste the prompt below, then paste the complete synthetic brand brief where indicated.**

```text
You are a Facebook marketing strategist preparing a decision brief. Use only facts in the supplied synthetic brand brief. Do not invent audience statistics, product claims, customer quotes, or performance. Label missing information as UNKNOWN.

Return Markdown with these headings:
1. Business result
2. Facebook marketing objective
3. Observable customer action
4. Primary KPI and formula
5. Two guardrail metrics
6. Approved offer facts
7. Audience problem hypothesis
8. Organic and paid channel roles
9. Human approval gates
10. Stop conditions
11. Unknowns to resolve

For every factual statement, add its source heading from the brief in parentheses.

SYNTHETIC BRAND BRIEF:
<PASTE THE COMPLETE HARBOUR & HEARTH BRAND BRIEF>
```

**4. Compare the AI output line by line with the brand brief. Delete or relabel every statement that cannot be traced to a source heading.**

```text
Reviewer rule: sourced fact / labelled assumption / UNKNOWN — there is no fourth category.
```

**5. Write the decision chain as one sentence and place it at the top of the file.**

```text
Because <BUSINESS RESULT>, Facebook will pursue <OBJECTIVE> by encouraging <CUSTOMER ACTION>; we will judge it mainly by <PRIMARY KPI> while protecting <GUARDRAIL 1> and <GUARDRAIL 2>.
```

**6. Add the primary KPI formula and two named guardrails. Use cost per purchase as the primary efficiency KPI, return on ad spend as value context, negative feedback rate as the customer-impact guard, and fulfilment headroom as the operating guard.**

```text
Cost per purchase = advertising spend / attributed purchases
Return on ad spend = attributed revenue / advertising spend
Negative feedback rate (%) = negative feedback / impressions × 100
Fulfilment headroom = daily box capacity - forecast daily boxes
Pause threshold for practice: negative feedback rate > 0.03% or fulfilment headroom < 0
```

**7. Add at least three stop conditions: missing or broken conversion data, an unsupported claim, and any action that would publish or spend without approval.**

```text
STOP when: tracking is missing or inconsistent; a claim has no approved source; the next action publishes, messages, changes targeting, or changes spend without the named approver.
```

**8. Paste the reviewed output into 01-success-brief.md. Add a final Review Log with your initials, today's date, and the corrections you made.**

```text
## Review Log
- Reviewer: <INITIALS>
- Date: <YYYY-MM-DD>
- Corrections: <LIST THE FACTS, ASSUMPTIONS, OR WORDING YOU CHANGED>
```

**9. Check the document word count. If it exceeds 600 words, remove repetition while preserving every required heading, definition, guardrail, unknown, and source reference.**

```text
Length limit: 600 words maximum
```

## Test It

Open 01-success-brief.md and confirm it contains one measurable customer action, a primary KPI with formula, two guardrail metrics, at least three stop conditions, and an UNKNOWN section. Choose any three offer facts at random; each must trace to a heading in the synthetic brand brief.

## Test Evidence

Save a Test Evidence row with the input or case, expected result, observed result, status, reviewer initials, and date. Use status VERIFIED or REVISE; do not rely on memory.

| Input or case | Expected result | Observed result | Status | Reviewer | Date |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Checkpoint for the Next Lab

Keep 01-success-brief.md open. Lab 2 will use its objective, approved facts, guardrails, and unknowns as authoritative inputs.

## Troubleshooting

- **The AI invents customer demographics or market size:** Delete the claim, add it to UNKNOWN, and repeat the instruction to use only supplied evidence.
- **The objective and KPI do not match:** Rewrite the chain from the customer action backwards; a purchase action needs a purchase-related decision metric.
- **The brief exceeds 600 words:** Move supporting explanation into notes and keep only decisions, definitions, constraints, and unknowns in the main brief.

## Challenge

Add one leading indicator and one lagging indicator, then explain what decision each can support without replacing the primary KPI.

## Reflection

Which part of the decision chain most needs human business judgement, and why would an AI model be unable to supply it safely from the brief alone?

---

[← Labs index](README.md) · [Lab 2 →](lab-02-create-the-audience-evidence-map-and-prompt-contract.md)
