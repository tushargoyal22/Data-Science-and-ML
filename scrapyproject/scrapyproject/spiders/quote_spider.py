import scrapy

class QuotesSpider(scrapy.Spider):
	name="quotes_spider"

	def start_request(self):

		url=[
		'http://quotes.toscrape.com/page/1/',
		'http://quotes.toscrape.com/page/2/'
		]

		# Generator function

		for url in urls:
			yield scrapy.Request(url=url,callback= self.parse)



	def parse(self,response):

		page_id= response.url.split("/")[-2]
		filename="quotes-%s"%page_id
		
		with open(filename,'wb') as f:
			f.write(response.body)
		self.log('Saved file %s'% filename) 