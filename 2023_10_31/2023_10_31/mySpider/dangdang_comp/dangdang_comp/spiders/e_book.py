import scrapy


class EBookSpider(scrapy.Spider):
    name = "e_book"
    allowed_domains = ["e.dangdang.com"]
    start_urls = ["http://e.dangdang.com/list-JSJWL-dd_sale-0-1.html"]

    def parse(self, response):
        # 获取页面中所有书的名称信息
        # txt = response.xpath("//div[@class='bookinfo']/div[@class='title']/text()").extract()
        # print(txt)

        # 分块提取数据
        book_list = response.xpath("//div[@class='bookinfo']")
        for book in book_list:
            title = book.xpath("./div[@class='title']/text()").extract_first()
            author = book.xpath("./div[@class='author']/text()").extract_first()
            price = book.xpath("./div[@class='price']/span[@class='now']/text()").extract_first()
            introduction = book.xpath("./div[@class='des']/text()").extract_first()

            dic = {
                "title": title,
                "author": author,
                "price": price,
            }

            yield dic
        pass
