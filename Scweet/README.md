# 美国国会议员社交网络分析

## 1. 安装：

```sh
git clone https://github.com/aaFrostnova/teamyqfx.git
cd teamyqfx
```

## 2. 推特数据爬取指南

### **爬虫工具：**

[Scweet](https://github.com/Altimis/Scweet)，chromedriver（根据自己的Google浏览版本确定对应版本）

### **Python环境要求：**

```python
certifi
selenium==4.2.0
pandas
python-dotenv
chromedriver-autoinstaller
geckodriver-autoinstaller
urllib3
```

###  **配置设置：**

Scweet/Scweet/utils.py line 150，更换为自己的Google浏览器缓存所在路径

```python
 options.add_argument('--user-data-dir=%s' % r"C:\Users\...\AppData\Local\Google\Chrome\User Data")
```

Scweet/Scweet/utils.py line 157，更换为自己的chromedriver.exe所在路径

```python
 if firefox:
        driver = webdriver.Firefox(options=options, executable_path=driver_path)
    else:
        driver = webdriver.Chrome(options=options, executable_path=r"C:\Users\...\AppData\Local\Google\Chrome\Application\chromedriver.exe")
```

### 爬取关注的议员

结果存放在  **follows/following筛选.csv**  中：

```sh
cd Scweet
python scripts/get_following.py
python scripts/transfer.py
```

### 爬取共现的议员

结果存放在 **mention/mention_results.csv** 里：

```sh
python scripts/get_mention.py
python scripts/extract_mention.py
```

### 爬取在同一个推特内容中一起出现的议员

结果存放在 **content/content_results.csv** 里：

```sh
python scripts/get_content.py
python scripts/extract_content.py
```



