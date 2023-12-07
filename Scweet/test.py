from Scweet.scweet import scrape
from Scweet.utils import init_driver, log_in
import csv
import time
from Scweet.utils import get_users_follow
def read_twitter_names(filename):
    twitter_names = []
    with open(filename, 'r', encoding='latin-1') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            twitter_name = row['Name']
            twitter_names.append(twitter_name)
    return twitter_names

filename = r'G:\project\twint\Scweet\美国国会\美国参议院名单.csv'  # 请确保文件名正确，并且与脚本文件在同一目录下
names = read_twitter_names(filename)


# following = get_users_follow(users=twitter_names, headless=False, env=None, follow='following')
'''data = scrape(words='@'+twitter_names[1], from_account=None, since="2023-10-20",
                  until="2023-10-30", mention_account=None,
                interval=1,
                headless=False, display_type="Latest", save_images=False, proxy="127.0.0.1:7890", save_dir='outputs同时@',
                resume=False, filter_replies=True, proximity=False) 
'''
time.sleep(300)
for name in names[15:]:
    data = scrape(words=name, from_account=None, since="2023-11-1",
                    until="2023-11-15", mention_account=None,
                    interval=1,
                    headless=False, display_type="Latest", save_images=False, proxy="127.0.0.1:7890", save_dir='outputs内容',
                    resume=False, filter_replies=True, proximity=False)



# ['@ifenglobal', '@nytchinese', '@PDChinese']
# 指定要保存的CSV文件路径
'''
csv_file_path = 'following.csv'

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
'''