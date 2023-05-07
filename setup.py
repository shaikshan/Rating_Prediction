import setuptools

with open("README.md","r",encoding = 'utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Rating_Prediction"
AUTHOR_USER_NAME = "shaikshan"
SRC_REPO = "Rating"
AUTHOR_EMAIL = "shaikroshan1997@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for rating prediction",
    long_description=long_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir= {"":"src"},
    packages= setuptools.find_packages(where="src")
)