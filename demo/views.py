from django.shortcuts import render
from django.http import HttpResponse
from network_build.network_dump import network_dump, relation_dump
from network_build.data_process import senator_reader, data_reader, init_matrix
import numpy as np
import os
import random
# Create your views here.

def index(request):
    senator_info = senator_reader()
    random_senators = random.sample(senator_info.keys(), 8)
    senators = {}
    senators["random_senators"] = {}
    senators["senator_info"] = {}
    for tw_name in random_senators:
        senators["random_senators"][tw_name] = senator_info[tw_name]["name"]
    for tw_name, info in senator_info.items():
        _tw_name = "@" + tw_name
        senators["senator_info"][_tw_name] = info["name"]
    return render(request, "./index.html", context=senators)

def graphoverall(request, num):
    file_list = ["following-network.json", "coat-network.json", "coexist-network.json"]
    disp_list = ["Following Network", "Co@ Network", "Coexist Network"]
    senator_info = senator_reader()
    msg = {}
    msg["filename"] = file_list[num]
    msg["dispname"] = disp_list[num]
    msg["senator_info"] = {}
    for tw_name, info in senator_info.items():
        _tw_name = "@" + tw_name
        msg["senator_info"][_tw_name] = info["name"]
    return render(request, "./graph-overall.html", context=msg)

def graphofone(request):
    return render(request, "./graph-of-one.html")

def search(request):
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
    name_map = {}
    for tw_name, info in senator_info.items():
        name_map[tw_name] = info["name"]
    msg = {}
    msg["error"] = None
    msg["Senator"] = None
    msg["filename"] = None
    print("Entering...............")
    if request.method == "GET":
        dic = request.GET
        submit_name = dic["SenatorName"].replace("@", '')
        if submit_name in name_map.keys():
            filename = submit_name
            Senator = name_map[submit_name]
        else:
            filename = [k for k, v in name_map.items() if v == submit_name]
            filename = filename[0]
            Senator = submit_name
        msg["Senator"] = Senator
        msg["filename"] = filename
        if filename == "":
            msg["error"] = f"{submit_name} was not found!"
            return render(request, "./graph-of-one.html", context=msg)
        senator_name = filename
        json_file = ".\static\data\\" + filename + ".json"
        relation_dump(senator_name, senator_info, json_file, mats=[following_mat, coat_mat, coexist_mat])
        return render(request, "./graph-of-one.html", context=msg)