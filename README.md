# SpringerBooksCOVID19

This script downloads all books that were made freely available by SpringerNature during the COVID-19 pandemic.

## Requires
```sh
requests | pandas | xlrd | os | tqdm | sys | getopt 
```

## Usage
Place the script in the desired download location and run. The excel files containing the book information need to be passed in as an argument to the script.   

### Input Example
```sh
./SpringerBatchDownload.py -i EnglishBooks.xlsx
```

### Help
```sh
./SpringerBatchDownload.py -h
```

## Output
Both PDF and EPUB versions are downloaded for each title in a folder within the speciality folder which is located. These files are stored by language given that both English and German books were made available.

### Example Folder structure
```sh
.
+-- SpringerBatchDownload.py
+-- EnglishBooks.xlsx
+-- GermanBooks.xlsx
+-- EN
|   +-- Medicine
|   |   +-- [Book Title]
|   |   |   +-- .PDF
|   |   |   +-- .EPUB (if available)
|   |   ...
|   ...
|   +-- Engineering
|   |   +-- [Book Title]
|   |   |   +-- .PDF
|   |   |   +-- .EPUB (if available)
|   |   ...
+-- DE
    +-- Medizin
    |   +-- [Buch Titel]
    |   |   +-- .PDF
    |   |   +-- .EPUB (wenn verfügbar)
    |   ...
    ...
    +-- Technik & Informatik
    |   +-- [Buch Titel]
    |   |   +-- .PDF
    |   |   +-- .EPUB (wenn verfügbar)
    |   ...
```
