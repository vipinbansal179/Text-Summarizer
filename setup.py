import setuptools

with open("README.md","r", encoding="utf-8") as fh:
    long_description = fh.read()

_version_= "0.0.0"

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME = "vipinbansal179"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "bansalvipin36@gmail.com"


setuptools.setup(
    name=REPO_NAME,
    version=_version_,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="Text Summarizer for summarizing the text",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
)