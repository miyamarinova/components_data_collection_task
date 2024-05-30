import scrapy

class ComponentSpider(scrapy.Spider):
    name = 'components'
    start_urls=['https://desktop.bg/computers-all']

    def parse(self, response):
        # Iterate through the product elements
        products = response.css('#products-container > ul')
        for product in products:
            processors = product.css('li > article > a > ul > li:nth-child(1)::text').getall()
            gpus = product.css('li > article > a > ul > li:nth-child(2)::text').getall()
            motherboards = product.css('li > article > a > ul > li:nth-child(3)::text').getall()
            rams = product.css('li > article > a > ul > li:nth-child(4)::text').getall()
            yield {
                'processors': processors,
                'gpus': gpus,
                'motherboards': motherboards,
                'rams': rams,
            }

        next_page = response.css('#products-container > ul > li.next-page > a::attr(href)').get()
        if next_page is not None:
            # Follow the link to the next page and parse it
            yield response.follow(next_page, callback=self.parse)




