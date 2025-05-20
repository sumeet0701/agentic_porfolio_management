import os
from pathlib import Path
import logging
from setuptools import setup, find_packages
from typing import List

# Configure logging
logging.basicConfig(level=logging.INFO)

# Project setup
while True:
    project_name = input("Enter your project name: ")
    if project_name != '':
        break

logging.info(f"Creating project by name: {project_name}")

list_of_files = [
    f"{project_name}/components/agents/__init__.py",
    f"{project_name}/components/utils/__init__.py",
    f"{project_name}/components/artifacts/__init__.py",
    f"{project_name}/components/config/__init__.py",
    f"{project_name}/Frontend/statics/",
    f"{project_name}/Frontend/templates/",
    f"{project_name}/Backend/api/__init__.py",
    "app.py",
    ".env",
    "requirements.txt",
    "readme.md",
]


# Write requirements to requirements.txt
requirement_list = ["agno", "groq", "llama-index", "langchain"]
with open("requirements.txt", "w") as f:
    for requirement in requirement_list:
        f.write(f"{requirement}\n")

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating a new directory at : {filedir} for file: {filename}")
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
            logging.info(f"Creating a new file: {filename} for path: {filepath}")
    else:
        logging.info(f"file is already present at: {filepath}")

# Setup configuration
PROJECT_NAME = project_name
VERSION = "0.0.1"
AUTHOR = "SUMEET"
DESCRIPTION = "Modular coding of Machine learning project"

REQUIREMENT_FILE_NAME = "requirements.txt"
HYPHEN_E_DOT = "-e ."

def get_requirements_list() -> List[str]:
    """
    Description: This function is going to return list of requirement
    mention in requirements.txt file
    return This function is going to return a list which contain name
    of libraries mentioned in requirements.txt file
    """
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(
    name=PROJECT_NAME,
    version=VERSION,
    author=AUTHOR,
    description=DESCRIPTION,
    packages=find_packages(),
    install_requires=get_requirements_list(),
)
