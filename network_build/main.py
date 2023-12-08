from data_process import senator_reader, data_reader, init_matrix
from network_dump import network_dump, relation_dump
import csv
import random

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

_file1 = r".\static\data\following-network.json"
_file2 = r".\static\data\coat-network.json"
_file3 = r".\static\data\coexist-network.json"
network_dump(following_mat, senator_info, _file1)
network_dump(coat_mat, senator_info, _file2)
network_dump(coexist_mat, senator_info, _file3)