# 欢迎使用python
from Scweet.scweet import scrape
import csv
import time

def read_twitter_names(filename):
    twitter_names = []
    with open(filename, 'r', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            twitter_name = row['twitter_name']
            twitter_names.append(twitter_name)
    return twitter_names

filename = r'G:\project\twint\Scweet\美国国会\美国参议院名单.csv'  # 请确保文件名正确，并且与脚本文件在同一目录下
twitter_names = read_twitter_names(filename)


# following = get_users_follow(users=twitter_names, headless=False, env=None, follow='following')
'''data = scrape(words='@'+twitter_names[1], from_account=None, since="2023-10-20",
                  until="2023-10-30", mention_account=None,
                interval=1,
                headless=False, display_type="Latest", save_images=False, proxy="127.0.0.1:7890", save_dir='outputs同时@',
                resume=False, filter_replies=True, proximity=False) 
'''
# time.sleep(300)
for twitter_name in twitter_names:
    data = scrape(words=None, from_account=None, since="2023-11-1",
                    until="2023-11-15", mention_account=twitter_name,
                    interval=1,
                    headless=False, display_type="Latest", save_images=False, proxy="127.0.0.1:7890", save_dir='../outputs同时@',
                    resume=False, filter_replies=True, proximity=False)


