# Batch XLIFF Word Counter

I made this after seeing a job that asked for word counts from 144 XLIFF files. Doing that by hand means opening each file and copying numbers into a sheet. This script does the whole folder in one go and writes an Excel report.

[Watch the 38-second demo video](docs/demo.mp4)

![Results](docs/step4_results.png)

## What it does

It reads XLIFF 1.2 and 2.x files (`.xliff`, `.xlf`, `.sdlxliff`, `.mqxliff`). It skips inline tags like `<ph>` and `<x/>`, so only real text gets counted. By default it counts the source text, and `--target` makes it count the translations instead. Chinese and Japanese don't use spaces, so it counts one word per character for those. If a file can't be read, the report says so on that file's row. It doesn't skip it silently.

The Excel report has a serial number, file name, word count, segments and notes for each file, with a TOTAL row at the bottom.

## What happened when I tested it

I ran it with `--target` on 8 real translation files from the Symfony framework.

| File | Language | Words |
|---|---|---|
| validators.ar.xlf | Arabic | 1,471 |
| validators.de.xlf | German | 1,204 |
| validators.en.xlf | English | 1,309 |
| validators.es.xlf | Spanish | 1,428 |
| validators.fr.xlf | French | 1,456 |
| validators.ja.xlf | Japanese | 2,708 |
| validators.ru.xlf | Russian | 1,139 |
| validators.zh_CN.xlf | Chinese (Simplified) | 1,598 |
| Total | | 12,313 |

That's 1,104 segments in total, with 0 errors. I haven't compared these counts against a CAT tool like MateCat or Trados yet. Those tools treat numbers and repeated segments a bit differently, so their counts can differ.

## Try it

```bash
pip install -r requirements.txt
python scripts/download_data.py        # downloads the 8 test files into data/
python xliff_wordcount.py data --target -o word_counts.xlsx
```

The options are `--target`, `--recursive` and `-o` for the output file.

## Screenshots

| | |
|---|---|
| ![Input](docs/step1_input.png) | ![Run](docs/step2_run.png) |
| ![Output](docs/step3_output.png) | ![Results](docs/step4_results.png) |

## Data and licence

The test files are the Symfony Validator translations from https://github.com/symfony/symfony (branch 7.3, `src/Symfony/Component/Validator/Resources/translations/`), MIT licence, © Fabien Potencier. I didn't commit them here. The download script fetches them.

The code is MIT licensed. See [LICENSE](LICENSE).

Made by Shannu, an engineering student who is new to freelancing.
