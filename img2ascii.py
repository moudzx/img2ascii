import argparse
from PIL import Image, ImageOps, ImageEnhance

RAMP = " .'`^\",:;Il!i><~+_-?][}{1)(|/tfjrxnuvczXYUJCLQ0OZmwqpdbkhao*#MW&8%B@$"


def convert(path, width, contrast, invert):
    img = Image.open(path).convert("L")
    img = ImageOps.autocontrast(img)
    img = ImageEnhance.Contrast(img).enhance(contrast)
    w, h = img.size
    height = max(1, int(width * h / w * 0.5))
    img = img.resize((width, height), Image.LANCZOS)
    ramp = RAMP[::-1] if invert else RAMP
    n = len(ramp) - 1
    lines = []
    for y in range(height):
        row = "".join(ramp[img.getpixel((x, y)) * n // 255] for x in range(width))
        lines.append(row.rstrip())
    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("image")
    parser.add_argument("-w", "--width", type=int, default=70)
    parser.add_argument("-c", "--contrast", type=float, default=1.5)
    parser.add_argument("-i", "--invert", action="store_true")
    parser.add_argument("-o", "--output", default="ascii.txt")
    args = parser.parse_args()

    art = convert(args.image, args.width, args.contrast, args.invert)
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(art)
    print(art)


if __name__ == "__main__":
    main()
