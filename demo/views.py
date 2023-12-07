from django.shortcuts import render
from django.http import HttpResponse
from network_build.network_dump import network_dump, relation_dump
from network_build.data_process import senator_reader, data_reader, init_matrix
import numpy as np
import os
# Create your views here.
def hello(request, num):
    return HttpResponse(f"Hello world{num}!")

def index(request):
    context = {
        "news_list" : [
            {
                "title":"第一篇新闻",
                "content":"哈哈哈哈成功了",
            },
            {
                "title":"第二篇新闻",
                "content":"哈哈哈哈又成功了",
            },
        ]
    }
    return render(request, "./index.html", context=context)

def graph(request):
    return render(request, "./graph-label-overlap.html")

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
    msg = {}
    msg["error"] = None
    if request.method == "GET":
        dic = request.GET
        msg["filename"] = dic["SenatorName"] + ".json"
        msg["Senator"] = dic["SenatorName"]
        if msg["Senator"] not in senator_node_vocab:
            msg["error"] = f"{msg['Senator']} was not found!"
            return render(request, "./index.html", context=msg)
        json_file = ".\static\data\\" + msg["filename"]
        if not os.path.exists(json_file):
            relation_dump(msg["Senator"], senator_info, json_file, mats=[following_mat, coat_mat, coexist_mat])
        return render(request, "./graph-of-one.html", context=msg)
    
def page1(request):
    return render(request, "./page1.html")

def page2(request):
    return render(request, "./page2.html")

def page3(request):
    return render(request, "./page3.html")