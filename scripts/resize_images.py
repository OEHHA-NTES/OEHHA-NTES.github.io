from PIL import Image
import os

images = [
    "assets/img/data_explorer_logo.png",
    "assets/img/PFAS_pk_app.png",
]
sizes = [480, 800, 1400]

for img in images:
    if not os.path.exists(img):
        print(f"Missing: {img}")
        continue
    im = Image.open(img)
    base, ext = os.path.splitext(img)
    for w in sizes:
        if im.width <= w:
            # If original is smaller than target, copy original (but still ensure png)
            out = f"{base}-{w}.png"
            im.save(out, format="PNG")
            print(f"Saved (copied): {out}")
            continue
        h = int(im.height * (w / im.width))
        out = f"{base}-{w}.png"
        im.resize((w, h), Image.LANCZOS).save(out, format="PNG")
        print(f"Saved: {out}")
