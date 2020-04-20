import requests
import pandas as pd
import os
from tqdm import tqdm

import sys, getopt

book_list = ''

def download_book(title, author, doi, pk_name, lang):

    pdf_available = False
    epub_available = False  

    # : is an invalid path symbol
    title = title.replace(':','')
    author = author.replace(':', '')
    doi = doi.replace(':', '')
    pk_name = pk_name.replace(':', '')

    # Create target Directory if don't exist
    dir = os.path.join(os.getcwd(),lang, pk_name,title)
    if not os.path.exists(dir):
        os.makedirs(dir)


    url = 'https://link.springer.com/content/pdf/' + doi + '.pdf'
    pdf_filename = url
    pdf_file = requests.get(url)
    if(pdf_file.status_code == 200):
        pdf_available = True
        pdf_filename = title.replace(',','-').replace('.','').replace('/',' ') + ' - ' + author.replace(', ','+').replace('.','').replace('/',' ') + '.pdf'
        open(os.path.join(dir, pdf_filename), 'wb').write(pdf_file.content)

    url = 'https://link.springer.com/download/epub/' + doi + '.epub'
    epub_filename = url   
    epub_file = requests.get(url)
    if(epub_file.status_code == 200):
        epub_available = True
        epub_filename = title.replace(',','-').replace('.','').replace('/',' ') + ' - ' + author.replace(', ','+').replace('.','').replace('/',' ') + '.epub'
        open(os.path.join(dir, epub_filename), 'wb').write(epub_file.content)

    # print('Downloaded book:\t' + title + '\tPDF: ' + str(pdf_available) + '\tEPUB: ' + str(epub_available))

    if((pdf_available == False and epub_available == False) and not os.listdir(dir)):
        os.rmdir(dir)
        print("Deleted empty directory:\t" + title)


def read_excel_sheet(path):
    df = pd.read_excel(os.path.join(os.getcwd(), path))
    title_col = df['Book Title']
    doiurl_col = df['DOI URL']
    author_col = df['Author']
    eng_packname_col = df['English Package Name']
    de_packname_col = df['German Package Name']

    lang_col = df['Language']

    total_titles = len(title_col)
    

    for i in tqdm(range(total_titles)):
        doi = str((doiurl_col[i].split('/'))[-2]) + "/" + str((doiurl_col[i].split('/'))[-1])

        lang = lang_col[i].strip()
        package_name = ''

        if(lang == 'EN'):
            package_name = eng_packname_col[i].strip()
        elif(lang == 'DE'):
            package_name = de_packname_col[i].strip()

        download_book((title_col[i]).strip(), (author_col[i]).strip(), doi.strip(), package_name, lang)
        # print("Downloaded " + str(i) + " of " + str(total_titles))

def main(argv):
   try:
      opts, args = getopt.getopt(argv,"hi:","ifile=")
   except getopt.GetoptError:
      print('USAGE: test.py -i <inputfile>')
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print('USAGE: test.py -i <inputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         read_excel_sheet(arg)
         print('Download ' + str(arg) + ' complete!')

if __name__ == "__main__":
   main(sys.argv[1:])


