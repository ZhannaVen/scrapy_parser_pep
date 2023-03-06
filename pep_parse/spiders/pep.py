import scrapy

from pep_parse.items import PepParseItem
from pep_parse.settings import PEP_URL


class PepSpider(scrapy.Spider):
    name = 'pep'
    allowed_domains = [PEP_URL]
    start_urls = [f'https://{PEP_URL}/']

    def parse(self, response):
        for pep_link in response.css(
            '#numerical-index tbody tr a::attr(href)'
        ):
            yield response.follow(pep_link, callback=self.parse_pep)

    def parse_pep(self, response):
        number, name = (
            response.css('h1.page-title::text').get().split(' – ')
        )
        yield PepParseItem(
            {
                'number': number.split()[1],
                'name': name,
                'status': response.css(
                    'dt:contains("Status") + dd abbr::text'
                ).get()
            }
        )
