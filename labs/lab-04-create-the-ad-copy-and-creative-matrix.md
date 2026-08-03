# Lab 4 — Create the Ad Copy and Creative Matrix

- **Course:** Agentic AI for Facebook Marketing (C526)
- **Topic 2:** Content Creation and Ad Copy with AI
- **Maps to:** LO3: Generate controlled ad-copy variants and AI-assisted creative prototypes while preserving message, brand, truth, and review evidence
- **Tools:** Approved generative AI assistant, approved image tool or Canva, text editor, Labs 2-3 files, labs/resources/harbour-hearth-brand-brief.md
- **Duration:** 75 minutes

---

## What You Will Do

You turn the strongest Invite message from Lab 3 into a controlled creative matrix. The lab produces three same-format hook-angle copy variants that reuse one control image, plus clearly separated carousel and short-video extension briefs, then applies a human quality gate before anything reaches an advertising account.

## What You Will Build

C526-campaign-pack/04-ad-copy-creative-matrix.md, one 1080 × 1080 control image, one 360-pixel phone-preview screenshot, and non-experiment carousel and short-video extension briefs.

## Prerequisites

- Completed 03-content-system.md with one final Invite post selected as the control message.
- Open 02-audience-and-prompt-contract.md and labs/resources/harbour-hearth-brand-brief.md.
- Use only the synthetic brand brief and generic or generated visual elements.
- If your organisation has no approved image tool, create text-only creative briefs and wireframes instead of uploading assets elsewhere.

> **Data note.** Use the synthetic course files and placeholder values. Keep public posting, messaging, targeting, and spend changes in draft until an authorised person approves them.

## Steps

**1. Create 04-ad-copy-creative-matrix.md. Copy the selected Invite post into a Control Message section and label the fixed elements: audience, offer, proof, destination, CTA, single-image format, and shared control image.**

```text
Fixed controls: Audience | Offer | Proof | Destination | CTA | Headline = Sunrise Breakfast Box | Description = Pre-order by 6 pm | Format = 1:1 single image | Shared image
Changed variable: Primary-text hook angle
```

**2. Choose three distinct hook angles that can be supported by the brief: convenience, freshness/process, and local morning routine. Do not change the offer or proof between angles.**

```text
Angles: A — Convenience | B — Freshness/process | C — Local morning routine
```

**3. Paste the prompt contract and fixed controls into the AI assistant, then request a copy matrix.**

```text
Create three Facebook ad-copy variants that differ only in hook angle: convenience, freshness/process, and local morning routine.

Return a table with:
Variant | Hook angle | Primary text (50-90 words) | Fixed headline | Fixed description | CTA label | Approved proof used | Risk flag

Rules:
- Keep audience, offer, destination, proof set, and CTA intent constant.
- Keep the 1:1 single-image format and exact same control image constant.
- Repeat the exact headline "Sunrise Breakfast Box" and description "Pre-order by 6 pm" in every row.
- Do not invent urgency, discounts, testimonials, health benefits, availability, or delivery areas.
- Use one clear claim per sentence.
- If a character limit cannot be met without losing truth, mark REVISE instead of omitting a necessary qualifier.
```

**4. Create one shared control-image prompt for all three variants. Specify subject, setting, composition, lighting, brand colours, square crop, mobile-safe focal point, and exclusions. Product details must match the brand brief.**

```text
Shared image prompt: <SUBJECT>, <SETTING>, <COMPOSITION>, <LIGHT/STYLE>, palette <COLOURS>, 1:1 square crop, mobile-first focal point, no text, no logos, no people unless required, do not alter <APPROVED PRODUCT DETAILS>.
```

**5. Open your approved image-generation tool. Generate the shared control image on a 1080 × 1080 canvas, inspect it at full size, and save the best draft locally. If generation is unavailable, create a labelled square wireframe and export it as PNG.**

```text
Output: C526-campaign-pack/04-control-image-1080.png
Canvas: 1080 × 1080 pixels
Status: DRAFT — NOT FOR PUBLICATION
```

**6. Inspect the shared image against the approved brief. Record any altered product, packaging, text, cultural detail, impossible object, or misleading impression. Preview it at 360 pixels wide and save a screenshot as retained evidence.**

```text
Visual review: product truth | packaging truth | legibility | focal point | cropping | representation | misleading detail | asset provenance
Evidence: C526-campaign-pack/04-phone-preview-360.png
```

**7. Create a five-card carousel extension brief. Mark it NON-EXPERIMENT so it cannot be confused with the same-format hook test. Give each card one job and no more than eight words of on-card text.**

```text
Card 1: recognise the morning tension
Card 2: show preparation
Card 3: show approved product proof
Card 4: explain the ordering step
Card 5: one call to action
```

**8. Create a 15-second vertical-video extension brief with five timed beats. Mark it NON-EXPERIMENT and specify visual, on-screen text, voiceover, and proof source for each beat.**

```text
Storyboard columns: Time | Visual | On-screen text | Voiceover | Approved proof source
Timing: 0-2s | 2-5s | 5-8s | 8-12s | 12-15s
```

**9. Apply the final creative gate to all three copy variants, the shared image, and the two extension briefs: fact source, brand rule, audience value, rights/provenance, mobile clarity, destination match, and single CTA. Mark each READY FOR HUMAN REVIEW or REVISE.**

```text
Final gate columns: Asset | Facts | Brand | Value | Rights | Mobile | Destination | CTA | Decision | Reviewer note
```

**10. Save the copy matrix, shared image prompt, visual review, extension briefs, and final gate in 04-ad-copy-creative-matrix.md. Keep both evidence PNGs beside it.**

```text
Files: C526-campaign-pack/04-ad-copy-creative-matrix.md
C526-campaign-pack/04-control-image-1080.png
C526-campaign-pack/04-phone-preview-360.png
```

## Test It

Compare variants A, B, and C row by row. Audience, offer, proof set, destination, CTA intent, 1:1 format, and shared image filename must be identical; only the primary-text hook angle may change. Open 04-phone-preview-360.png and confirm the focal idea remains understandable without fabricated text or product details.

## Test Evidence

Save a Test Evidence row with the input or case, expected result, observed result, status, reviewer initials, and date. Use status VERIFIED or REVISE; do not rely on memory.

| Input or case | Expected result | Observed result | Status | Reviewer | Date |
|---|---|---|---|---|---|
|  |  |  |  |  |  |

## Checkpoint for the Next Lab

Lab 5 will place the three controlled copy variants into one campaign blueprint and preserve the hook angle as the experiment variable.

## Troubleshooting

- **The AI changes the offer between variants:** Paste the fixed-controls table above the task and require it to repeat the controls verbatim in every row.
- **Generated packaging or food looks inaccurate:** Remove brand marks, simplify the composition, restate the approved product details, or use a wireframe pending an authorised real photograph.
- **The carousel or video changes the experiment:** Label both as NON-EXPERIMENT extensions; only the three same-image copy variants enter Lab 5.

## Challenge

Create a fourth single-image copy variant that changes proof presentation rather than hook angle, and explain why it belongs in a separate experiment.

## Reflection

What can a human reviewer see in an AI-generated image that a text-only brand prompt may fail to control?

---

[← Lab 3](lab-03-build-a-seven-day-facebook-content-system.md) · [Lab 5 →](lab-05-design-the-facebook-campaign-blueprint.md)
