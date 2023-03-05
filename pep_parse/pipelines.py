import csv
import datetime as dt
from collections import defaultdict

from scrapy.exceptions import DropItem

from .settings import DATETIME_FORMAT, RESULTS_DIR, BASE_DIR

MESSAGE = 'Удивительно, но у PEP {} - {} статуса нет.'


class PepParsePipeline:
    def open_spider(self, spider):
        self.results = defaultdict(int)

    def process_item(self, item, spider):
        pep_status = item['status']
        if pep_status:
            self.results[pep_status] += 1
        else:
            raise DropItem(MESSAGE.format(item['number'], pep_status))
        return item

    def close_spider(self, spider):
        results_dir = BASE_DIR / RESULTS_DIR
        results_dir.mkdir(exist_ok=True)
        now = dt.datetime.now()
        now_formatted = now.strftime(DATETIME_FORMAT)
        file_name = f'status_summary_{now_formatted}.csv'
        file_path = results_dir / file_name
        with open(file_path, 'w', encoding='utf-8') as f:
            writer = csv.writer(f, dialect=csv.unix_dialect)
            writer.writerows(
                (
                    ('Статус', 'Количество'),
                    *self.results.items(),
                    ('Total', sum(self.results.values()))
                )
            )
