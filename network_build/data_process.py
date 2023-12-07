import csv
import os
import numpy as np
def senator_reader():
    #print(os.getcwd())
    senators_file = r".\network_build\senators_of_America.csv"
    senators_info = {}
    with open(senators_file, 'r', encoding="utf-8") as f:
        csv_reader = csv.reader(f)
        header     = next(csv_reader)
        for row in csv_reader:
            office       = row[0]
            office_url   = row[1]
            name         = row[2]
            party        = row[3]
            _            = row[4]
            twitter_name = row[5]
            senators_info[twitter_name]                = {}
            senators_info[twitter_name]["office"]      = office
            senators_info[twitter_name]["offfice_url"] = office_url
            senators_info[twitter_name]["name"]        = name
            senators_info[twitter_name]["party"]       = party
    return senators_info

def data_reader(filename):
    #print(os.getcwd())
    if not os.path.exists(filename):
        print(f"No such file named '{filename}'")
        return None
    
    data_dict = {}
    with open(filename, 'r', encoding="utf-8") as f:
        csv_reader = csv.reader(f)
        #header = next(csv_reader)
        for row in csv_reader:
            center            = row[0]
            around            = row[1:]
            around            = [item for item in around if item]
            around            = [item.replace('@', '') for item in around]
            data_dict[center] = around
    return data_dict

def init_matrix(data_dict, senator_node_vocab):
    num_senator_nodes = len(senator_node_vocab)
    if data_dict == None:
        return np.zeros((num_senator_nodes, num_senator_nodes), dtype=int)

    data_mat         = np.zeros((num_senator_nodes, num_senator_nodes), dtype=int)

    for i in range(num_senator_nodes):
        senator = senator_node_vocab[i] # 取senator姓名
        for name in data_dict[senator]:
            j              = senator_node_vocab.index(name)
            data_mat[i, j] = 1                          # 建立关系：relation(senator1, senator2) = 1

    for k in range(num_senator_nodes):
        data_mat[k, k] = 0
        
    return data_mat

def build_matrix(file1, file2, file3):
    senator_info       = senator_reader()            # 参议员所有的信息
    following_dict     = data_reader(filename=file1) # 关注者字典
    coat_dict          = data_reader(filename=file2) # 同时被@字典
    coexist_dict       = data_reader(filename=file3) # 同时出现字典

    senator_node_vocab = list(senator_info.keys())                                 # 参议院节点的名字
    
    following_mat      = init_matrix(following_dict, senator_node_vocab) # 关注者矩阵
    coat_mat           = init_matrix(coat_dict, senator_node_vocab)      # 同时被@矩阵
    coexist_mat        = init_matrix(coexist_dict, senator_node_vocab)   # 同时出现矩阵

    return following_mat, coat_mat, coexist_mat, senator_info, following_dict, coat_dict, coexist_dict, senator_node_vocab


