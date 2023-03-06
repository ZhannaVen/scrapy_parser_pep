from pathlib import Path

BOT_NAME = 'pep_parse'

SPIDERS_DIR = 'pep_parse.spiders'

SPIDER_MODULES = [SPIDERS_DIR]

NEWSPIDER_MODULE = SPIDERS_DIR

ROBOTSTXT_OBEY = True

RESULTS_DIR = 'results'

FILE_NAME = 'pep_%(time)s.csv'

FEEDS = {
    f'{RESULTS_DIR}/{FILE_NAME}': {
        'format': 'csv',
        'fields': ['number', 'name', 'status'],
        'overwrite': True
    },
}

BASE_DIR = Path(__file__).parent.parent

DATETIME_FORMAT = '%Y-%m-%d_%H-%M-%S'

ITEM_PIPELINES = {
    'pep_parse.pipelines.PepParsePipeline': 300,
}

PEP_URL = 'peps.python.org'
