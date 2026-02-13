---
name: image-optimizer
description: Optimizes images for web using Python (WebP conversion + Resizing).
---

# Image Optimizer Agent

## Trigger
Use this skill when the user provides new photos or asks to "optimize images".

## The Tool
I have a Python script strategy for this.

1. **Source Directory:** Look for images in `raw_images/`.
2. **Target Directory:** Save optimized versions in `public/images/`.
3. **Specifications:**
   - Format: WebP (Quality 80)
   - Max Width: 1920px (for hero headers), 800px (for gallery grid).
   - Filenames: Convert to snake_case (e.g., "Foto Habitacion 1.jpg" -> "habitacion_01.webp").

## Action
If the script `optimize.py` does not exist in root, create it using `Pillow` library:
- Import `PIL` (Image).
- Loop through files.
- Resize using `Image.LANCZOS`.
- Save as `.webp`.