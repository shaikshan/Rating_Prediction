import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO,format='[%(asctime)s]: %(message)s:')


package_name = "Rating"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"{package_name}/__init__.py",
    f"{package_name}/components/__init__.py",
    f"{package_name}/utils/__init__.py",
    f"{package_name}/entity/__init__.py",
    f"{package_name}/config/__init__.py",
    f"{package_name}/pipeline/__init__.py",
    f"{package_name}/constants/__init__.py",
    "configs/config.yaml",
    "configs/schema.yaml",
    "init_setup.sh",
    "requirements.txt",
    "requirements_dev.txt",
    "setup.py",
    "setup.cfg",
    "pyproject.toml",
    "tox.ini",
    "research/trials.ipynb"
]

for file_path in list_of_files:
    file_path = Path(file_path)
    filedir,filename = os.path.split(file_path)
    if filedir !="":
        os.makedirs(filedir,exist_ok=True)
        logging.info(f"Creating directory:{filedir} for file:{filename}")
    if (not os.path.exists(file_path)) or (os.path.getsize(file_path)==0):
        with open(file_path,'w') as f:
            pass #create an empty file
            logging.info(f"Creating empty file:{file_path}")
    else:
        logging.info(f"File already exist:{file_path}")