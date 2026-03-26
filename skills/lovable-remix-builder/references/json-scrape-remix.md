# JSON Scrape Remix

Use this when the user provides a structured export from a scraping tool instead of screenshots.

## What To Pull From The JSON

### Branding
- color scheme
- primary and accent colors
- background color
- text color
- font family
- button radius and general component feel

### CTA Hierarchy
- primary CTA text
- secondary CTA text
- supportive actions like region checks, waitlist joins, demos

### Section Order
Use the markdown or extracted content to infer:
- navbar
- hero
- supporting proof card or demo area
- features
- social proof or trust signal
- form / checker / lead capture
- footer

### Tone
Look for:
- emotional stance
- target audience
- product personality
- whether the site feels calm, urgent, playful, or premium

## Output Shape

When using a JSON export, produce:
1. a design-system summary
2. a section map
3. the Lovable prompts in order
4. rewrite prompts if the user is changing brands
5. follow-on page prompts

## Example Mapping

If the JSON says:
- `Plus Jakarta Sans`
- light color scheme
- orange accent
- primary CTA `Sign up now`
- secondary CTA `Check your region`

then your Lovable prompts should preserve:
- clean, rounded, trust-first visual language
- pill buttons
- clear hero CTA hierarchy
- warm modern dating-app tone

## Important Rule

Do not dump raw JSON into Lovable.
Translate it into a cleaner build plan and section prompts first.
