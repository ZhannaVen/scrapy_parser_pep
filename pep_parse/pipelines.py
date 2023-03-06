import csv
import datetime as dt
from collections import defaultdict
from .settings import DATETIME_FORMAT, RESULTS_DIR, BASE_DIR


class PepParsePipeline:

    def __init__(self):
        self.results_dir = BASE_DIR / RESULTS_DIR
        self.results_dir.mkdir(exist_ok=True)

    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        pep_status = item['status']
        self.results[pep_status] += 1
        return item

    def close_spider(self, spider):
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = self.results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            csv.writer(
                f,
                dialect=csv.unix_dialect,
                quoting=csv.QUOTE_NONE
            ).writerows(
                (
                    ('Статус', 'Количество'),
                    *self.results.items(),
                    ('Total', sum(self.results.values()))
                )
            )
