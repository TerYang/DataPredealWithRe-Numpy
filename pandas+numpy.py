import pandas as pd
import numpy as np

def writetofile(content, attr2):
    with open(attr2,'a',encoding='utf-8') as f:
        f.write(content + '\n')
        # f.writable()
        # f.writelines(json.dumps(content,ensure_ascii=False)+'\n')

# dates = pd.date_range('20190305', periods=6)
# pf = pd.DataFrame(np.arange(24).reshape((6,4)), index=dates,
#                   columns=['A','B','C','D'])
# pf.iloc[0,1] = np.nan
# pf.iloc[1,2] = np.nan

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
# data = pd.read_csv(r"/home/gjj/PycharmProjects/ADA/test1.txt",sep=None,header=None,engine='python')
# # read txt,deal with pandas.errors.ParserError: Error tokenizing data. C error: Expected 1 fields in line 121, saw 2
# data = pd.read_csv(r"/home/gjj/PycharmProjects/ADA/test1.txt",sep=' ',delimiter='\t',)
#names , nrows:0-arr rows, chunksize:bathc size:
# data.to_pickle(r"/home/gjj/PycharmProjects/ADA/test1.pickle")

# print(data[0:4][3:6])
# # print(data[0:2])
# print(data['ID'])


# merging data:concat
# data1 = data
# data2 = data
# data3 = data
#
# res = pd.concat([data,data1,data2,data3],axis=0,ignore_index=True)
# # reconstruct row indexs:ignore_index=True
# print(res)

# merging data:join,['inner','outer']
# merging data with different columns flag(index names)
# df1 = pd.DataFrame(np.zeros((3,4)),columns=['b','c','d','e'],index=[1,2,3])

# df2 = pd.DataFrame(np.ones((3,4)),columns=['b','c','d','e',],index=[2,3,4])
# print(df1)
# print(df2)
# res = pd.concat([df1,df2],join='inner',ignore_index=True)#merging cross sets 上下合并
# res2 = pd.concat([df1,df2],axis=1,join_axes=[df1.index])#merging cross sets 左右合并
# print(res)
# print(res2)

# append 默认上下add 数据
# df1 = pd.DataFrame(np.zeros((3,4)),columns=['a','b','c','d'],index=[1,2,3])
# df2 = pd.DataFrame(np.zeros((3,4)),columns=['a','b','c','d'],index=[1,2,3])
# df3 = pd.DataFrame(np.zeros((3,4)),columns=['a','b','c','d'],index=[1,2,3])
# # res = df1.append(df2,ignore_index=True)
# res = df1.append([df2,df3],ignore_index=True)
# print(res)

# df1 = pd.DataFrame(np.zeros((3,4)),columns=['a','b','c','d'],index=[1,2,3])
# s1 =pd.Series([1,2,3,4],index=['a','b','c','d'])
# res = df1.append(s1,ignore_index=True)
# print(res)

# merge two df by key/keys,used on database
# left = pd.DataFrame({'key':['k1','k2','k3','k4'],'A':['A0','A2','A3','A4'],'B':['B1','B2','B3','B4']})
# right = pd.DataFrame({'key':['k1','k2','k3','k4'],'A':['A0','A2','A3','A4'],'B':['B1','B2','B3','B4']})
#
# print(left)
# print(right)
# res = pd.merge(left,right,on='key')#on which columns
# print(res)

# merge two df by key/keys,used on database
#consider two columns
# left = pd.DataFrame({'key1':['k0','k0','k0','k2'],'key2':['k0','k1','k0','k1'],
#                      'A':['A0','A2','A3','A4'],'B':['B1','B2','B3','B4']})
# right = pd.DataFrame({'key1':['k0','k1','k1','k2'],'key2':['k0','k0','k0','k0'],
#                       'A':['A0','A2','A3','A4'],'B':['B1','B2','B3','B4']})
# res = pd.merge(left,right,on=['key1','key2'],how='outer',indicator=True)

#default merge by inner,how='inner','outer','left','right',indicator,考虑合并关注属性，
# 如何合并，indicator=True显示合并结果如何，是否两者都有，后者仅是是一方

# merge by index
# left = pd.DataFrame({'A': ['A0', 'A1', 'A2'],
#                                   'B': ['B0', 'B1', 'B2']},
#                                   index=['K0', 'K1', 'K2'])
# right = pd.DataFrame({'C': ['C0', 'C2', 'C3'],
#                                      'D': ['D0', 'D2', 'D3']},
# index=['K0', 'K2', 'K3'])
# res = pd.merge(left,right,left_index=True,right_index=True,how='outer',indicator=True)
# print(left)
# print(right)
# print(res)

# handle overlapping处理重复的信息
boys = pd.DataFrame({'k': ['K0', 'K1', 'K2'], 'age': [1, 2, 3]})
girls = pd.DataFrame({'k': ['K0', 'K0', 'K3'], 'age': [4, 5, 6]})
res = pd.merge(boys, girls, on='k', suffixes=['_boy', '_girl'], how='inner')#suffixes
print(res)

