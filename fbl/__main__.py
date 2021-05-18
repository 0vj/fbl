import argparse
import re
import fitz
import requests
import docx
from ODTtoText import odtToText

# a regular expression of URLs
URL_REGEX = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=\n]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"

def print_err(err):
    print('\033[31m {} \033[0m'.format(err))

def txtfamily_extract_text(file_location:str) -> str:
    with open(file_location) as txt:
        text = txt.read()
    return text

#extract raw text from pdf
def pdf_extract_text(file_location:str) -> str:
    # open the PDF file
    with fitz.open(file_location) as pdf:
        text = ""
        for page in pdf:
            # extract text of each PDF page
            text += page.getText()
    return text

#extract text of docx file
def docx_extract_text(file_location:str) -> str:
    docx_file = docx.Document(file_location)
    text = ""
    for paragraph in docx_file.paragraphs:
        text += paragraph.text
    return text

# extract all urls using the regular expression
def find_urls(text:str) -> list:
    urls = [match.group() for match in re.finditer(URL_REGEX, text)]
    print("\033[1;49;34m->\033[0m \033[1mURLs found:\033[0m\n", '\n'.join(urls))
    #print("=======================================")
    return urls

#request to urls and check them
def find_bad_urls(urls) -> list:
    bad_urls = []
    for url in urls:
        print("    \033[1;49;92m==>\033[0m \033[1mCheck: \033[0m", url, end="")
        try :
            res = requests.get(url)
            if not res.ok :
                bad_urls.append(url)
                print(u"\033[31m x\033[0m")
                continue
        except :
            bad_urls.append(url)
            print(u"\033[31m x\033[0m")
            continue
        print(u"\033[1;49;92m \u2713\033[0m")
    return bad_urls

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file_location", help="File location", required=True)
    file_location = parser.parse_args().file_location
    try :
        with open(file_location, 'r'):
            pass
        #if txt family files
        if file_location.endswith((".txt", ".htm", ".html", ".md")):
            bad_urls = find_bad_urls(find_urls(txtfamily_extract_text(file_location)))

        elif file_location.endswith(".pdf"):
            bad_urls = find_bad_urls(find_urls(pdf_extract_text(file_location)))

        elif file_location.endswith(".docx"):
            bad_urls = find_bad_urls(find_urls(docx_extract_text(file_location)))

        elif file_location.endswith(".odt"):
            bad_urls = find_bad_urls(find_urls(odtToText(file_location)))

        else :
            print_err("That file type is not supported")

        print("=======================================")

        print('\033[31m->\033[0m \033[1mBad URLs:\033[0m', "\n".join(bad_urls))

        print("\n\033[1m[*] Total of bad urls: \033[0m", "\033[31m"+str(len(bad_urls))+"\033[0m")

    except FileNotFoundError as exception:
        print_err('File[{}] does not exist: {}'.format(file_location, exception))

    except IOError as exception :
        print_err('File[{}] is not accessible: {}'.format(file_location, exception))


if __name__ == '__main__':
    main()
