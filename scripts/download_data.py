"""Download the 8 Symfony Validator XLIFF files (MIT licence) into data/."""
import urllib.request
from pathlib import Path
BASE = "https://raw.githubusercontent.com/symfony/symfony/7.3/src/Symfony/Component/Validator/Resources/translations/"
out = Path(__file__).resolve().parent.parent / "data"
out.mkdir(exist_ok=True)
for lang in ["ar", "de", "en", "es", "fr", "ja", "ru", "zh_CN"]:
    name = f"validators.{lang}.xlf"
    urllib.request.urlretrieve(BASE + name, out / name)
    print("saved", out / name)
