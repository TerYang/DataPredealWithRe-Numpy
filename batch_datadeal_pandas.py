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
print(data)
print(data.loc[:,4])
data1 = s1.str.split('\t+',expand=True)
data2 = s2.str.split('\t+',expand=True)
print(data1,data2)

def my_test(a,b):
    return a+b

data3 = data.apply(lambda column:my_test(data.loc[:,2],data.loc[:,3]),axis=1 )
print(data3)
# print(data)