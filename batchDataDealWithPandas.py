import pandas as pd
import numpy as np

# pandas I/O  pandas.pydata.org/pandas-docs/stable/io.html
# data = pd.read_csv(r"/home/gjj/PycharmProjects/ADA/test1.csv")
read_url = "/home/gjj/PycharmProjects/ADA/data/Attack_free_dataset2.txt"
data = pd.read_csv(read_url,sep=None,header=None,engine='python',chunksize=10000)
write_url = "/home/gjj/PycharmProjects/ADA/dealed_data/Attack_free_dataset2_Dealed.txt"
count = 0
for o1 in data:
    # print(o1)
    count +=1
    if count%10==0:
        print("loop:",count)

    o1 = o1.dropna(axis=1, how='all')# how = ['any','all']
    try:
        o1 = o1.drop(columns=[11,39])
    except KeyError:
            pass
    # o1 = o1.astype(np.str)
    # print(o1)
    if count==1:
        o1 = o1.drop(index=[0])
    s1 = pd.Series(o1.loc[:,0])
    s2 = pd.Series(o1.loc[:,7])

    # print(o1.loc[:,4])
    data1 = s1.str.split('\t+',expand=True)
    data2 = s2.str.split('\t+',expand=True)
    # print(data2)

    # def my_test(a,b):
    #     return a+b
    # f = lambda x: str(int(x))+'0'
    data_result = pd.DataFrame()
    data_result['Timeflag'] = data2.loc[:,1]
    data_result['ID'] = data1.loc[:,0]
    data_result['DLC'] = data1.loc[:,1]
    # data_result['message'] = data1.loc[:,2]+o1.loc[:,1].map(f)+o1.loc[:,2]+o1.loc[:,3]+o1.loc[:,4].map(f)+o1.loc[:,5]+o1.loc[:,6]+data2.loc[:,0]
    data_result['message'] = data1.loc[:,2]+o1.loc[:,1]+o1.loc[:,2]+o1.loc[:,3]+o1.loc[:,4]+o1.loc[:,5]+o1.loc[:,6]+data2.loc[:,0]
    # print(data_result)
    data_result.to_csv(write_url, sep=' ', index=False,header=False,mode='a')
