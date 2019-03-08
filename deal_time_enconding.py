import pandas as pd
import numpy as np
import os

np.set_printoptions(suppress=True)

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

had_dealed = ['Attack_free_dataset2_Dealed.txt',
              'Attack_free_dataset_Dealed.txt']

for attr in attrs:
    if attr in had_dealed:
        continue
    print("current:",attr)
    # continue

    read_url = source_attr + attr
    dire_url = dire_attr + attr[0: attr.index('.')] + r"_DT.txt"
    # print(read_url,'\n',dire_url)
    # continue
    np.set_printoptions(suppress=True,precision=6)
    data = pd.read_csv(read_url, sep=None, header=None, engine='python', chunksize=10000)#,dtype=np.str

    count = 0
    s1_fir_element = 0

    for o1 in data:

        o1 = o1.dropna(axis=1, how='all')  # how = ['any','all']
        """ print(o1.dtypes)
        0    float64
        1     object
        2      int64
        3     object
        """
        count += 1
        if count%10==0:
            print("loop:",count)
        # continue
        # indexOfDF = o1.shape[0]
        arr = np.insert(o1.loc[:,0].values,0,s1_fir_element,axis=0)
        arr1 = arr[1:]-arr[:-1]# calculate the time difference between before and after
        s1_fir_element = arr[-1]
        # print(len(arr1),arr1)
        # exit()
        # # f = lambda x: int(x)
        # s1_fir_element = arr[-1]
        # # print(s1_fir_element,o1.iloc[-1,0])
        # # exit()
        # s1 = pd.Series(arr[:-1],index=np.arange(indexOfDF))
        # s2 = pd.Series(arr[1:],index=np.arange(indexOfDF))
        # # print(s1,s2)
        # # exit()
        # o1.loc[:,0] = s2.sub(s1).values#s2-s1
        o1.loc[:,0] = arr1#set the columns 0 as the array arr1
        # print("o1.loc[:,0]\t",o1.loc[:,0])
        # print("values\t",o1.loc[:,0].values)
        # exit()
        if count==1:
            o1.loc[0,0] = 0
        # if count==372:
        #     print(s1, s2)
        #     print(s2.sub(s1))
            # print(o1.loc[:,0])
        #     break
        o1.to_csv(dire_url, sep=' ', index=False,header=False,mode='a')#write_url
