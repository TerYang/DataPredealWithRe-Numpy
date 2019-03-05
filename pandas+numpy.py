import pandas as pd
import numpy as np

def writetofile(content, attr2):
    with open(attr2,'a',encoding='utf-8') as f:
        f.write(content + '\n')
        # f.writable()
        # f.writelines(json.dumps(content,ensure_ascii=False)+'\n')

dates = pd.date_range('20190305', periods=6)
pf = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates,
                  columns=['A','B','C','D'])
pf.iloc[0,1] = np.nan
pf.iloc[1,2] = np.nan

# print(pf)
# print(pf['A'], pf.A)#colums selecter
# print(pf[0:3])#selecter rows 0 to row2, selecter with index
# print(pf['20190305':'2019-03-07'])#selecte rows 0 to row2, selecter by flag

# select by label:loc
# print(pf.loc['20190305'])#select row labeled by arr
# print(pf.loc[:,['A', 'B']])#select all rows and colums limited by arr
# print(pf.loc['20190305',['A','B']])#select specific rows and colums limited by arr


#select by position:iloc
# print(pf.iloc[3:5,1:3])
# print(pf.iloc[[1,3,5],1:3])

#mixed selection:ix
# print(pf.ix[:3,['A','C']])#row 0-2,columns A to C


# Boolean indexing:
# print(pf)
# print(pf[pf.A>8])#select all row data large than 8 in colums A
# pf.B[pf.A>4] = 0# only change columns B
# pf['F'] = np.nan
# pf['E'] = pd.Series([i for i in range(1,7)], index=pd.date_range(
#     "20190305",periods=6))#data row index is index.
# print(pf)

# 丢失数据处理，丢弃或者替换dropdown:dropna
# print(pf)
# print(pf.dropna(axis=1, how='any'))# how = ['any','all']
# print(pf.dropna(axis=0, how='any'))# how = ['any','all']

#fill default lost data with arr
# print(pf.fillna(value=0))
# print(np.any(pf.isnull())==True)#any data loss is True
# print(pf.isnull())#lost data is True,else is False


# pandas I/O  pandas.pydata.org/pandas-docs/stable/io.html
# data = pd.read_csv(r"/home/gjj/PycharmProjects/ADA/test1.csv")
data = pd.read_csv(r"/home/gjj/PycharmProjects/ADA/test1.txt",sep=',',delimiter='\t')
# data.to_pickle(r"/home/gjj/PycharmProjects/ADA/test1.pickle")

print(data)
print(data.ID)

