from data_process import senator_reader, data_reader, init_matrix
from network_dump import network_dump, relation_dump
import json
import numpy as np
file1 = r".\network_build\following.csv"
senator_info       = senator_reader()            # 参议员所有的信息
following_dict     = data_reader(filename=file1) # 关注者字典
coat_dict          = {}
coexist_dict       = {}
senator_node_vocab = list(senator_info.keys())                                 # 参议院节点的名字 
following_mat      = init_matrix(following_dict, senator_node_vocab) # 关注者矩阵
num_senator_nodes  = len(senator_node_vocab)
coat_mat           = np.zeros((num_senator_nodes, num_senator_nodes), dtype=int)
coexist_mat        = np.zeros((num_senator_nodes, num_senator_nodes), dtype=int)
# 总体关注者网络图
json_file1         = r".\network_build\following-network.json"
network_dump(following_mat, senator_info, json_file1)

# SenKatieBritt个人网络建立
json_file2         = r".\network_build\SenKatieBritt.json"
relation_dump("SenKatieBritt", senator_info, json_file2, mats=[following_mat, coat_mat, coexist_mat])






