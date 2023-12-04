from data_process import senator_reader, data_reader, init_matrix
from network_dump import relation_dump
import json
file1 = r".\network_build\following.csv"
senator_info       = senator_reader()            # 参议员所有的信息
following_dict     = data_reader(filename=file1) # 关注者字典
coat_dict          = {}
coexist_dict       = {}
senator_node_vocab = list(senator_info.keys())                                 # 参议院节点的名字 
following_mat      = init_matrix(following_dict, senator_node_vocab) # 关注者矩阵

# 关注者网络图
json_file1         = r".\network_build\following-network.json"
relation_dump(following_mat, senator_info, json_file1)






