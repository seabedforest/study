from scrapy import cmdline

# cmdline.execute('scrapy crawl car2 -o car.csv'.split())
cmdline.execute('scrapy crawl car2 -o car.json'.split())
