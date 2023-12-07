import pandas as pd

# 假设你有一个包含姓名的表 df_names
df_names = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob', 'Eve']
})

# 假设你有一个名字到推特名字的映射表 df_mapping
df_mapping = pd.DataFrame({
    'Name': ['John', 'Alice', 'Bob', 'Eve'],
    'TwitterName': ['john_twitter', 'alice_twitter', 'bob_twitter', 'eve_twitter']
})

# 使用 Pandas 的 merge 函数根据 'Name' 列合并两个表
result_df = pd.merge(df_names, df_mapping, on='Name', how='left')

# 输出结果
print(result_df)
