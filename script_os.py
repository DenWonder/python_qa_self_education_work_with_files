import os.path

print("\n\n")
CURRENT_FILE = os.path.abspath(__file__)
CURRENT_DIR = os.path.dirname(CURRENT_FILE)
print(CURRENT_DIR)
print(os.path.abspath('script_open.py'))

TMP_DIR = os.path.join(CURRENT_DIR, 'tmp')