import argparse
import os
from PIL import Image

def compress_image(input_file, output_file, quality=85):
    try:
        with Image.open(input_file) as img:
            img.save(output_file, optimize=True, quality=quality)
        print(f"Image compressed and saved to {output_file}")
    except Exception as e:
        print(f"Error compressing image: {e}")

def main():
    parser = argparse.ArgumentParser(description="Image Compressor with Quality Control")
    parser.add_argument("input", help="Input image file path")
    parser.add_argument("--json", action="store_true", help="Output JSON format")
    parser.add_argument("--output", default=None, help="Output image file path")
    parser.add_argument("--quality", type=int, default=85, choices=range(10, 101), help="JPEG quality (default: 85)")
    args = parser.parse_args()

    if not os.path.isfile(args.input):
        print(f"Error: Input file {args.input} does not exist")
        return

    output_file = args.output or args.input.replace(os.path.splitext(args.input)[1], '.jpg')

    compress_image(args.input, output_file, quality=args.quality)

if __name__ == "__main__":
    main()