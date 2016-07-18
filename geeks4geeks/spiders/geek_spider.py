import scrapy

class G4GSpider(scrapy.Spider):
	name = "g4gspider"
        allowed_domains = ["geeksforgeeks.org"]
	start_urls = ["http://www.geeksforgeeks.org/data-structures/","http://www.geeksforgeeks.org/fundamentals-of-algorithms/"]
	def parse(self, response):
		filename = response.url.split("/")[-2] + '.html'
		with open(filename, 'wb') as f:
			f.write(response.body)
