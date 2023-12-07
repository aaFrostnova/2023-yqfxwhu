# 欢迎使用python
import pandas as pd
import os
import csv

# 0. 读取第二张CSV表格中的twitter_name列表
csv2_path = 'following.csv'
df2 = pd.read_csv(csv2_path)
twitter_names = set(df2['twitter_name'])
# 1. 读取第一张CSV表格
folder_path = 'outputs同时@'
for filename in os.listdir(folder_path):
    if filename.endswith('.csv'):
        # 读取第一个CSV文件
        csv1_path = os.path.join(folder_path, filename)
        df1 = pd.read_csv(csv1_path, encoding='latin-1')
        # 获取第一个 CSV 文件名中第一个 '_' 字符前面的字符串
        csv1_name_prefix = os.path.basename(csv1_path).split('_')[0]


        # 2. 提取Embedded_text列中以@开头的字符串
        embedded_texts = df1['Embedded_text'].astype(str)
        at_mentions = embedded_texts.apply(lambda text: [word[1:]  for word in text.split() if word.startswith('@')])



        # 3. 检查第一张表中的项是否存在于第二张表中的名字列表中
        found_names = set()
        for mentions in at_mentions:
            found_names.update(set(mentions) & twitter_names)

        # 4. 将记录的名字写入新的CSV文件
        output_folder = 'mentions'
        output_csv_path = os.path.join(output_folder, 'mention_results.csv')
        with open(output_csv_path, mode='a', newline='') as csvfile:
            csv_writer = csv.writer(csvfile)
            csv_writer.writerow([csv1_name_prefix] + ['@' + name for name in found_names])

print(f"结果已保存至 {output_csv_path}")
