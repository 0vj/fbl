import fitz
import re
import requests
import click

# a regular expression of URLs
url_regex = r"https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=\n]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()@:%_\+.~#?&//=]*)"

def txt_get_text():
    pass

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
def docx_extract_text():
    pass

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
            if r.status_code != 200 :
                bad_urls.append(url)
        except :
            bad_urls.append(url)
            continue
    return bad_urls

@click.command()
@click.option('--file_location', help='location of file')
def main(file_location:str):
    if file_location.endswith(".txt"):
        bad_urls = find_bad_urls(find_urls(txt_extract_text(file_location)))

    elif file_location.endswith(".pdf"):
        bad_urls = find_bad_urls(find_urls(pdf_extract_text(file_location)))

    elif file_location.endswith(".docx"):
        bad_urls = find_bad_urls(find_urls(docx_extract_text(file_location)))

    elif file_location.endswith(".md"):
        bad_urls = find_bad_urls(find_urls(md_extract_text(file_location)))

    for bad_url in bad_urls:
        print(bad_url)

    print("[*] Total of bad urls:", len(bad_urls))


if __name__ == '__main__':
    main()
