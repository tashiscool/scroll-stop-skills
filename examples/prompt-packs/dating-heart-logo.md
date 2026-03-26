# Dating Heart Logo Prompt Pack

This example shows how `exploded-scene-prompter` should improve a weak one-shot video prompt into a stronger three-part prompt package.

## Original Prompt

```text
You are an expert AI video prompt engineer. When I give you an image and an animation idea, generate a high-quality cinematic AI video prompt for video generation models. I am providing an image of a heart car. The animation should start with the heart fully exploded into many parts floating in space. The camera angle, framing, and composition must remain completely fixed throughout the entire animation. The parts should smoothly assemble together until the final frame becomes the fully built car exactly matching the reference image.
```

## Why It Was Weak

- It only described the motion, not both still endpoints in enough detail.
- It left the exploded state too vague.
- It did not inventory the fragments or define their material finish.
- It did not define pacing, secondary motion, or final hold strongly enough.

## Better Workflow

Generate:
1. assembled still
2. exploded still
3. video transition between them

Then, if needed, generate the HTML page around that pack.

## Example Output

### PROMPT A - ASSEMBLED SHOT

```text
Professional product-logo photography of a premium dating app heart emblem centered in frame, shot straight-on with perfectly symmetrical framing. Clean white seamless background (#FFFFFF), soft studio lighting with a subtle grounded shadow directly beneath the logo.

The logo is fully assembled and exactly matches the reference image: a stylized heart mark formed from two elegant ribbon-like curves, with a smooth coral-to-pink gradient on the left side and a rich magenta-to-violet gradient on the right side. The shape is crisp, polished, and pristine, with clean edges, subtle depth, and a refined premium finish.

The silhouette is simple and iconic, with the lower right ribbon sweep clearly visible and the inner negative space of the heart perfectly clean. The object should feel like a premium 3D brand sculpture rather than flat graphic design.

Photorealistic rendering, 16:9 aspect ratio, luxury product-catalog quality. Sharp focus across the entire emblem, subtle reflections on the curved surfaces, minimal elegant Apple-style product photography. No text, no additional objects in frame.

Shot on Phase One IQ4 150MP, 80mm lens, f/8. Studio strobe lighting with a large overhead softbox and white bounce cards on both sides. Ultra-clean commercial finish, 8K render downsampled to 4K.
```

### PROMPT B - DECONSTRUCTED / EXPLODED VIEW

```text
Professional exploded-view photography of the same premium dating app heart emblem, fully deconstructed into many floating sculptural fragments suspended in space against a clean white seamless background (#FFFFFF).

The exploded composition preserves the overall silhouette of the heart while separating it into 24-36 elegant curved fragments, each hovering with even spacing as if frozen mid-assembly. The pieces vary in size from larger ribbon arcs to smaller petal-like and shard-like sections, all derived from the same final heart mark. The arrangement should feel organized, balanced, and premium rather than chaotic.

Each fragment carries the same refined material finish and gradient palette as the final logo: coral, pink, magenta, and violet transitions across smooth curved surfaces. The pieces should feel like a high-end sculptural system broken into components, with subtle bevels, clean edges, and gentle thickness visible on each element.

The composition is centered, with the densest cluster near the heart silhouette and smaller pieces radiating slightly outward. Every element is pristine and detailed, with visible curvature, soft reflections, and precise separation between parts. The overall exploded layout should clearly imply that all fragments belong to one elegant heart-shaped emblem.

Soft studio lighting with subtle individual shadows beneath the floating pieces. Photorealistic rendering, 16:9 aspect ratio, technical product-illustration photography. Focus-stacked sharpness across all fragments. Same lighting setup and same camera position as prompt A for perfect visual continuity.
```

### PROMPT C - VIDEO TRANSITION (START FRAME / END FRAME)

```text
START FRAME: The heart logo is fully exploded into many sculptural fragments floating in space, centered on a clean white background. The camera is completely locked off. The fragments are evenly spaced, elegant, and clearly imply the silhouette of the final heart emblem.

END FRAME: The same fragments have smoothly assembled into the fully built premium heart logo, perfectly matching the reference image: coral-to-pink left curve, magenta-to-violet right curve, crisp heart silhouette, subtle grounded shadow, white studio background.

TRANSITION: Smooth, satisfying premium assembly animation. The shot begins with a brief still pause of 0.4 seconds while all fragments hover motionless in space. Then the largest anchor pieces begin to glide inward first, establishing the main outer curves of the heart. Smaller mid-size fragments follow in layered waves, filling in the form progressively from outer silhouette to inner contour. The smallest accent pieces arrive last, completing the edges and smoothing the final geometry.

Each fragment travels along deliberate, graceful arcing paths with slow-in, slow-out easing. Pieces rotate subtly as they move to reveal their 3D curvature, but never spin wildly. Motion should feel magnetically guided and precise, as if each part knows exactly where it belongs. The assembly happens over 2.5-3 seconds, with a premium snap-into-place finish followed by a very subtle final settle. Hold on the completed logo for 1 second.

STYLE: Photorealistic, white seamless background throughout, consistent soft studio lighting, no camera movement, no zoom, no pan, no tilt, no handheld motion. The only motion is the controlled assembly of the heart fragments into the final logo. Premium brand-film precision, clean luxury-tech aesthetic, no text, no extra objects.
```

## Takeaway

The pack is better because it gives the model:
- a clear intact endpoint
- a clear exploded endpoint
- a real choreography between them

That usually produces stronger video generations than a single vague motion prompt.
