import pandas as pd
import numpy as np
import os

source_attr ="/home/gjj/PycharmProjects/ADA/dealed_data/"
dire_attr = "/home/gjj/PycharmProjects/ADA/DT/"
attrs = os.listdir(source_attr)
# print(attrs)
# exit()
# pandas I/O  pandas.pydata.org/pandas-docs/stable/io.html
# data = pd.read_csv(r"/home/gjj/PycharmProjects/ADA/test1.csv")
# read_url = "/home/gjj/PycharmProjects/ADA/dealed_data/Attack_free_dataset_Dealed.txt"

# write_url = "/home/gjj/PycharmProjects/ADA/DT/Attack_free_dataset_DT.txt"
# data1 = pd.read_csv(write_url,sep=None,header=None,engine='python')
# print('sub_r',data1.iloc[-1,0],data1.shape)
# data2 = pd.read_csv(read_url,sep=None,header=None,engine='python')
# print('elements',data2.shape)#data2.iloc[-2:, 0],

had_dealed = ['Attack_free_dataset2_Dealed.txt','Attack_free_dataset_Dealed.txt']
for attr in attrs:
    if attr in had_dealed:
        continue
    print("current:",attr)

    read_url = source_attr + attr
    dire_url = dire_attr + attr[0: attr.index('.')] + r"_DT.txt"
    data = pd.read_csv(read_url, sep=None, header=None, engine='python', chunksize=10000)

    count = 0
    s1_fir_element = 0

    for o1 in data:
        # try:
        o1 = o1.dropna(axis=1, how='all')  # how = ['any','all']
        # print(o1)
        # exit()
        if count%10000==0:
            print("loop:",count)

        indexOfDF = o1.shape[0]
        arr = np.insert(o1.loc[:,0].values,0,s1_fir_element,axis=0)
        # print(arr[0])
        # exit()
        s1_fir_element = arr[-1]
        # print(s1_fir_element)
        # exit()
        s1 = pd.Series(arr[:-1],index=np.arange(indexOfDF),dtype=np.float32)
        s2 = pd.Series(arr[1:],index=np.arange(indexOfDF),dtype=np.float32)

        o1.loc[:,0] = s2.sub(s1).values#s2-s1
        if count==1:
            o1.loc[0,0] = 0
        # if count==372:
        #     print(s1, s2)
        #     print(s2.sub(s1))
            # print(o1.loc[:,0])
        #     break
o1.to_csv(dire_url, sep=' ', index=False,header=False,mode='a')#write_url
