import random
import json
import os
import shutil

def relation_dump(mat, senator_info, json_file):
    relation_dict = {"nodes" : [], "links": [], "categories": [],}
    senator_node_vocab = list(senator_info.keys())
    num_senator = len(senator_node_vocab)
    party_dict = {"Republican" : 0, "Democratic" : 1, "Independent" : 2}
    for i in range(num_senator):
        tmp = {}
        id = i
        name = senator_node_vocab[i]
        symbolSize = random.uniform(1.5, 30.8)
        x = random.uniform(-500, 500)
        y = random.uniform(-500, 500)
        value = senator_info[name]["party"]
        tmp["id"] = id
        tmp["name"] = name
        tmp["symbolSize"] = symbolSize
        tmp["x"] = x
        tmp["y"] = y
        tmp["value"] = value
        tmp["category"] = party_dict[value]
        relation_dict["nodes"].append(tmp)

    for i in range(num_senator):
        for j in range(num_senator):
            if mat[i, j] == 1:
                tmp = {}
                source = i
                target = j
                tmp["source"] = source
                tmp["target"] = target
                relation_dict["links"].append(tmp)

    categories = [{"name" : "Republican"}, {"name" : "Democratic"}, {"name" : "Independent"}, ]
    relation_dict["categories"] = categories

    json_str = json.dumps(relation_dict, indent=1)
    #print(os.getcwd())
    with open(json_file, "w", encoding="utf-8", newline="\n") as f:
        f.write(json_str)

    destination_path = ".\static\data\\"
    filename = os.path.basename(json_file)
    destination_file = destination_path + filename
    try:
        shutil.copy(json_file, destination_file)
        print(f"The json file has been copied!")
    except FileNotFoundError:
        print(f"The json file was not found!")
    except PermissionError:
        print("Permission is denied!")

