import scrapy


class AnimeSpider(scrapy.Spider):
    # 爬虫名称
    name = "anime"
    # 允许的域名
    allowed_domains = ["yuc.wiki"]
    # 起始页面url
    start_urls = ["https://yuc.wiki/?utm_source=xinquji"]

    def parse(self, response):  # 默认是用来处理解析的
        # print(response)
        # print(response.text)
        txt = response.xpath("/html/body/div/main/div/div[1]/div/article/div[1]/div[5]/div[2]/div/table/tbody/tr[1]/td")
        print(txt)

