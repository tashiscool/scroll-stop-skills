# JSON Brand / Copy Source

Use this when the user provides a scraped JSON export alongside the video-led website request.

## What The JSON Is For

In `scroll-stop-builder`, the JSON is not the page blueprint.
It is the source of truth for:
- brand colors
- typography
- CTA priority
- tone of voice
- feature language
- supporting section ideas

The actual coded page can still be completely different in structure if the video-led design needs it.

## What To Extract

### Visual Tokens
- primary color
- background color
- text color
- accent color
- font family
- border radius feel
- button style

### CTA Logic
- primary CTA
- secondary CTA
- helper actions like region checks, waitlist, pricing, or demos

### Messaging
- product headline
- trust statement
- feature blurbs
- audience tone

### Section Signals
- what the source site considered important enough to place on the homepage
- how proof is presented
- whether the product emphasizes trust, speed, comparison, or emotional safety

## Recommended Pattern

For a video-led landing page:
1. use the video as the emotional hook
2. use the JSON to shape copy and CTA hierarchy
3. use the extracted design tokens to keep the coded implementation on-brand

## Pairara Example

If the JSON says:
- light scheme
- Plus Jakarta Sans
- orange CTA
- primary CTA `Sign up now`
- secondary CTA `Check your region`

then the coded scroll site should likely preserve:
- calm, trust-first dating tone
- one strong signup CTA
- one supporting region/waitlist flow
- clean pill-button controls
- warm, light visual system
