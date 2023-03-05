# scrapy_parser_pep - asynchronous PEP parser (educational project)

### Description

The project obtains data on the statuses of all PEPs) from [peps.python.org](https://peps.python.org/).

Parser outputs the collected information into two .csv files:

- list of all PEPs: number, name and status

- list of summary of PEP statuses: status and number of documents


### Used frameworks and libraries:
- Python 3.7
- Scrapy

### How to start a project (Unix) 
- Clone repository:
```bash
git clone git@github.com:ZhannaVen/scrapy_parser_pep.git
```
- Activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate
```
- Install dependencies:
```bash
pip install -r requirements.txt
```
- The parser is launched from the ./scrapy_parser_pep/
```bash
scrapy crawl pep
```

## Author

- [Zhanna Ventsenostseva](https://github.com/ZhannaVen)

