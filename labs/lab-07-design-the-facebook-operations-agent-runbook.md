# Lab 7 — Design the Facebook Operations Agent Runbook

- **Course:** Agentic AI for Facebook Marketing (C526)
- **Topic 4:** Automating and Scaling Facebook Marketing with AI Agents
- **Maps to:** LO6: Design a governed workflow for content scheduling, routine responses, escalation, and evidence-linked reporting
- **Tools:** Approved generative AI assistant, text editor or spreadsheet, brand brief, message scenarios, runbook template, optional Meta Business Suite view
- **Duration:** 60 minutes

---

## What You Will Do

You design a draft-first operations workflow that coordinates approved Facebook content, Meta Business Suite surfaces, routine Inbox responses, and a weekly report. You then simulate message triage on synthetic scenarios so routine questions and human-escalation cases follow different paths.

## What You Will Build

C526-campaign-pack/07-operations-agent-runbook.md containing the workflow map, permission table, response bank, triage results, scheduling checklist, weekly report schema, and retained Test Evidence.

## Prerequisites

- Completed Labs 1-6 and have the content calendar, prompt contract, and metric definitions available.
- Open labs/resources/harbour-hearth-brand-brief.md, harbour-hearth-message-scenarios.csv, and operations-runbook-template.md.
- Do not use real messages, names, phone numbers, email addresses, or order details.
- Any Meta Business Suite activity remains in draft or view-only mode unless an authorised Page owner separately approves it.

> **Data note.** Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

## Steps

**1. Open operations-runbook-template.md and save a copy as 07-operations-agent-runbook.md. Keep its four workflow lanes: Content Planning, Scheduling, Inbox Triage, and Weekly Reporting.**

```text
Template: labs/resources/operations-runbook-template.md
Save as: C526-campaign-pack/07-operations-agent-runbook.md
```

**2. For each lane, complete the operating-loop fields: trigger, authorised inputs, agent task, tool or surface, validation, human approval, action, log evidence, and stop or escalation path.**

```text
Runbook columns: Lane | Trigger | Inputs | Agent task | Tool/surface | Validation | Approval | Action | Log | Stop/escalation
```

**3. Create a permission table for reading course files, drafting content, preparing a schedule, publishing a post, drafting a reply, sending a reply, reading aggregate insights, changing targeting, and changing budget.**

```text
Permission columns: Action | Risk level | Reversible? | Allowed in this workflow | Human role required | Evidence to log
```

**4. Set this lab's authority: the agent may read synthetic files, draft content, classify synthetic messages, and prepare recommendations. Publishing, sending messages, changing targeting, and changing spend are blocked behind a person.**

```text
Allowed: read synthetic inputs; draft; classify; calculate; recommend
Blocked: publish; send; change targeting; change budget; upload customer lists
```

**5. Build an approved routine-response bank for the collection window, product information, ordering link, delivery-area unknown, and order-specific help. General opening hours remain UNKNOWN. Use only the brand brief; route order-specific and personal-data cases to a person.**

```text
Response bank columns: Intent | Approved reply | Source | Prohibited additions | Escalation condition | Owner
Do not broaden the approved 7:30-11:00 collection window into general opening hours.
```

**6. Open the synthetic message-scenarios CSV. Paste it, the response bank, and the G-C-A-T-E contract into the AI assistant. Ask for triage only, not message sending.**

```text
Classify each synthetic Facebook message scenario.

Return columns:
scenario_id | intent | routine_or_human | approved_response_id | draft_reply_or_handoff_note | risk_reason | log_fields

Rules:
- Use only the approved response bank and brand brief.
- Routine replies may give approved public information.
- Escalate complaints, refunds, safety concerns, legal threats, account issues, order-specific cases, and any personal data.
- Never request or repeat personal data in the draft.
- Do not send anything; output is for human review.
```

**7. Review the triage table. Any scenario containing an order number, contact detail, complaint, safety concern, refund request, or legal language must route to a person even if part of the question looks routine.**

```text
Triage invariant: higher-risk content overrides a routine keyword match.
```

**8. Write the scheduling checklist from the Lab 3 calendar. Include Page identity, content ID, approved asset, final copy, link, time zone, date and time, reviewer, status, and rollback owner.**

```text
Scheduling status values: DRAFT | READY FOR HUMAN REVIEW | APPROVED TO SCHEDULE | SCHEDULED | PAUSED
```

**9. Optional view-only practice: In Meta Business Suite, open Planner and locate the Create post and scheduling controls described by the trainer. Do not schedule or publish. Record any interface difference in the runbook so the owner can verify the current path.**

```text
Reference path: Facebook Page → Meta Business Suite → Create post / Planner → Scheduling options
Action in this lab: view only; close without saving or scheduling.
```

**10. Create the weekly report schema. Every finding must name the date window, source, metric definition, comparison, evidence row, limitation, and recommended next action with owner.**

```text
Report sections: Objective status | Content delivered | Metric movement | Audience feedback themes | Risks and exceptions | One next experiment | Decisions needed
```

**11. Save the completed runbook with a Change Log for response-bank updates, workflow exceptions, and owner decisions.**

```text
## Change Log
| Date | Workflow or response ID | Evidence | Change | Owner | Review date |
```

## Test It

Use M01 as the routine case and M06 as the escalation case. M01 must cite the approved collection window; M06 must contain a handoff note without repeating the phone number. Also confirm every high-impact action in the permission table names a human role.

## Test Evidence

Save a Test Evidence row with the input or case, expected result, observed result, status, reviewer initials, and date. Use status VERIFIED or REVISE; do not rely on memory.

| Input or case | Expected result | Observed result | Status | Reviewer | Date |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Checkpoint for the Next Lab

Lab 8 will reuse the permission table, report evidence rules, human roles, stop paths, and change log as the foundation of a bounded scale policy.

## Troubleshooting

- **The agent treats every message as routine:** Move the override risks above keyword rules and require risk classification before response selection.
- **The runbook says 'review as needed':** Name the exact check, human role, evidence, and status transition required at that point.
- **Scheduling instructions do not match the current interface:** Record the interface difference, use the current official Help path, and keep the action in view or draft mode.

## Challenge

Add a response-quality sampling plan that reviews a percentage of routine drafts each week and turns recurring corrections into response-bank changes.

## Reflection

Which operations step benefits most from deterministic rules, and which benefits most from contextual agent reasoning?

---

[← Lab 6](lab-06-diagnose-performance-and-design-one-controlled-test.md) · [Lab 8 →](lab-08-simulate-a-bounded-optimisation-and-scale-loop.md)
