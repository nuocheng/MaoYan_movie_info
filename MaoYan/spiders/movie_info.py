import scrapy
import time
import random
class MovieInfoSpider(scrapy.Spider):
    name = 'movie_info'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/films?showType=3&offset=0']
    num=0
#https://maoyan.com/films?showType=3&offset=1980
    def parse(self, response):
        # print(response.text)
        movie_list=response.xpath("//div[@class='movies-list']/dl//dd")
        print(len(movie_list))
        for movie_info in movie_list:
            try:
                info={
                    'movie_id':movie_info.xpath("./div[@class='movie-item film-channel']/a/@href").extract_first().split("/")[-1],
                    'name':movie_info.xpath("./div[@class='channel-detail movie-item-title']/a/text()").extract_first(),
                    'score':str(movie_info.xpath("./div[@class='channel-detail channel-detail-orange']/i[@class='integer']/text()").extract_first())+str(movie_info.xpath("./div[@class='channel-detail channel-detail-orange']/i[@class='fraction']/text()").extract_first()),
                    'image_url':movie_info.xpath("./div[@class='movie-item film-channel']/div[@class='movie-item-hover']/a/img[@class='movie-hover-img']/@src").extract_first(),
                    'type':"".join(str(movie_info.xpath("./div[@class='movie-item film-channel']/div[@class='movie-item-hover']/a/div[@class='movie-hover-info']/div[@class='movie-hover-title']")[1].xpath("./span/following::text()[1]").extract_first()).split()),
                    'main_actor':"".join(str(movie_info.xpath("./div[@class='movie-item film-channel']/div[@class='movie-item-hover']/a/div[@class='movie-hover-info']/div[@class='movie-hover-title']")[2].xpath("./span/following::text()[1]").extract_first()).split()),
                    'release_time':movie_info.xpath("./div[@class='movie-item film-channel']/div[@class='movie-item-hover']/a/div[@class='movie-hover-info']/div[@class='movie-hover-title movie-hover-brief']")[0].xpath("./span/following::text()[1]").extract_first().split()[0],
                }

                print(info)
                yield info
            except:
                print("信息不完整，跳过")
        self.num=self.num+1
        if self.num<=66:
            # for i in range(1,67):
            #     time.sleep(round(random.uniform(0, 1), 2))
            #     url="https://maoyan.com/films?showType=3&offset={}".format(i*30)
            #     print(url)
            #     time.sleep(round(random.uniform(2,4), 2))
            #     yield scrapy.Request(url,callback=self.parse)
            url = "https://maoyan.com/films?showType=3&offset={}".format(self.num * 30)
            print(url)
            time.sleep(round(random.uniform(2, 4), 2))
            yield scrapy.Request(url, callback=self.parse)
