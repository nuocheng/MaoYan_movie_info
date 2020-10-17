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
   cd 位置/MaoYan_movie_info
   ~~~

3. 然后输入

   - 如果使用conda，先进入**运行环境**，然后执行下面命令
   - 如果是用本地Python中的运行环境，可直接执行下面命令

   ~~~cmd
   scrapy crawl movie_info
   ~~~

4. 程序运行完后，会在maoyan文件下生成两个文件（json,excel）

   爬取的数据存在里面（数据内容是一样的，只是格式不同）



##### movie.xlsx，data.json是已经爬完后的数据文件，可以直接查看



#### 代码爬取时间控制

```python
time.sleep(round(random.uniform(2, 4), 2))
```

该句在项目中（MaoYan_movie_info\MaoYan\spiders\movie_info.py文件里）40行位置处，为了防止爬取速度过快、被禁





#####  介绍

- 项目名：猫眼爬虫
- 编写者：张程东
- 邮箱：1642342180@qq.com
- 微信：17853317980