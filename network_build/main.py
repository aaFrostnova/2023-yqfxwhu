from data_process import senator_reader, analysis_reader, data_reader, init_matrix, build_matrix
from network_dump import network_dump, relation_dump
import csv
import random

file1 = r".\network_build\following.csv"
file2 = r".\network_build\coat.csv"
file3 = r".\network_build\coexist.csv"
following_mat, coat_mat, coexist_mat, senator_info, _, _, _, _ = build_matrix(file1, file2, file3)
analysis_info      = analysis_reader()


_file1 = r".\static\data\following-network.json"
_file2 = r".\static\data\coat-network.json"
_file3 = r".\static\data\coexist-network.json"
network_dump(following_mat, senator_info, _file1)
network_dump(coat_mat, senator_info, _file2)
network_dump(coexist_mat, senator_info, _file3)