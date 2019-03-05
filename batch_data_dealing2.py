import numpy as np
import pandas as pd
import re
import os

# current_atrr = os.getcwd()
# print(current_atrr)


def writetofile(content, attr2):
    with open(attr2,'a',encoding='utf-8') as f:
        f.write(content + '\n')
        # f.writable()
        # f.writelines(json.dumps(content,ensure_ascii=False)+'\n')


def dealingdata(arr1,arr2):
    data = np.loadtxt(arr1, delimiter=",", dtype=np.str, encoding='utf-8')
    print("total data row numbers:",data.shape[0])

    data = np.array(data).reshape(data.shape[0], -1)
    pattern = re.compile(".*Timestamp:|ID:|DLC:(.*?)']", re.S)
    pattern2 = re.compile("\s+", re.S)
    # qs = np.array()
    for i in range(data.shape[0]):
        if i%5000==0:
            print("current row:",i)
        ls = []
        string = str(data[i, :])
        # print(string)
        results = re.split(pattern, string)
        # print(results, results.__len__())
        for result in results:
            if result is not None or not " ":
                # print(result.strip())
                ls.append(result.strip())
            elif result == ' ':
                pass
        # print(ls[1:-1])
        q = ls[1:-1]
        f = []
        for j in q:
            if ' ' not in j:
                f.append(j)
            else:
                o = ''
                res = re.split(pattern2, j)
                if q.index(j) == 2:
                    f.append(res.pop(0))
                for r in res:
                    o += r.strip()
                f.append(o)
        # print(f)
        if f.__len__()<4:
            f.append("None")
        strf = ""
        for fi in f:
            strf += fi + " "
        writetofile(strf, arr2)


if __name__ == "__main__":
    r = r"/home/gjj/PycharmProjects/ADA/data/"
    current_atrr = os.listdir(r)
    current_atrr1 = []
    for i in range(7):
        # if i==2 or i==4 or i==6:
        # if i==5:
        if i==0 or i==1:
            current_atrr1.append(current_atrr[i])

    #         print(i)
    # print(current_atrr1)
    # exit()
    for attr in current_atrr1:
        attr1 = r
        attr1 += attr
        print(current_atrr1.index(attr))
        print("dealing:",attr)
        # ll = dealingdata(attr1)
        # attr2 = attr1[0: attr1.index('.')] + r"_Dealed.txt"
        attr2 = r"/home/gjj/PycharmProjects/ADA/dealed data/" + attr[0: attr.index('.')]+r"_Dealed.txt"
        dealingdata(attr1, attr2)