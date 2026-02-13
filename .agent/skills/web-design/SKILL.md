---
name: web-design-guidelines
description: Review UI code for Olaizola Etxea. Ensures modern, accessible, and clean design.
version: "1.0.0"
---

# Olaizola Etxea Design Guidelines

## Core Principles
1. **Minimalism & Nature:** The design must reflect the "warm minimalism" and "nature" vibe of Arantza Hotela but with our own identity.
2. **Mobile First:** Everything must look perfect on mobile.
3. **Speed:** Use semantic HTML5 and optimized CSS (Tailwind).

## Color Palette (From Color Flow)
Paleta Color Flow - Códigos HEX:
1. #F9E5DF - Rosa muy claro / Crema rosado
2. #EECBC4 - Rosa pálido / Melocotón claro
3. #E8B2AB - Rosa coral / Salmón
4. #B36A64 - Terracota / Rojo ladrillo
5. #5B6775 - Gris azulado / Pizarra
6. #BABECB - Gris lavanda / Azul grisáceo
Para Tailwind CSS:
colors: {
  'color-flow': {
    100: '#F9E5DF',
    200: '#EECBC4',
    300: '#E8B2AB',
    400: '#B36A64',
    500: '#5B6775',
    600: '#BABECB',
  }
}
O si prefieres nombres descriptivos:
colors: {
  'cream-rose': '#F9E5DF',
  'peach-pale': '#EECBC4',
  'coral-rose': '#E8B2AB',
  'terracotta': '#B36A64',
  'slate-blue': '#5B6775',
  'lavender-gray': '#BABECB',
}

## Typography
- Headings: Serif font (e.g., 'Playfair Display') for elegance.
- Body: Sans-serif (e.g., 'Lato' or 'Inter') for readability.

## Components
- **Buttons:** Simple, elegant, no heavy shadows. Ghost buttons for secondary actions.
- **Images:** Always use `object-cover` to handle diverse aspect ratios. Rounded corners (`rounded-lg`) for a softer feel.
- **Spacing:** Generous whitespace (`p-8`, `gap-8`) to convey luxury and calm.

## Accessibility
- Ensure high contrast for text.
- Always include `alt` tags for images (crucial for SEO).