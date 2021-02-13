import fitz
import re
import requests
import argparse
import docx

# a regular expression of URLs
url_regex = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=\n]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"

def print_err(err):
    print('\033[31m {} \033[0m'.format(err))

def txtfamily_extract_text(file_location:str):
    with open(file_location) as txt:
         text = txt.read()
    return text

#extract raw text from pdf
def pdf_extract_text(file_location:str):
    # open the PDF file
    with fitz.open(file_location) as pdf:
        text = ""
        for page in pdf:
            # extract text of each PDF page
            text += page.getText()
    return text

#extract text of docx file
def docx_extract_text(file_location:str):
    docx = docx.Document(file_location)
    text = ""
    for paragraph in docx.paragraphs:
        text += paragraphs.text
    return text


#extract text of Mark down file
def md_extract_text():
    pass


# extract all urls using the regular expression
def find_urls(text:str):
    urls = []
    for match in re.finditer(url_regex, text):
        url = match.group()
        urls.append(url)
    print("urls :", urls)
    return urls

#request to urls and check them
def find_bad_urls(urls):
    bad_urls = []
    for url in urls:
        try :
            r = requests.get(url)
            if not r.ok :
                bad_urls.append(url)
        except :
            bad_urls.append(url)
            continue
    return bad_urls

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("-f", "--file_location", help="File location", required=True)
    file_location = parser.parse_args().file_location
    try :
        f = open(file_location, 'r')
        f.close()
        #if txt family files
        if file_location.endswith(".txt", ".htm", ".html", ".md"):
            bad_urls = find_bad_urls(find_urls(txtfamily_extract_text(file_location)))

        elif file_location.endswith(".pdf"):
            bad_urls = find_bad_urls(find_urls(pdf_extract_text(file_location)))

        elif file_location.endswith(".docx"):
            bad_urls = find_bad_urls(find_urls(docx_extract_text(file_location)))

        elif file_location.endswith(".md"):
            bad_urls = find_bad_urls(find_urls(md_extract_text(file_location)))

        else :
            print("That file type is not supported")

        for bad_url in bad_urls:
            print(bad_url)

        print("[*] Total of bad urls:", len(bad_urls))

    except FileNotFoundError as exception:
        print_err('File[{}] does not exist: {}'.format(file_location, exception))

    except IOError as exception :
        print_err('File[{}] is not accessible: {}'.format(file_location, exception))


if __name__ == '__main__':
    main()
