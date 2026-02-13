# Olaizola Landetxea

## Estructura de Imágenes

```
public/
├── images/
│   ├── optimized/      # Imágenes optimizadas automáticamente
│   ├── raw/           # Imágenes originales sin optimizar
│   └── icons/         # Iconos y favicons
└── fonts/             # Fuentes locales
```

### Convenciones de Nombres

- **Imágenes**: kebab-case (ej: `casa-exterior.jpg`)
- **Iconos**: prefijo `icon-` (ej: `icon-phone.svg`)
- **Formatos preferidos**: WebP, AVIF para web; JPG para fotografías; PNG para transparencias

### Optimización

Las imágenes en `raw/` deben optimizarse antes de usar en producción.