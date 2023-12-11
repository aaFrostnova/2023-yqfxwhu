# 欢迎使用python
from Scweet.scweet import scrape
import csv
from Scweet.utils import get_users_follow
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


following = get_users_follow(users=twitter_names, headless=False, env=None, follow='following')

csv_file_path = '../follows/following.csv'

all_keys = set(key for keys in following.values() for key in keys)

# 打开文件，指定写入模式，newline='' 用于避免写入空行
with open(csv_file_path, 'a', newline='', encoding='utf-8') as csv_file:
    # 创建 CSV 写入器对象
    csv_writer = csv.writer(csv_file)

    # 逐行写入数据
    for username, follows in following.items():
        row_data = [username] + follows
        csv_writer.writerow(row_data)

print(f'CSV 文件已创建：{csv_file_path}')
