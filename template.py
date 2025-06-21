import os
from pathlib import Path
import logging

# Setup logging
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s')

# List of files to create
list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

# Loop through each file path
for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    # Create directory if needed
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file: {filename}")

    # Create the file if it doesn't exist or is empty
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} already exists")
