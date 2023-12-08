from data_process import senator_reader, data_reader, init_matrix
from network_dump import network_dump, relation_dump
import csv
import random

senator_info = senator_reader()
submit_name = "Katie Britt"
if submit_name not in senator_info.keys():
    matched_keys = [key for key, value in senator_info.items() if value["name"] == submit_name]
    senator_file = matched_keys[0]
print(matched_keys)