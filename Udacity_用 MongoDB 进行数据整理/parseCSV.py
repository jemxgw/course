# 引入CSV模块
import csv

# 文件路径
filePath = '/Users/zhangmimi/Git/python/Udacity_用 MongoDB 进行数据整理/beatles-diskography.csv'

with open(filePath) as f:
    csv_result = csv.DictReader(f, delimiter=',')
    for v in csv_result:
        print(v)
