import scrapy
from urllib.parse import quote
import hashlib

class SkillsSpider(scrapy.Spider):
    name = "skills"

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def start_requests(self):
        job_search = quote("data analyst")
        hk_urls = [
            f'https://hk.indeed.com/jobs?q={job_search}&start={n}' for n in range(0, 200, 10)
        ]
        ca_urls = [
            f'https://ca.indeed.com/jobs?q={job_search}&start={n}' for n in range(0, 400, 10)
        ]
        for url in ca_urls:
            yield scrapy.Request(url, self.parse_search, meta={'country': 'Canada'})
        # for url in hk_urls:
        #     yield scrapy.Request(url, self.parse_search, meta={'country': 'Hong Kong'})

    def parse_search(self, response):
        for listing_link in response.xpath("//a[contains(@class, 'jcs-JobTitle')]/@href"):
            yield response.follow(listing_link, self.parse_listing, meta={'country': response.meta['country']})

    def parse_listing(self, response):
        position = response.xpath("//h1[contains(@class, 'jobsearch-JobInfoHeader-title')]/text()").get()
        company = response.xpath("//a[contains(@href, '/cmp/')]/text()").get()
        description = response.xpath("//div[contains(@id, 'jobDescriptionText')]//text()").getall()
        country = response.meta['country']
        try:
            location = response.xpath("//div[contains(@class, 'jobsearch-JobInfoHeader-subtitle')]/div//text()").getall()[-1]
        except:
            location = country
        

        item = {
            "_id": hashlib.sha256(f"{position} {company} {location} {country}".encode()).hexdigest(),
            "position": position,
            "company": company,
            "country": country,
            "location": location,
            "description": description,
        }

        yield item