# FBL(Find/File broken links)

FBL is tool to find broken links in articles and files

![issues](https://img.shields.io/github/issues/mr-tafreshi/fbl)
![repo size](https://img.shields.io/github/repo-size/mr-tafreshi/fbl)
![license](https://img.shields.io/github/license/mr-tafreshi/fbl)
![stars](https://img.shields.io/github/stars/mr-tafreshi/fbl?label=Stars&logo=github)


---


## how it works

FBL finds all the links and checks them all. Any broken link will be displayed to you


## Things tou need in your system

- Python
- Pip
- Git

> Git is not required if you are installing with **pip**


## How to install

- Installing via **pip** :

```bash 
pip3 install fbl
```

**or**

- Get the last update via **git** :

```bash
git clone https://github.com/mr-tafreshi/fbl && cd fbl
pip3 install -e . 
```


## How to run

Run this command in your terminal or CMD :

```bash 
fbl --file_location my.pdf
```

---

### TODO

- [x] .txt support

- [x] .pdf support
- [x] Mark Down Support
- [x] docx support
- [x] .odt support
- [x] .htm and .html support
- [ ] .XLS and XLSX support
- [ ] .PPT and .PPTX support
- [ ] Add GUI version
