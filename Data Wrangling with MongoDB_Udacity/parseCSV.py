# # 引入CSV模块
# import csv
#
# # 文件路径
# filePath = '/Users/zhangmimi/Git/python/Udacity_用 MongoDB 进行数据整理/beatles-diskography.csv'
#
# with open(filePath) as f:
#     csv_result = csv.DictReader(f, delimiter=',')
#     for v in csv_result:
#         print(v)

# Your task is to read the input DATAFILE line by line, and for the first 10 lines (not including the header)
# split each line on ',' and then for each line, create a dictionary
# where the key is the header title of the field, and the value is the value of that field in the row.
# The function parse_file should return a list of dictionaries,
# each data line in the file being a single list entry.
# Field names and values should not contain extra whitespace, like spaces or newline characters.
# You can use the Python string method strip() to remove the extra whitespace.
# You have to parse only the first 10 data lines in this exercise,
# so the returned list should have 10 entries!
import os
from pprint import pprint

DATADIR = '/Users/zhangmimi/Git/course/Data Wrangling with MongoDB_Udacity'
DATAFILE = 'beatles-diskography.csv'


def parse_file(datafile):
    data = []
    with open(datafile, 'r') as f:
        # 首行已被读过
        fields = f.readline().split(',')
        # for line in f.readlines():
        #     print(line)
        counter = 0
        # 所以到这里首行就不会重新读,在下面就不会出现key和value相等的情况
        for line in f.readlines():
            if counter == 10:
                break

            dataElem = {}
            values = line.split(',')

            for i, v in enumerate(values):
                dataElem[fields[i].strip()] = v.strip()

            data.append(dataElem)
            counter += 1

    return data


def test():
    # a simple test of your implemetation
    datafile = os.path.join(DATADIR, DATAFILE)
    d = parse_file(datafile)
    pprint(d)
    firstline = {'Title': 'Please Please Me', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)',
                 'Released': '22 March 1963', 'US Chart Position': '-', 'RIAA Certification': 'Platinum',
                 'BPI Certification': 'Gold'}
    tenthline = {'Title': '', 'UK Chart Position': '1', 'Label': 'Parlophone(UK)', 'Released': '10 July 1964',
                 'US Chart Position': '-', 'RIAA Certification': '', 'BPI Certification': 'Gold'}

    assert d[0] == firstline
    assert d[9] == tenthline


test()
