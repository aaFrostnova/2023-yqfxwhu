import pandas as pd
import os
import csv

# 0. 读取第二张 CSV 表格中的 twitter_name 列表
csv2_path = os.path.join('../美国国会', '美国参议院名单.csv')
df2 = pd.read_csv(csv2_path, encoding='latin-1')
twitter_names = set(df2['Name'])
twitter_mapping = dict(zip(df2['Name'], df2['twitter_name']))

# 1. 读取第一张 CSV 表格
folder_path = '../outputs内容'
output_folder = '../content'
output_csv_path = os.path.join(output_folder, 'content_results.csv')

# 使用 'w' 模式而不是 'a' 模式，以确保在每次运行时都创建一个新的输出文件
with open(output_csv_path, mode='w', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)


for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        # 读取第一个 CSV 文件
        csv1_path = os.path.join(folder_path, filename)
        df1 = pd.read_csv(csv1_path, encoding='latin-1')

        # 获取第一个 CSV 文件名中第一个 '_' 字符前面的字符串
        csv1_name_prefix = os.path.basename(csv1_path).split('_')[0]
        csv1_name_prefix = twitter_mapping.get(csv1_name_prefix, csv1_name_prefix)
        # 2. 提取 Embedded_text 列中的议员名字
        embedded_texts = df1['Embedded_text'].astype(str)
        all_strings = embedded_texts.tolist()

        # 3. 检查第一张表中的项是否存在于第二张表中的名字列表中
        found_twitter_names = set()
        for text in all_strings:
            found_twitter_names.update(twitter_mapping.get(name, name) for name in twitter_names if name in text)

        # 4. 将记录的名字写入新的 CSV 文件
        with open(output_csv_path, mode='a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([csv1_name_prefix] + ['@' + twitter_name for twitter_name in found_twitter_names])

print(f"结果已保存至 {output_csv_path}")
