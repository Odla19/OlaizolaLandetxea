#!/usr/bin/env python3
"""
Image Optimizer Script for Olaizola Landetxea
Optimizes images for web use: converts to WebP and creates multiple sizes.

Usage:
    python optimize_images.py

Requirements:
    pip install Pillow

Place source images in: public/images/raw/
Optimized images will be saved to: public/images/
"""

import os
import sys
import re
from pathlib import Path
from PIL import Image
from PIL.Image import Resampling

# Configuration
SOURCE_DIR = Path("public/images/raw")
OUTPUT_DIR = Path("public/images")
SIZES = {
    "sm": 640,
    "md": 768,
    "lg": 1024,
    "xl": 1280,
    "2xl": 1536,
}
QUALITY = 85
SUPPORTED_FORMATS = (".jpg", ".jpeg", ".png")

# Mapping for standardized names
STANDARDIZED_NAMES = {
    r'hero.*\.(jpg|jpeg|png)': 'hero',
    r'casa.*\.(jpg|jpeg|png)': 'casa',
    r'habitacion.*\.(jpg|jpeg|png)': 'habitacion',
    r'room.*\.(jpg|jpeg|png)': 'habitacion',
    r'hotel.*\.(jpg|jpeg|png)': 'hotel',
    r'exterior.*\.(jpg|jpeg|png)': 'exterior',
    r'interior.*\.(jpg|jpeg|png)': 'interior',
    r'naturaleza.*\.(jpg|jpeg|png)': 'naturaleza',
    r'paisaje.*\.(jpg|jpeg|png)': 'paisaje',
}


def ensure_dir(directory: Path) -> None:
    """Create directory if it doesn't exist."""
    directory.mkdir(parents=True, exist_ok=True)


def get_standardized_name(filename: str) -> str:
    """Get standardized name based on filename patterns."""
    filename_lower = filename.lower()
    
    for pattern, name in STANDARDIZED_NAMES.items():
        if re.match(pattern, filename_lower):
            return name
    
    # If no pattern matches, use the original name without extension
    return Path(filename).stem


def optimize_image(source_path: Path, output_dir: Path) -> None:
    """
    Optimize a single image: convert to WebP and create multiple sizes.
    
    Args:
        source_path: Path to the source image
        output_dir: Directory to save optimized images
    """
    try:
        # Open image
        with Image.open(source_path) as img:
            # Convert RGBA to RGB if necessary (for JPEG/WebP compatibility)
            if img.mode in ("RGBA", "P"):
                img = img.convert("RGB")
            
            # Get original dimensions
            original_width, original_height = img.size
            aspect_ratio = original_height / original_width
            
            # Get standardized base name
            base_name = get_standardized_name(source_path.name)
            
            print(f"Processing: {source_path.name} ({original_width}x{original_height})")
            
            # Create different sizes
            for size_name, max_width in SIZES.items():
                # Skip if original is smaller than target size
                if original_width < max_width:
                    continue
                
                # Calculate new dimensions maintaining aspect ratio
                new_width = max_width
                new_height = int(new_width * aspect_ratio)
                
                # Resize image
                resized = img.resize((new_width, new_height), Resampling.LANCZOS)
                
                # Save as WebP
                output_filename = f"{base_name}-{size_name}.webp"
                output_path = output_dir / output_filename
                
                resized.save(
                    output_path,
                    "WEBP",
                    quality=QUALITY,
                    method=6,  # Best compression
                    optimize=True
                )
                
                print(f"  Created: {output_filename} ({new_width}x{new_height})")
            
            # Also save original size as WebP
            output_filename = f"{base_name}-original.webp"
            output_path = output_dir / output_filename
            
            img.save(
                output_path,
                "WEBP",
                quality=QUALITY,
                method=6,
                optimize=True
            )
            
            print(f"  Created: {output_filename} (original size)")
            
    except Exception as e:
        print(f"Error processing {source_path}: {e}", file=sys.stderr)


def main():
    """Main function to optimize all images in the source directory."""
    # Check if Pillow is installed
    try:
        from PIL import Image
    except ImportError:
        print("Error: Pillow is not installed. Run: pip install Pillow", file=sys.stderr)
        sys.exit(1)
    
    # Ensure directories exist
    ensure_dir(SOURCE_DIR)
    ensure_dir(OUTPUT_DIR)
    
    # Find all images in source directory
    image_files = [
        f for f in SOURCE_DIR.iterdir()
        if f.is_file() and f.suffix.lower() in SUPPORTED_FORMATS
    ]
    
    if not image_files:
        print(f"No images found in {SOURCE_DIR}")
        print(f"Place images ({', '.join(SUPPORTED_FORMATS)}) in that directory and run again.")
        return
    
    print(f"Found {len(image_files)} image(s) to optimize\n")
    
    # Process each image
    for image_file in sorted(image_files):
        optimize_image(image_file, OUTPUT_DIR)
        print()
    
    print("Optimization complete!")


if __name__ == "__main__":
    main()
