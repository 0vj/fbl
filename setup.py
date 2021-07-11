import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="fbl",
    version="0.9.2",
    author="Amirmahdi Tafreshi",
    install_requires=["certifi==2020.12.5",
                     "chardet==4.0.0",
                     "idna==2.10",
                     "lxml==4.6.3",
                     "PyMuPDF==1.18.6",
                     "python-docx==0.8.10",
                     "requests==2.25.1",
                     "urllib3==1.26.5",
                     "ODTtoText==0.0.1"],
    author_email="a.tafreshi440@gmail.com",
    description="FBL is tool to find broken links in articles and files",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mr-tafreshi/fbl",
    packages=setuptools.find_packages(),
    entry_points={
        "console_scripts": ["fbl = fbl.__main__:main"],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
