# Canonical Moving Van Example

Use this example as the default quality bar for requests like:

```text
Hey using this skill, build me a html view for a moving company which is full of furniture and i want the visual to be the back of that van exploding with all of the items
```

## Expected Behavior

Do this in two phases:

1. Generate the three video-generation prompt blocks first
2. Only after that, generate the HTML prompt page around them if requested

## Canonical Output Shape

### PROMPT A - ASSEMBLED SHOT

```text
Professional product photography of a modern white removal van (Mercedes Sprinter or Ford Transit style) centered in frame, shot from a 3/4 front angle. Clean white background (#FFFFFF), soft studio lighting with subtle shadows beneath the vehicle.

The van is pristine, brand-new, with rear doors wide open revealing a perfectly packed interior neatly stacked cardboard moving boxes in various sizes (small, medium, large), a rolled-up rug poking out, a floor lamp handle visible, and the edges of bubble-wrapped picture frames. Everything is immaculately organized inside the cargo area like a real-life game of Tetris. The boxes are uniform kraft brown cardboard with clean edges.

The van exterior is clean matte white with subtle panel lines and chrome door handles. Visible details include the roof rack, side mirrors, rear step bumper, and professional-grade tie-down straps inside the cargo bay.

Photorealistic rendering, 16:9 aspect ratio, product catalog quality. Sharp focus across the entire vehicle and its contents, subtle reflections on the van's bodywork. Minimal, elegant, Apple-style product photography. No text, no logos, no other objects in frame.

Shot on Phase One IQ4 150MP, 80mm lens, f/8. Studio strobe lighting with a large softbox above and white bounce cards on both sides. Ultra-clean commercial finish, 8K render downsampled to 4K.
```

### PROMPT B - DECONSTRUCTED / EXPLODED VIEW

```text
Professional exploded-view photography of a white removal van, deconstructed into its entire packed contents, every item floating elegantly in space against a clean white background (#FFFFFF).

The van sits at center with its rear doors swung fully open, and every single item that was packed inside is now floating outward in a dramatic, organized explosion. Each piece hovers with even spacing, maintaining the general spatial relationship of where it sat in the cargo area. The arrangement follows a diagonal explosion axis radiating outward from the van's open rear doors.

Floating items include: 12-15 kraft cardboard moving boxes in various sizes (some open showing bubble wrap inside), a rolled Persian rug, two bubble-wrapped picture frames, a disassembled flat-pack bookshelf, a standing floor lamp, a set of dining chairs, a microwave oven, a potted plant in protective wrapping, coiled packing tape rolls, a dolly / hand truck, folded moving blankets, a box of kitchen utensils with items spilling out (whisk, ladle, spatula), sofa cushions, a guitar in a soft case, a stack of books held by a bungee cord, and ratchet tie-down straps unfurling in mid-air.

Every item is pristine and detailed. You can see the corrugation texture on the cardboard, the weave of the moving blankets, the chrome on the kitchen utensils, and the grain on the wooden bookshelf pieces. The overall composition maintains the silhouette of the loaded van expanding outward.

Soft studio lighting with subtle individual shadows on each floating piece. Photorealistic rendering, 16:9 aspect ratio, technical illustration photography. Shot on Phase One IQ4 150MP, focus-stacked for sharpness across all floating elements. Same lighting setup as prompt A for visual continuity.
```

### PROMPT C - VIDEO TRANSITION (START FRAME / END FRAME)

```text
START FRAME: A fully loaded white removal van with rear doors open, perfectly packed with moving boxes, furniture, and household items. Centered on a white background, product photography style, soft studio lighting.

END FRAME: The same white removal van with all of its contents elegantly exploded outward, every box, piece of furniture, household item, and packing material floating in space around the van in an organized radial explosion from the open rear doors. Each item maintains its spatial relationship to where it was packed.

TRANSITION: Smooth, satisfying unpacking deconstruction animation. The van begins still and fully loaded. After a brief pause (0.5s), items begin to float outward from the cargo area starting with the items nearest the doors (boxes at the back) and progressively pulling out deeper items (furniture, rugs, appliances). Each piece lifts and drifts outward along clean, deliberate arcing paths. Movement is eased (slow-in, slow-out) with slight rotations on individual items to reveal their 3D form. Boxes gently tumble, the rug unrolls slightly, and tie-down straps unfurl like ribbons. The separation happens over 2-3 seconds in a cascading sequence from back-to-front, not all at once. Final floating arrangement holds for 1 second with every item suspended in perfect organized chaos.

STYLE: Photorealistic, white background throughout, consistent studio lighting, locked-off camera, no text, no logos. The only motion is the van contents floating out of the cargo area with product-film precision.
```

## Why This Example Matters

- It expands the user's generic idea into a stronger payload inventory.
- It preserves continuity between the stills and the motion prompt.
- It gives the video model a real choreography instead of a vague “stuff explodes out” instruction.
- It creates a much stronger foundation for the later HTML prompt page.
