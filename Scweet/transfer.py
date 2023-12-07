import csv

# 读取CSV文件，提取第一列的元素作为list1
with open('following.csv', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

# 加上@字符并形成list1
list1 = ['@' + row[0] for row in data]

# 处理每一行，找到匹配的元素并保存结果
result_data = []

for row in data:
    name = row[0]
    matching_elements = [element for element in row[1:] if element in list1]
    result_row = [name] + matching_elements
    result_data.append(result_row)

# 保存结果为新的CSV文件
with open('result.csv', 'w', newline='') as result_file:
    writer = csv.writer(result_file)
    writer.writerows(result_data)
