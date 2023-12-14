# 欢迎使用python
import pandas as pd

# 读取CSV文件
follows_df = pd.read_csv('content/content_results.csv', encoding='latin-1', header=None)
party_mapping_df = pd.read_csv('美国国会/美国参议院名单.csv', encoding='latin-1')

# 创建一个新的 DataFrame 用于存储计算结果
result_df = pd.DataFrame(columns=['Name', 'Republican', 'Democratic', 'Independent'])

# 遍历 follows_df 中的每一行
for index, row in follows_df.iterrows():
    name = row.iloc[0]
    follows = row.iloc[1:].dropna().tolist()

    # 获取该人的党派
    party = party_mapping_df.loc[party_mapping_df['twitter_name'] == name, 'Party'].values[0]

    # 统计关注的人中各党派的数量
    party_count = {'Republican': 0, 'Democratic': 0, 'Independent': 0}
    for followed_person in follows:
        followed_person = followed_person.replace("@", "")
        followed_party = party_mapping_df.loc[party_mapping_df['twitter_name'] == followed_person, 'Party'].values[0]
        party_count[followed_party] += 1

    # 计算比例并添加到结果表中
    total_follows = len(follows)
    partyA_ratio = party_count['Republican'] / total_follows if total_follows > 0 else 0
    partyB_ratio = party_count['Democratic'] / total_follows if total_follows > 0 else 0
    partyC_ratio = party_count['Independent'] / total_follows if total_follows > 0 else 0

    current_result = pd.DataFrame({'Name': [name], 'Republican': [partyA_ratio], 'Democratic': [partyB_ratio], 'Independent': [partyC_ratio]})
    result_df = pd.concat([result_df, current_result], ignore_index=True)

# 将结果写入新的CSV文件
result_df.to_csv('result.csv', index=False)

# 打印结果
print(result_df)
