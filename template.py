import os
from pathlib import Path
import logging
 
logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:') 

list_of_files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "requirments.txt",
    "setup.py",
    "app.py",
    "research/trials.ipynb"
]

for filepath in list_of_files:
    filepath = Path(filepath)  # Convert to Path object
    filedir, filename = os.path.split(filepath.as_posix())  # Use as_posix for consistency

    if filedir:  # Check if directory path is not empty
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir} for the file {filename}")

    if not filepath.exists() or filepath.stat().st_size == 0:
        with open(filepath, 'w') as f:
            logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"{filename} is already created")
