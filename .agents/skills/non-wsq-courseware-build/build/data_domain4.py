"""Topic 4 — Automating and Scaling Facebook Marketing with AI Agents."""

DOMAIN4 = [
    dict(
        num=7,
        topic=4,
        title="Design the Facebook Operations Agent Runbook",
        objective="LO6: Design a governed workflow for content scheduling, routine responses, escalation, and evidence-linked reporting",
        duration="60 minutes",
        desc=(
            "You design a draft-first operations workflow that coordinates approved Facebook content, Meta Business Suite surfaces, routine Inbox responses, and a weekly report. "
            "You then simulate message triage on synthetic scenarios so routine questions and human-escalation cases follow different paths."
        ),
        build="C526-campaign-pack/07-operations-agent-runbook.md containing the workflow map, permission table, response bank, triage results, scheduling checklist, weekly report schema, and retained Test Evidence.",
        services="Approved generative AI assistant, text editor or spreadsheet, brand brief, message scenarios, runbook template, optional Meta Business Suite view",
        prerequisites=[
            "Completed Labs 1-6 and have the content calendar, prompt contract, and metric definitions available.",
            "Open labs/resources/harbour-hearth-brand-brief.md, harbour-hearth-message-scenarios.csv, and operations-runbook-template.md.",
            "Do not use real messages, names, phone numbers, email addresses, or order details.",
            "Any Meta Business Suite activity remains in draft or view-only mode unless an authorised Page owner separately approves it.",
        ],
        deck_steps=[
            "Map triggers, inputs, tools, outputs, checks, approvals, logs, and stop paths.",
            "Separate low-risk drafting from high-impact publishing, messaging, and spend actions.",
            "Create an approved routine-response bank and simulate message triage.",
            "Connect calendar status and metric evidence to one weekly report schema.",
        ],
        deck_test="Check one routine case, one escalation, and every human owner.",
        steps=[
            (
                "Open operations-runbook-template.md and save a copy as 07-operations-agent-runbook.md. Keep its four workflow lanes: Content Planning, Scheduling, Inbox Triage, and Weekly Reporting.",
                "Template: labs/resources/operations-runbook-template.md\nSave as: C526-campaign-pack/07-operations-agent-runbook.md",
            ),
            (
                "For each lane, complete the operating-loop fields: trigger, authorised inputs, agent task, tool or surface, validation, human approval, action, log evidence, and stop or escalation path.",
                "Runbook columns: Lane | Trigger | Inputs | Agent task | Tool/surface | Validation | Approval | Action | Log | Stop/escalation",
            ),
            (
                "Create a permission table for reading course files, drafting content, preparing a schedule, publishing a post, drafting a reply, sending a reply, reading aggregate insights, changing targeting, and changing budget.",
                "Permission columns: Action | Risk level | Reversible? | Allowed in this workflow | Human role required | Evidence to log",
            ),
            (
                "Set this lab's authority: the agent may read synthetic files, draft content, classify synthetic messages, and prepare recommendations. Publishing, sending messages, changing targeting, and changing spend are blocked behind a person.",
                "Allowed: read synthetic inputs; draft; classify; calculate; recommend\nBlocked: publish; send; change targeting; change budget; upload customer lists",
            ),
            (
                "Build an approved routine-response bank for the collection window, product information, ordering link, delivery-area unknown, and order-specific help. General opening hours remain UNKNOWN. Use only the brand brief; route order-specific and personal-data cases to a person.",
                "Response bank columns: Intent | Approved reply | Source | Prohibited additions | Escalation condition | Owner\nDo not broaden the approved 7:30-11:00 collection window into general opening hours.",
            ),
            (
                "Open the synthetic message-scenarios CSV. Paste it, the response bank, and the G-C-A-T-E contract into the AI assistant. Ask for triage only, not message sending.",
                """Classify each synthetic Facebook message scenario.

Return columns:
scenario_id | intent | routine_or_human | approved_response_id | draft_reply_or_handoff_note | risk_reason | log_fields

Rules:
- Use only the approved response bank and brand brief.
- Routine replies may give approved public information.
- Escalate complaints, refunds, safety concerns, legal threats, account issues, order-specific cases, and any personal data.
- Never request or repeat personal data in the draft.
- Do not send anything; output is for human review.""",
            ),
            (
                "Review the triage table. Any scenario containing an order number, contact detail, complaint, safety concern, refund request, or legal language must route to a person even if part of the question looks routine.",
                "Triage invariant: higher-risk content overrides a routine keyword match.",
            ),
            (
                "Write the scheduling checklist from the Lab 3 calendar. Include Page identity, content ID, approved asset, final copy, link, time zone, date and time, reviewer, status, and rollback owner.",
                "Scheduling status values: DRAFT | READY FOR HUMAN REVIEW | APPROVED TO SCHEDULE | SCHEDULED | PAUSED",
            ),
            (
                "Optional view-only practice: In Meta Business Suite, open Planner and locate the Create post and scheduling controls described by the trainer. Do not schedule or publish. Record any interface difference in the runbook so the owner can verify the current path.",
                "Reference path: Facebook Page → Meta Business Suite → Create post / Planner → Scheduling options\nAction in this lab: view only; close without saving or scheduling.",
            ),
            (
                "Create the weekly report schema. Every finding must name the date window, source, metric definition, comparison, evidence row, limitation, and recommended next action with owner.",
                "Report sections: Objective status | Content delivered | Metric movement | Audience feedback themes | Risks and exceptions | One next experiment | Decisions needed",
            ),
            (
                "Save the completed runbook with a Change Log for response-bank updates, workflow exceptions, and owner decisions.",
                "## Change Log\n| Date | Workflow or response ID | Evidence | Change | Owner | Review date |",
            ),
        ],
        test=(
            "Use M01 as the routine case and M06 as the escalation case. M01 must cite the approved collection window; M06 must contain a handoff note without repeating the phone number. "
            "Also confirm every high-impact action in the permission table names a human role."
        ),
        checkpoint="Lab 8 will reuse the permission table, report evidence rules, human roles, stop paths, and change log as the foundation of a bounded scale policy.",
        troubleshooting=[
            ("The agent treats every message as routine", "Move the override risks above keyword rules and require risk classification before response selection."),
            ("The runbook says 'review as needed'", "Name the exact check, human role, evidence, and status transition required at that point."),
            ("Scheduling instructions do not match the current interface", "Record the interface difference, use the current official Help path, and keep the action in view or draft mode."),
        ],
        challenge="Add a response-quality sampling plan that reviews a percentage of routine drafts each week and turns recurring corrections into response-bank changes.",
        reflection="Which operations step benefits most from deterministic rules, and which benefits most from contextual agent reasoning?",
    ),
    dict(
        num=8,
        topic=4,
        title="Simulate a Bounded Optimisation and Scale Loop",
        objective="LO6 and LO5: Apply performance, operational, privacy, and customer-impact limits to a human-governed scaling decision",
        duration="65 minutes",
        desc=(
            "You complete the course by converting all prior guardrails into a bounded optimisation policy, then run synthetic scenarios through an agent that may recommend but cannot execute. "
            "The final campaign operations pack shows when to hold, pause, investigate, or propose a small scale step and records the evidence behind each decision."
        ),
        build="C526-campaign-pack/08-bounded-scale-policy.md plus a final manifest linking all eight campaign-pack checkpoints, owners, approvals, stop conditions, and rollback evidence.",
        services="Approved generative AI assistant, spreadsheet or text editor, scale scenarios, bounded-policy template, Labs 1-7 outputs",
        prerequisites=[
            "Completed all Labs 1-7; this lab reuses the success brief, prompt contract, performance diagnosis, and operations runbook.",
            "Open labs/resources/harbour-hearth-scale-scenarios.csv and bounded-scale-policy-template.md.",
            "Use only synthetic scenarios and hypothetical budget values.",
            "The workflow may recommend actions but may not change a real campaign or send a message.",
        ],
        deck_steps=[
            "Define eligibility, allowed actions, change caps, cooldowns, stop rules, and owners.",
            "Run synthetic scenarios through a recommendation-only agent.",
            "Check that tracking, customer impact, capacity, and policy risks override performance gains.",
            "Create the final campaign-pack manifest and 30-day pilot plan.",
        ],
        deck_test="Tracking errors block scale; changes stay within 15% and 72 hours.",
        steps=[
            (
                "Open bounded-scale-policy-template.md and save a copy as 08-bounded-scale-policy.md. Fill its primary KPI, guardrail metrics, stop rule, permission table, and human roles from Labs 1, 6, and 7.",
                "Template: labs/resources/bounded-scale-policy-template.md\nSave as: C526-campaign-pack/08-bounded-scale-policy.md\nInputs: 01-success-brief.md | 02-audience-and-prompt-contract.md | 06-performance-diagnosis.md | 07-operations-agent-runbook.md",
            ),
            (
                "Write the policy with six blocks: eligibility, allowed recommendations, maximum change, cooldown, stop or pause conditions, and approval plus log requirements.",
                """## Bounded Optimisation Policy
Eligibility: same metric definitions; complete 7-day window; event status healthy; minimum 10 purchases; no unresolved data-quality issue.
Allowed recommendations: HOLD, PAUSE, INVESTIGATE, PROPOSE CREATIVE TEST, PROPOSE BUDGET CHANGE.
Maximum budget recommendation: +15% or -15% per decision cycle.
Cooldown: 72 hours after a material change before another scale recommendation.
Stop or pause: tracking error; unsupported claim; privacy concern; negative feedback rate above 0.03%; fulfilment capacity below forecast demand; negative margin context; missing approver.
Approval and log: named marketing owner approves; record before/after value, evidence, reason, timestamp, expected result, rollback action.""",
            ),
            (
                "Open harbour-hearth-scale-scenarios.csv and read the column definitions. Confirm that Metric_Definition_Version matches the approved version, Event_Status is healthy, and Unresolved_Data_Quality_Issue is no before treating a row as eligible. Keep every row unchanged so classmates work from the same evidence.",
                "Open: labs/resources/harbour-hearth-scale-scenarios.csv\nEligibility evidence: Metric_Definition_Version = v1 | Event_Status = healthy | Unresolved_Data_Quality_Issue = no",
            ),
            (
                "Paste the G-C-A-T-E contract, bounded policy, and scenario table into the AI assistant. Make its authority recommendation-only.",
                """You are a recommendation-only Facebook campaign operations agent. Apply the bounded policy to each synthetic scenario independently.

Return columns:
scenario_id | eligible_yes_no | evidence | guardrail_status | recommendation | proposed_change | human_approval_needed | cooldown_end | rollback_trigger | log_note

Decision order:
1. Validate data and eligibility.
2. Apply privacy, advertising, customer-impact, capacity, and tracking stop rules.
3. Review the primary KPI and value context.
4. Apply the cooldown: when As_Of_Datetime is earlier than Last_Change_Datetime + 72 hours, choose HOLD and make no budget proposal.
5. Choose only one allowed recommendation and cap any budget proposal at 15%.

Never execute a change. When evidence conflicts or is missing, choose INVESTIGATE or HOLD and name the missing evidence.""",
            ),
            (
                "Check the scenario decisions against policy invariants. A tracking error, privacy concern, unsupported claim, negative feedback rate above 0.03%, negative margin context, or capacity shortfall must prevent scaling even when ROAS is strong. A cooldown violation is also decisive: when As_Of_Datetime is earlier than Last_Change_Datetime + 72 hours, the recommendation must be HOLD with no budget proposal. Use SC06 to verify this rule.",
                "Invariant check columns: Scenario | Trigger present | Required policy effect | Agent effect | Corrected decision\nSC06 expected effect: HOLD | Proposed change: none",
            ),
            (
                "For any incorrect agent decision, identify whether the failure came from missing input, ambiguous policy, wrong calculation, or instruction order. Revise the policy or prompt and rerun only that scenario.",
                "Correction log: Scenario | Failure type | Evidence | Rule change | New recommendation",
            ),
            (
                "Choose one eligible healthy scenario and write a human Decision Note. Calculate the proposed daily budget from Current_Daily_Budget_SGD, calculate Cooldown_End from Last_Change_Datetime + 72 hours, and include expected effect, capacity check, guardrails, approver, and rollback trigger.",
                "Status must remain PROPOSED — AWAITING HUMAN APPROVAL.",
            ),
            (
                "Create the final campaign-pack manifest. List each numbered artifact, its purpose, authoritative inputs, owner, current status, last review date, and next decision it supports.",
                "Manifest columns: Artifact | Purpose | Authoritative inputs | Owner | Status | Last review | Next decision",
            ),
            (
                "Add a 30-day draft-first pilot plan with weekly checkpoints for content quality, metric integrity, response exceptions, customer impact, and policy changes. Keep all public or financial actions under the named owners.",
                "Week 1: baseline and draft quality\nWeek 2: exception and correction labels\nWeek 3: one controlled experiment\nWeek 4: governance review and authority decision",
            ),
            (
                "Save 08-bounded-scale-policy.md and confirm the C526-campaign-pack folder contains artifacts 01 through 08, the two Lab 4 image-evidence files, and the metric workbook.",
                "Final folder: C526-campaign-pack/\nRequired numbered files: 01, 02, 03, 04, 05, 06, 07, 08\nEvidence: 04-control-image-1080.png | 04-phone-preview-360.png | 06-facebook-metrics.xlsx",
            ),
        ],
        test=(
            "Run four invariants: Tracking_Error = yes must block scaling; Negative_Feedback_Rate_Pct > 0.03 must block scaling; a proposed budget change must be no greater than 15%; and As_Of_Datetime earlier than Last_Change_Datetime + 72 hours must produce HOLD with no budget proposal. Record SC06 as the cooldown Test Evidence row. "
            "Finally, trace the selected scale recommendation back to its metric row, policy rule, human owner, and rollback trigger."
        ),
        checkpoint="The completed C526-campaign-pack is your reusable implementation model. Replace synthetic inputs only after your organisation authorises the data, owners, platform access, and operating limits.",
        troubleshooting=[
            ("The agent scales whenever ROAS is high", "Move stop conditions before performance evaluation and require guardrail status to be clear before any scale recommendation."),
            ("The proposed change exceeds 15%", "Add a deterministic cap calculation and reject any recommendation whose absolute percentage is greater than 15."),
            ("The policy contains vague terms such as 'enough data'", "Replace them with a named window, minimum event count, data-quality condition, owner, and exception path."),
        ],
        challenge="Design a second authority level that may automatically pause on a verified tracking outage but still cannot resume or change budget without a person; explain why pause and resume have different risk.",
        reflection="What evidence would you require before increasing this workflow's autonomy beyond recommendation-only mode?",
    ),
]
