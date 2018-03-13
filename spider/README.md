Python简单爬虫框架结构（Python 2）：

```py
spider_main：爬虫主函数
	├─url_manager：URL管理器（增加、删除、去重URL）
	├─html_downloader：HTML下载器（下载HTML文件到本地）
	├─html_parser：HTML解析器（解析下载到本地的HTML文件）
	└─html_outputer：HTML生成器（结构化输出爬到的数据到HTML文件）
```

