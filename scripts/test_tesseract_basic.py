from pathlib import Path
import pytesseract
from PIL import Image

# CHANGE THIS to any real receipt image you already have
IMG_PATH = Path("invoice-ai/data/samples/img/X00016469670.jpg")
OUT_DIR = Path("scripts/outputs")
OUT_FILE = OUT_DIR / "psm4.txt"

def main():
    if not IMG_PATH.exists():
        raise FileNotFoundError(f"Image not found: {IMG_PATH}")
    OUT_DIR.mkdir(parents=True, exist_ok=True)

    img = Image.open(IMG_PATH)
    custom_oem_psm_config = r'--oem 3 --psm 4'

    text = pytesseract.image_to_string(img,config=custom_oem_psm_config)
    OUT_FILE.write_text(text, encoding="utf-8")

if __name__ == "__main__":
    main()
