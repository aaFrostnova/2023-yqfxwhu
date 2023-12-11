from data_process import senator_reader, data_reader, init_matrix
from network_dump import network_dump, relation_dump
import csv
file1 = r".\network_build\following.csv"
file2 = r".\network_build\coat.csv"
file3 = r".\network_build\coexist.csv"
senator_info       = senator_reader()            # 参议员所有的信息
following_dict     = data_reader(filename=file1) # 关注者字典
coat_dict          = data_reader(filename=file2)
coexist_dict       = data_reader(filename=file3)
senator_node_vocab = list(senator_info.keys())                                 # 参议院节点的名字 
following_mat      = init_matrix(following_dict, senator_node_vocab) # 关注者矩阵
num_senator_nodes  = len(senator_node_vocab)
coat_mat           = init_matrix(coat_dict, senator_node_vocab)
coexist_mat        = init_matrix(coexist_dict, senator_node_vocab)

test_idx = senator_node_vocab.index("JohnBoozman")
cnt = 0
for t in range(num_senator_nodes):
    if coat_mat[test_idx, t] == 1:
        cnt += 1
        print(senator_node_vocab[t])
print(coat_dict["JohnBoozman"])
print(cnt)

