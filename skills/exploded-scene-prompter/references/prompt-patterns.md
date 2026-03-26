# Prompt Patterns

Use these formulas to keep exploded scenes crisp and premium.

The default deliverable is a three-part package:
1. assembled still
2. exploded still
3. video transition from 1 to 2

If the user also asked for an HTML page, the HTML is built after these three prompts, not instead of them.

## Base Formula

1. Hero subject and orientation
2. Background and lighting
3. Visible components and arrangement
4. Material and texture detail
5. Motion feel
6. Camera and quality cues

## Assembled Shot Formula

```text
Professional product photography of [hero subject] centered in frame, shot from [angle]. [Background]. [Lighting]. The subject is pristine and fully assembled, with [payload/components] neatly visible. [Material details]. Photorealistic, premium catalog quality, [aspect ratio]. No text, no logos, no clutter.
```

## Exploded Shot Formula

```text
Professional commercial hero shot of [hero subject] with [rear/front/top/side] opened and its contents exploding outward in a controlled suspended composition. Items include [component list]. Each element is evenly spaced, fully readable, and visually balanced as if frozen mid-motion. [Background]. [Lighting]. Premium product-ad realism, [aspect ratio], sharp focus, subtle shadows, no text, no logos.
```

## Video Transition Formula

```text
START FRAME: [describe the intact loaded / assembled state clearly]

END FRAME: [describe the fully exploded or deconstructed final composition clearly]

TRANSITION: [describe the exact motion choreography]. After a brief pause, [what moves first] begins to separate, followed by [what moves next], with [arcing / radial / cascading / staged] motion. Each object follows a deliberate path with [easing notes]. Add secondary motion such as [unfurling / slight unrolling / gentle tumbling / lid opening / ribbon-like strap movement] to reveal shape and material. The final arrangement holds for [duration] with all elements suspended cleanly in space.

STYLE: [photoreal / premium product film / white studio background / consistent lighting / locked camera / no text / etc.]
```

## Video Prompt Quality Rules

- Keep the start and end frames visually continuous.
- Explicitly state whether the camera is locked, dollying, orbiting, or handheld.
- Explain motion order. “Everything flies out” is too weak.
- Mention timing beats:
  - opening pause
  - reveal duration
  - final hold
- Mention secondary motion on at least 2-4 object types.
- Reuse the same lighting and lens family as the still prompts unless the user wants a style shift.

## Generic Prompt Upgrade Rules

Weak:
```text
A van explodes and all the furniture comes out.
```

Stronger:
```text
A clean white removal van remains locked in a centered studio shot. After a brief still pause, the back-row moving boxes lift out first, followed by deeper furniture and wrapped household goods in a cascading back-to-front unpacking motion. Boxes tumble subtly, tie-down straps unfurl, the rolled rug loosens slightly, and chair legs rotate just enough to show their form.
```

## Service-Business Formula

For moving, repair, cleaning, catering, or similar services:
- Show the service vehicle or toolset as the hero object.
- Make the payload tell the business story.
- Keep the motion dramatic but organized.
- Bias toward “premium ad campaign” rather than chaotic action scene.
- In the video transition, make the unpacking order believable.

## Moving Company Example Components

- cardboard moving boxes in mixed sizes
- rolled rug
- dining chair
- table lamp
- bubble-wrapped picture frames
- folded blankets
- side table
- packing tape
- labeled storage crates
- tie-down straps

## HTML View Requirements

When asked for an HTML view:
- Use the template in `assets/prompt-page-template.html`
- Include a short scene summary at the top
- Present prompts in separate cards
- Keep the visual design neutral and premium
- Make it easy to copy each prompt block
