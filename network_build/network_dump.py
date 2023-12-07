import random
import json
import os
import shutil

def network_dump(mat, senator_info, json_file):
    relation_dict = {"nodes" : [], "links": [], "categories": [],}
    senator_node_vocab = list(senator_info.keys())
    num_senator = len(senator_node_vocab)
    category_dict = {"Republican" : 0, "Democratic" : 1, "Independent" : 2}
    category_list = list(category_dict.keys())
    for i in range(num_senator):
        tmp = {}
        id = f"n{i}"
        name = senator_node_vocab[i]
        symbolSize = random.uniform(1.5, 30.8)
        x = random.uniform(-500, 500)
        y = random.uniform(-500, 500)
        value = senator_info[name]
        tmp["id"] = id
        tmp["name"] = name
        tmp["symbolSize"] = symbolSize
        tmp["x"] = x
        tmp["y"] = y
        tmp["value"] = value
        tmp["category"] = category_dict[value["party"]]
        relation_dict["nodes"].append(tmp)

    for i in range(num_senator):
        for j in range(num_senator):
            if mat[i, j] == 1:
                tmp = {}
                source = f"n{i}"
                target = f"n{j}"
                tmp["source"] = source
                tmp["target"] = target
                relation_dict["links"].append(tmp)

    categories = [{"name" : "Republican"}, {"name" : "Democratic"}, {"name" : "Independent"}, ]
    relation_dict["categories"] = categories

    json_str = json.dumps(relation_dict, indent=1)
    #print(os.getcwd())
    with open(json_file, "w", encoding="utf-8", newline="\n") as f:
        f.write(json_str)


def relation_dump(senator_name, senator_info, json_file, mats):
    relation_dict = {"nodes" : [], "links": [], "categories": [],}
    senator_node_vocab = list(senator_info.keys())
    num_senator = len(senator_node_vocab)
    center_id = senator_node_vocab.index(senator_name)
    category_dict = {"Center" : 0, "Following" : 1, "Coat" : 2, "Coexist" : 3, }
    category_list = list(category_dict.keys())
    categories = [{"name" : "Center"}, {"name" : "Following"}, {"name" : "Co@"}, {"name" : "Coexist"}, ]
    relation_dict["categories"] = categories
    center_node = {"id":f"n{center_id}", "name":senator_name, "symbolSize":30.8, "x":0, "y":0, "value":senator_info[senator_name], "category":0}
    relation_dict["nodes"].append(center_node)
    cnt = 0
    for i in range(3):
        category = category_list[i+1]
        mat = mats[i]
        for j in range(num_senator):
            if cnt == center_id:
                cnt += 1
            tmp = {}
            id = cnt
            name = senator_node_vocab[j]
            symbolSize = random.uniform(1.5, 30.8)
            x = random.uniform(-500, 500)
            y = random.uniform(-500, 500)
            value = senator_info[name]
            tmp["id"] = f"n{id}"
            tmp["name"] = name
            tmp["symbolSize"] = symbolSize
            tmp["x"] = x
            tmp["y"] = y
            tmp["value"] = value
            tmp["category"] = category_dict[category]
            relation_dict["nodes"].append(tmp)
            if mat[center_id, j] == 1:
                tmp = {}
                source = center_id
                target = id
                tmp["source"] = f"n{source}"
                tmp["target"] = f"n{target}"
                relation_dict["links"].append(tmp)
            cnt += 1
    json_str = json.dumps(relation_dict, indent=1)
    #print(os.getcwd())
    with open(json_file, "w", encoding="utf-8", newline="\n") as f:
        f.write(json_str)
