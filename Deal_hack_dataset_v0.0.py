import pandas as pd
import numpy as np
import os
import multiprocessing as mp


# def writetofile(content, attr2):
#     with open(attr2,'a',encoding='utf-8') as f:
#         f.write(content + '\n')
#         # f.writable()
#         # f.writelines(json.dumps(content,ensure_ascii=False)+'\n')


def job(url):
    url1 = url[0]
    url2 = url[1]
    # print(url1)
    # print(url2)
    # return 0
    # print(url2.index('/',53))
    # print(url2[55:-4])
    data = pd.read_csv(url1, sep='\s+',delimiter=',', header=None,
                       engine='python', chunksize=10000,dtype=np.str)
    count = 0
    s1_fir_element = 0
    for o1 in data:
        count += 1
        if count%10==0:
            print(url2[55:-9]+' loop:{}'.format(count))
        # for l in o1.loc[:5,:].iterrows():#行迭代器
            # print(l[1])
        # print(o1.loc[:5,:].notna())#查看非空，空元素
        # o1.loc[:5,:].replace('None',np.nan)

        """take the difference between after and before on columns 0 or time"""
        arr = np.insert(o1.loc[:,0].values,0,s1_fir_element,axis=0).astype(np.float64)
        arr1 = arr[1:]-arr[:-1]# calculate the time difference between before and after
        s1_fir_element = arr[-1]
        # np.set_printoptions(precision=4)
        o1.iloc[:,0] = arr1
        if count == 1:
            o1.iloc[0,0]= 0


        """merge columns 4 to 10"""
        l = o1.iloc[:, 3:].values
        dlc =  o1.iloc[:, 2].values
        # print(dlc)
        x = [5,6,7,8,9,10,11]
        o1.drop(o1.columns[x],axis=1,inplace=True)
        # print("o1.loc[9980,:]:",o1.iloc[9980,:])
        # print("l[9980,:]:",l[9980])
        # print("dlc[9980]:",dlc[9980])
        # is_copy()

        contents = []
        flags = []
        for i in zip(l,dlc):
            # print(i[0][int(i[1])])
            flags.append(i[0][int(i[1])])
            content = ''
            for _ in range(int(i[1])):
                # print(i[0][_])
                content += i[0][_]
            contents.append(content)

        # print(flags)
        # print(contents)
        o1.iloc[:,3] = contents
        o1.iloc[:,4] = flags
        o1.to_csv(url2,sep=' ', index=False,header=False,mode='a')
        # print("o1:\n",o1)
        # # np.set_printoptions(precision=4)
        # print("o1.loc[9980,:]\n",o1.loc[9980,:])
        # print(o1.loc[:,4])
        # print(o1)
        # exit()


def test(urls):
    print(urls)
    for url in urls:

        url1 = url[0]
        url2 = url[1]
        # print(url1,'\n',url2)
        # continue
        data1 = pd.read_csv(url1, sep='\s+', delimiter=',', header=None,
                           engine='python', chunksize=10000, dtype=np.str)
        data2 = pd.read_csv(url2, sep='\s+', delimiter=',', header=None,
                           engine='python', chunksize=10000, dtype=np.str)
        """shared memory"""
        ran_array = np.random.randint(1, 10000, [1,1]).flatten('C').tolist()
        # print(ran_array)
        # exit()
        array = mp.Array('i', ran_array)
        count_t = 0
        for _ in ran_array:
            print(url1[url1.index("t/")+2:url1.index(".")] + 'ranloop:{}loop'.format(count_t,count))
            count_t+=1

            count = 0
            for o1 in zip(data1,data2):
                count+=1
                if count%70==0:
                    print("row data:{}\nDeal data:{}".format(o1[0].iloc[_,:],o1[1].iloc[_,:]))

    return 0


if __name__ == "__main__":
    np.set_printoptions(suppress=True,precision=4)
    source_attr =r"/home/gjj/PycharmProjects/ADA/data/car-hacking-instrusion dataset/"
    dire_attr = r"/home/gjj/PycharmProjects/ADA/dealed_data/hacking_data/"
    attrs = os.listdir(source_attr)

    pool = mp.Pool(processes=4)#rocess"""


    r_url = []
    w_url = []
    # print(attrs)
    for attr in attrs:
        r_url.append(source_attr + attr)
        w_url.append(dire_attr + attr[:attr.index('.')] + "_Deal.txt")
    # print(r_url[1][r_url[1].index("t/")+2:r_url[1].index(".")])

    """test"""
    # test(zip(r_url,w_url))

    """multiprocess :pool map or apply_async()"""
    pool.map(job, zip(r_url,w_url),)
    pool.close()
    pool.join()

    """test the result by random select"""


    # r = source_attr +"DoS_dataset.csv"
    # w = dire_attr + "DoS_dataset_DT.txt"
    # for attr in attrs:
    #     print(attr)
    #     r_url = source_attr + attr
    #     w_url = dire_attr + attr[:attr.index('.')] + "_Deal.txt"
    #     p1 = pool.apply_async(job, (r_url,w_url,))
    # job(r,w)