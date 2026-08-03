# Lab 3 — Build a Seven-Day Facebook Content System

- **Course:** Agentic AI for Facebook Marketing (C526)
- **Topic 2:** Content Creation and Ad Copy with AI
- **Maps to:** LO3: Produce a journey-aligned Facebook content calendar and post set from approved facts, audience evidence, and brand rules
- **Tools:** Approved generative AI assistant, text editor or spreadsheet, Lab 1 and Lab 2 files
- **Duration:** 45 minutes

---

## What You Will Do

You use the success brief, selected audience, and prompt contract to design a seven-day Facebook calendar that balances teaching, proof, invitation, and learning. You then turn the selected Invite entry into one publication-ready control post while keeping every fact traceable.

## What You Will Build

C526-campaign-pack/03-content-system.md containing four content pillars, a seven-day calendar, one complete control post, a quality gate, a reviewer correction log, and retained Test Evidence.

## Prerequisites

- Completed 01-success-brief.md and 02-audience-and-prompt-contract.md.
- Selected one primary audience hypothesis in Lab 2.
- No confidential brand assets or real customer comments are used.

> **Data note.** Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

## Steps

**1. Create 03-content-system.md. At the top, paste the final decision chain and the selected audience hypothesis from Labs 1 and 2.**

```text
File: C526-campaign-pack/03-content-system.md
Inputs: 01-success-brief.md + selected audience hypothesis from 02-audience-and-prompt-contract.md
```

**2. Define four content pillars named Teach, Show, Prove, and Invite. For each, write its customer-journey job, allowed evidence, suitable formats, and the action it may request.**

```text
Table columns: Pillar | Journey job | Allowed evidence | Suitable formats | Allowed customer action
```

**3. Start a fresh AI chat. Paste the G-C-A-T-E contract, the success brief, selected audience hypothesis, and the four-pillar table. Then request the calendar.**

```text
Create a seven-day Facebook organic content calendar for the synthetic Harbour & Hearth Sunrise Breakfast Box.

Return exactly seven rows with columns:
Day | Journey job | Pillar | Format | Hook | Approved evidence used | Main value | Call to action | Learning question | Human review focus

Constraints:
- Use Teach, Show, Prove, and Invite; include each at least once.
- Use at least three formats across single image, carousel, and short video.
- Keep one main message and one customer action per row.
- Cite the exact source heading or signal ID for every evidence claim.
- Do not invent a price, promotion, testimonial, customer count, health claim, or scarcity.
- The learning question must name the metric or feedback signal that could improve the next content cycle.
```

**4. Review the seven rows as one system. Confirm all four pillars appear, no two consecutive rows do the same journey job, and the Invite posts do not outnumber the combined Teach and Prove posts.**

```text
Calendar balance check: all 4 pillars present; at least 3 formats; one CTA per row; every row has an evidence reference and learning question.
```

**5. Choose one Invite row as the paid-message control for Lab 4. Ask the AI to draft that one complete post using the output schema below.**

```text
For the selected Invite calendar row, return:
POST ID
PURPOSE: one sentence
PRIMARY TEXT: 60-110 words, warm and direct
ON-CREATIVE TEXT: maximum 8 words
CALL TO ACTION: one action
CREATIVE BRIEF: subject, setting, composition, proof detail, mobile-readability note
EVIDENCE USED: exact source heading or signal ID
REVIEW FLAGS: factual, brand, rights, privacy, or advertising concerns

Use Singapore English naturally without forced slang. One helpful detail must appear before the invitation.
```

**6. Apply the Content Quality Gate to the control draft. Mark Grounded facts, Brand fit, Audience value, Creative and rights check, and Objective-action match as OK or REVISE, with one sentence of evidence.**

```text
Quality Gate columns: Post ID | Grounded facts | Brand fit | Audience value | Creative and rights | Objective-action match | Reviewer decision
```

**7. Revise every REVISE item yourself or with a focused follow-up prompt. Do not ask for a total rewrite when one sentence is the problem.**

```text
Focused revision prompt: Revise only <NAMED ELEMENT>. Preserve every approved fact, the selected audience need, the format, and the single call to action. Explain the change in one sentence.
```

**8. Save the final calendar, control post, quality gate, and a Correction Log listing what the AI got wrong and what instruction would prevent the same issue.**

```text
## Correction Log
| Post ID | Problem label | Exact correction | Prompt rule to add next time |
```

## Test It

Pick one calendar row and trace its audience need to the Lab 2 hypothesis, its claim to an approved source, its action to the Lab 1 customer action, and its learning question to a named signal. The chain must be complete without relying on an invented fact.

## Test Evidence

Save a Test Evidence row with the input or case, expected result, observed result, status, reviewer initials, and date. Use status VERIFIED or REVISE; do not rely on memory.

| Input or case | Expected result | Observed result | Status | Reviewer | Date |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Checkpoint for the Next Lab

Lab 4 will use the final Invite post and its learning question as the control message for paid creative variants.

## Troubleshooting

- **The calendar is seven versions of the same offer:** Reassert the journey job and require different Teach, Show, Prove, and Invite value before changing formats.
- **The captions sound generic:** Paste the operational brand rules and ask for one specific approved detail before the call to action.
- **Evidence citations disappear during revision:** Require the source column to remain unchanged and reject any new claim without a source heading or signal ID.

## Challenge

Draft one Teach post and one Prove post from the calendar, then add a community-engagement question that invites a useful response without collecting personal data.

## Reflection

Which calendar field makes the system learn over time instead of becoming a faster content factory?

---

[← Lab 2](lab-02-create-the-audience-evidence-map-and-prompt-contract.md) · [Lab 4 →](lab-04-create-the-ad-copy-and-creative-matrix.md)
