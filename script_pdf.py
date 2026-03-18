import os.path

from pypdf import PdfReader

from script_os import TMP_DIR

reader = PdfReader(os.path.join(TMP_DIR, "sample.pdf"))

print(reader.pages)
print(len(reader.pages))

print(reader.pages[0].extract_text())
print(os.path.getsize(os.path.join(TMP_DIR, "sample.pdf")))


assert "Selenium" in reader.pages[0].extract_text()
assert os.path.getsize(os.path.join(TMP_DIR, "sample.pdf")) >= 6169510