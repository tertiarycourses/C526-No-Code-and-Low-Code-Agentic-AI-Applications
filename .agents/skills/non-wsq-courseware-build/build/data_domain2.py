"""Topic 2 — Content Creation and Ad Copy with AI."""

DOMAIN2 = [
    dict(
        num=3,
        topic=2,
        title="Build a Seven-Day Facebook Content System",
        objective="LO3: Produce a journey-aligned Facebook content calendar and post set from approved facts, audience evidence, and brand rules",
        duration="45 minutes",
        desc=(
            "You use the success brief, selected audience, and prompt contract to design a seven-day Facebook calendar that balances teaching, proof, invitation, and learning. "
            "You then turn the selected Invite entry into one publication-ready control post while keeping every fact traceable."
        ),
        build="C526-campaign-pack/03-content-system.md containing four content pillars, a seven-day calendar, one complete control post, a quality gate, a reviewer correction log, and retained Test Evidence.",
        services="Approved generative AI assistant, text editor or spreadsheet, Lab 1 and Lab 2 files",
        prerequisites=[
            "Completed 01-success-brief.md and 02-audience-and-prompt-contract.md.",
            "Selected one primary audience hypothesis in Lab 2.",
            "No confidential brand assets or real customer comments are used.",
        ],
        deck_steps=[
            "Define four content pillars with a customer-journey job and evidence boundary.",
            "Generate a seven-day calendar with one learning question per item.",
            "Draft the selected Invite control post and review it against the contract.",
            "Save reviewer corrections so later prompts can improve.",
        ],
        deck_test="Trace audience to evidence, action, and a learning signal.",
        steps=[
            (
                "Create 03-content-system.md. At the top, paste the final decision chain and the selected audience hypothesis from Labs 1 and 2.",
                "File: C526-campaign-pack/03-content-system.md\nInputs: 01-success-brief.md + selected audience hypothesis from 02-audience-and-prompt-contract.md",
            ),
            (
                "Define four content pillars named Teach, Show, Prove, and Invite. For each, write its customer-journey job, allowed evidence, suitable formats, and the action it may request.",
                "Table columns: Pillar | Journey job | Allowed evidence | Suitable formats | Allowed customer action",
            ),
            (
                "Start a fresh AI chat. Paste the G-C-A-T-E contract, the success brief, selected audience hypothesis, and the four-pillar table. Then request the calendar.",
                """Create a seven-day Facebook organic content calendar for the synthetic Harbour & Hearth Sunrise Breakfast Box.

Return exactly seven rows with columns:
Day | Journey job | Pillar | Format | Hook | Approved evidence used | Main value | Call to action | Learning question | Human review focus

Constraints:
- Use Teach, Show, Prove, and Invite; include each at least once.
- Use at least three formats across single image, carousel, and short video.
- Keep one main message and one customer action per row.
- Cite the exact source heading or signal ID for every evidence claim.
- Do not invent a price, promotion, testimonial, customer count, health claim, or scarcity.
- The learning question must name the metric or feedback signal that could improve the next content cycle.""",
            ),
            (
                "Review the seven rows as one system. Confirm all four pillars appear, no two consecutive rows do the same journey job, and the Invite posts do not outnumber the combined Teach and Prove posts.",
                "Calendar balance check: all 4 pillars present; at least 3 formats; one CTA per row; every row has an evidence reference and learning question.",
            ),
            (
                "Choose one Invite row as the paid-message control for Lab 4. Ask the AI to draft that one complete post using the output schema below.",
                """For the selected Invite calendar row, return:
POST ID
PURPOSE: one sentence
PRIMARY TEXT: 60-110 words, warm and direct
ON-CREATIVE TEXT: maximum 8 words
CALL TO ACTION: one action
CREATIVE BRIEF: subject, setting, composition, proof detail, mobile-readability note
EVIDENCE USED: exact source heading or signal ID
REVIEW FLAGS: factual, brand, rights, privacy, or advertising concerns

Use Singapore English naturally without forced slang. One helpful detail must appear before the invitation.""",
            ),
            (
                "Apply the Content Quality Gate to the control draft. Mark Grounded facts, Brand fit, Audience value, Creative and rights check, and Objective-action match as OK or REVISE, with one sentence of evidence.",
                "Quality Gate columns: Post ID | Grounded facts | Brand fit | Audience value | Creative and rights | Objective-action match | Reviewer decision",
            ),
            (
                "Revise every REVISE item yourself or with a focused follow-up prompt. Do not ask for a total rewrite when one sentence is the problem.",
                "Focused revision prompt: Revise only <NAMED ELEMENT>. Preserve every approved fact, the selected audience need, the format, and the single call to action. Explain the change in one sentence.",
            ),
            (
                "Save the final calendar, control post, quality gate, and a Correction Log listing what the AI got wrong and what instruction would prevent the same issue.",
                "## Correction Log\n| Post ID | Problem label | Exact correction | Prompt rule to add next time |",
            ),
        ],
        test=(
            "Pick one calendar row and trace its audience need to the Lab 2 hypothesis, its claim to an approved source, its action to the Lab 1 customer action, and its learning question to a named signal. "
            "The chain must be complete without relying on an invented fact."
        ),
        checkpoint="Lab 4 will use the final Invite post and its learning question as the control message for paid creative variants.",
        troubleshooting=[
            ("The calendar is seven versions of the same offer", "Reassert the journey job and require different Teach, Show, Prove, and Invite value before changing formats."),
            ("The captions sound generic", "Paste the operational brand rules and ask for one specific approved detail before the call to action."),
            ("Evidence citations disappear during revision", "Require the source column to remain unchanged and reject any new claim without a source heading or signal ID."),
        ],
        challenge="Draft one Teach post and one Prove post from the calendar, then add a community-engagement question that invites a useful response without collecting personal data.",
        reflection="Which calendar field makes the system learn over time instead of becoming a faster content factory?",
    ),
    dict(
        num=4,
        topic=2,
        title="Create the Ad Copy and Creative Matrix",
        objective="LO3: Generate controlled ad-copy variants and AI-assisted creative prototypes while preserving message, brand, truth, and review evidence",
        duration="75 minutes",
        desc=(
            "You turn the strongest Invite message from Lab 3 into a controlled creative matrix. "
            "The lab produces three same-format hook-angle copy variants that reuse one control image, plus clearly separated carousel and short-video extension briefs, then applies a human quality gate before anything reaches an advertising account."
        ),
        build="C526-campaign-pack/04-ad-copy-creative-matrix.md, one 1080 × 1080 control image, one 360-pixel phone-preview screenshot, and non-experiment carousel and short-video extension briefs.",
        services="Approved generative AI assistant, approved image tool or Canva, text editor, Labs 2-3 files, labs/resources/harbour-hearth-brand-brief.md",
        prerequisites=[
            "Completed 03-content-system.md with one final Invite post selected as the control message.",
            "Open 02-audience-and-prompt-contract.md and labs/resources/harbour-hearth-brand-brief.md.",
            "Use only the synthetic brand brief and generic or generated visual elements.",
            "If your organisation has no approved image tool, create text-only creative briefs and wireframes instead of uploading assets elsewhere.",
        ],
        deck_steps=[
            "Lock the offer, proof, audience, destination, and CTA as experiment controls.",
            "Generate three hook-angle copy variants that reuse one image and one format.",
            "Produce the shared image and separate carousel/video extension briefs.",
            "Run truth, brand, rights, mobile, and objective-action checks.",
        ],
        deck_test="Only the hook varies; the phone-size prototype stays truthful.",
        steps=[
            (
                "Create 04-ad-copy-creative-matrix.md. Copy the selected Invite post into a Control Message section and label the fixed elements: audience, offer, proof, destination, CTA, single-image format, and shared control image.",
                "Fixed controls: Audience | Offer | Proof | Destination | CTA | Headline = Sunrise Breakfast Box | Description = Pre-order by 6 pm | Format = 1:1 single image | Shared image\nChanged variable: Primary-text hook angle",
            ),
            (
                "Choose three distinct hook angles that can be supported by the brief: convenience, freshness/process, and local morning routine. Do not change the offer or proof between angles.",
                "Angles: A — Convenience | B — Freshness/process | C — Local morning routine",
            ),
            (
                "Paste the prompt contract and fixed controls into the AI assistant, then request a copy matrix.",
                """Create three Facebook ad-copy variants that differ only in hook angle: convenience, freshness/process, and local morning routine.

Return a table with:
Variant | Hook angle | Primary text (50-90 words) | Fixed headline | Fixed description | CTA label | Approved proof used | Risk flag

Rules:
- Keep audience, offer, destination, proof set, and CTA intent constant.
- Keep the 1:1 single-image format and exact same control image constant.
- Repeat the exact headline "Sunrise Breakfast Box" and description "Pre-order by 6 pm" in every row.
- Do not invent urgency, discounts, testimonials, health benefits, availability, or delivery areas.
- Use one clear claim per sentence.
- If a character limit cannot be met without losing truth, mark REVISE instead of omitting a necessary qualifier.""",
            ),
            (
                "Create one shared control-image prompt for all three variants. Specify subject, setting, composition, lighting, brand colours, square crop, mobile-safe focal point, and exclusions. Product details must match the brand brief.",
                "Shared image prompt: <SUBJECT>, <SETTING>, <COMPOSITION>, <LIGHT/STYLE>, palette <COLOURS>, 1:1 square crop, mobile-first focal point, no text, no logos, no people unless required, do not alter <APPROVED PRODUCT DETAILS>.",
            ),
            (
                "Open your approved image-generation tool. Generate the shared control image on a 1080 × 1080 canvas, inspect it at full size, and save the best draft locally. If generation is unavailable, create a labelled square wireframe and export it as PNG.",
                "Output: C526-campaign-pack/04-control-image-1080.png\nCanvas: 1080 × 1080 pixels\nStatus: DRAFT — NOT FOR PUBLICATION",
            ),
            (
                "Inspect the shared image against the approved brief. Record any altered product, packaging, text, cultural detail, impossible object, or misleading impression. Preview it at 360 pixels wide and save a screenshot as retained evidence.",
                "Visual review: product truth | packaging truth | legibility | focal point | cropping | representation | misleading detail | asset provenance\nEvidence: C526-campaign-pack/04-phone-preview-360.png",
            ),
            (
                "Create a five-card carousel extension brief. Mark it NON-EXPERIMENT so it cannot be confused with the same-format hook test. Give each card one job and no more than eight words of on-card text.",
                "Card 1: recognise the morning tension\nCard 2: show preparation\nCard 3: show approved product proof\nCard 4: explain the ordering step\nCard 5: one call to action",
            ),
            (
                "Create a 15-second vertical-video extension brief with five timed beats. Mark it NON-EXPERIMENT and specify visual, on-screen text, voiceover, and proof source for each beat.",
                "Storyboard columns: Time | Visual | On-screen text | Voiceover | Approved proof source\nTiming: 0-2s | 2-5s | 5-8s | 8-12s | 12-15s",
            ),
            (
                "Apply the final creative gate to all three copy variants, the shared image, and the two extension briefs: fact source, brand rule, audience value, rights/provenance, mobile clarity, destination match, and single CTA. Mark each READY FOR HUMAN REVIEW or REVISE.",
                "Final gate columns: Asset | Facts | Brand | Value | Rights | Mobile | Destination | CTA | Decision | Reviewer note",
            ),
            (
                "Save the copy matrix, shared image prompt, visual review, extension briefs, and final gate in 04-ad-copy-creative-matrix.md. Keep both evidence PNGs beside it.",
                "Files: C526-campaign-pack/04-ad-copy-creative-matrix.md\nC526-campaign-pack/04-control-image-1080.png\nC526-campaign-pack/04-phone-preview-360.png",
            ),
        ],
        test=(
            "Compare variants A, B, and C row by row. Audience, offer, proof set, destination, CTA intent, 1:1 format, and shared image filename must be identical; only the primary-text hook angle may change. "
            "Open 04-phone-preview-360.png and confirm the focal idea remains understandable without fabricated text or product details."
        ),
        checkpoint="Lab 5 will place the three controlled copy variants into one campaign blueprint and preserve the hook angle as the experiment variable.",
        troubleshooting=[
            ("The AI changes the offer between variants", "Paste the fixed-controls table above the task and require it to repeat the controls verbatim in every row."),
            ("Generated packaging or food looks inaccurate", "Remove brand marks, simplify the composition, restate the approved product details, or use a wireframe pending an authorised real photograph."),
            ("The carousel or video changes the experiment", "Label both as NON-EXPERIMENT extensions; only the three same-image copy variants enter Lab 5."),
        ],
        challenge="Create a fourth single-image copy variant that changes proof presentation rather than hook angle, and explain why it belongs in a separate experiment.",
        reflection="What can a human reviewer see in an AI-generated image that a text-only brand prompt may fail to control?",
    ),
]
