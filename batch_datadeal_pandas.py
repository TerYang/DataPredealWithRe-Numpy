import pandas as pd
import numpy as np

def writetofile(content, attr2):
    with open(attr2,'a',encoding='utf-8') as f:
        f.write(content + '\n')
        # f.writable()
        # f.writelines(json.dumps(content,ensure_ascii=False)+'\n')

# pandas I/O  pandas.pydata.org/pandas-docs/stable/io.html
# data = pd.read_csv(r"/home/gjj/PycharmProjects/ADA/test1.csv")
data = pd.read_csv(r"/home/gjj/PycharmProjects/ADA/test1.txt",sep=None,
                   header=None,engine='python')
# # read txt,deal with pandas.errors.
# ParserError: Error tokenizing data. C error: Expected 1 fields in line 121, saw 2
# data = pd.read_csv(r"/home/gjj/PycharmProjects/ADA/test1.txt",sep=' ',delimiter='\t',)
#names , nrows:0-arr rows, chunksize:bathc size: sep='\s+'
# data.to_pickle(r"/home/gjj/PycharmProjects/ADA/test1.pickle")
# print(data)
global i#i is columns
for i in data:
    pass
# for column in range(i):
data = data.dropna(axis=1, how='all')# how = ['any','all']
data = data.drop(columns=[16,39])
data = data.drop(index=[0])
s1 = pd.Series(data.loc[:,0])
s2 = pd.Series(data.loc[:,7])

# print(data.loc[:,4])
data1 = s1.str.split('\t+',expand=True)
data2 = s2.str.split('\t+',expand=True)
print(data2)

# print(data1,data2)

def my_test(a,b):
    return a+b

# print(data)

f = lambda x: str(int(x))+'0'
# print(data.loc[:,1].map(f))
# print(max(data.index))
# exit()
# print(data1.loc[:,2]+data.loc[:,1].map(f)+
# data.loc[:,2]+data.loc[:,3]+data.loc[:,4].map(f)+data.loc[:,5]+data.loc[:,6]+data2.loc[:,0])
data_result = pd.DataFrame()
# data_result = pd.DataFrame([data2.loc[:,1],data1.loc[:,0],data1.loc[:,1],data1.loc[:,2]+data.loc[:,1].map(f)+
# data.loc[:,2]+data.loc[:,3]+data.loc[:,4].map(f)+data.loc[:,5]+data.loc[:,6]++data2.loc[:,0]],index=list(data.index),columns=['Timeflag','ID','DLC','message'])
data_result['Timeflag'] = data2.loc[:,1]
data_result['ID'] = data1.loc[:,0]
data_result['DLC'] = data1.loc[:,1]
data_result['message'] = data1.loc[:,2]+data.loc[:,1].map(f)+data.loc[:,2]+data.loc[:,3]+data.loc[:,4].map(f)+data.loc[:,5]+data.loc[:,6]++data2.loc[:,0]
print(data_result)
data_result.to_csv(r"/home/gjj/PycharmProjects/ADA/result1.txt",sep=' ',index=False,header=False)
# data3 = data.apply(lambda column:my_test(data.loc[:,2],data.loc[:,3]))
# data3.to_csv(r"/home/gjj/PycharmProjects/ADA/result1.txt")
# print(data)