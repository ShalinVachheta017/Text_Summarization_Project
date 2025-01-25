import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.0"

REPONAME = "Text_Summarization_Project"
AUTHOR_USER_NAME = "shalinvachheta017"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "shalinvachheta2016@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for NLP app",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPONAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)