from scrapy import cmdline

cmdline.execute('scrapy crawl car2 -o car2.csv'.split())
# cmdline.execute('scrapy crawl car2 -o car2.json'.split())
