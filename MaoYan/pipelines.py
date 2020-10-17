# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import json
from openpyxl import Workbook
import os
class MaoyanPipeline:
    def __init__(self):
        self.wb=Workbook()
        self.ws=self.wb.active
        self.ws.append(['movie_id','name','score','image_url','type','main_actor','release_time'])
    def process_item(self, item, spider):
        #创建json文件
        line = json.dumps(dict(item))
        if os.path.exists("../data.json"):

            with open("./data.json",'a+') as f:
                f.write(line+"\n")
        else:

            with open("./data.json", 'a+') as f:
                f.write(line)

        #创建excel
        line = [item['movie_id'], item['name'], item['score'], item['image_url'], item['type'],item['main_actor'],item['release_time']]
        self.ws.append(line)
        self.wb.save('./movie.xlsx')
        return item


