#### 运行环境

- ##### scrapy

- ##### openpyxl

- ##### lxml

#### 运行

1. 克隆项目

   ~~~git
   git clone https://github.com/nuocheng/MaoYan_movie_info.git
   ~~~

   

2. 使用cmd进入项目中

   ~~~git
   cd 位置/maoyan
   ~~~

3. 然后输入

   ~~~cmd
   scrapy crawl movie_info
   ~~~

4. 程序运行完后，会在maoyan文件下生成两个文件（json,excel）

   爬取的数据存在里面（数据内容是一样的，只是格式不同）

#### 代码爬取时间控制

```python
time.sleep(round(random.uniform(2, 4), 2))
```

该句在项目中（maoyan\MaoYan\spiders\movie_info.py文件里）40行位置处，为了防止爬取速度过快、被禁





#####  介绍

- 项目名：猫眼爬虫
- 编写者：张程东
- 邮箱：1642342180@qq.com
- 微信：17853317980