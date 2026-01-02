# Image Generation MCP

## Purpose
Generate visual artifacts to support planning, reflection, or motivation.

## Characteristics
- Stateless
- Uses external image generation API
- Saves images locally
- Returns metadata only (not raw image bytes)

## Operations
- generate_image(prompt, style?)
- list_generated_images()

## Storage
- Local directory for generated images
- Simple metadata tracking (file name + prompt)

## Non-Goals
- No image editing
- No image deletion
- No UI rendering

### generate_image
Inputs:
- prompt: string
- style: string (optional)

Behavior:
- Generates an image that visually represents the intent of the prompt.
- Applies the optional style as a high-level aesthetic hint.
- Saves the generated image locally with a unique filename.
- Does not return raw image data.

Returns:
- image_path: string (local file path)
- description: string (brief description of what was generated)

Errors:
- If prompt is missing or empty: return a clear error message.
- If image generation fails: return a clear failure message.

