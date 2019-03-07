import threading as td
import time
from queue import Queue
import numpy as np
import copy

"""join func"""
# def td_job1():
#     print('j1 start \n')
#     #     print("this is an added Thread,number is %s"%td.current_thread())
#     for i in range(10):
#         time.sleep(1)
#     print('j1 finish\n')

# def td_job2():
#     print('j2 start \n')
#     #     print("this is an added Thread,number is %s"%td.current_thread())
#     # for i in range(10):
#     #     time.sleep(1)
#     print('j2 finish\n')
#
# def main():
#     added_thread = td.Thread(target=td_job1,name='j1')
#     thread2 = td.Thread(target=td_job2,name='j2')
#
#     added_thread.start()#run threads
#     thread2.start()
#     thread2.join()#in process seq as the code do
#     added_thread.join()#in process seq as the code do
#     #add to the main thread seq,glabal seq
#     print('all done\n')
# #     print(td.active_count())
# #     print(td.enumerate())
# #     # print(td.current_thread())


"""queue store the thread process result ,thread had not return func"""
# def j1(l,q):
#     for i in range(len(l)):
#         l[i] = l[i]**2
#     q.put(l)#list put into Queue
#     # return l
#
# def multithread():#data
#     q = Queue()#init a Queue
#     threads = []
#     data = np.arange(12).reshape((4,3))
#     for i in range(4):
#         t = td.Thread(target=j1,args=(data[i],q))#args as thread job arg
#         t.start()
#         threads.append(t)
#     for thread in threads:#join main thread
#         thread.join()
#     results = []
#     for _ in range(4):
#         results.append(q.get())#append Queue element to list
#
#     print(results)

"""GIL LOCK MULTITHREADS"""
# def job(l, q):
#     res = sum(l)
#     q.put(res)
#
# def multithreading(l):
#     q = Queue()
#     threads = []
#     for i in range(4):
#         t = td.Thread(target=job, args=(copy.copy(l), q), name='T%i' % i)
#         # thin copy,original object changed,the copy change as the same as the original
#         # what tin copy do as the placeholder,just like a container
#         # deepcopy,original object changed,the copy not changed by the original
#         t.start()
#         threads.append(t)
#     [t.join() for t in threads]
#     total = 0
#     for _ in range(4):
#         total += q.get()
#     print("multithread:",total)
#
# def normal(l):
#     total = sum(l)
#     print('normalprocess:',total)

"""LOCK"""
def job1():
    global A, lock
    lock.acquire()#lock current thread,lock seq
    for i in range(10):
        A += 1
        print('job1', A)
    lock.release()#release the lock

def job2():
    global A, lock
    lock.acquire()#lock current thread
    for i in range(10):
        A += 10
        print('job2', A)
    lock.release()#release the lock

if __name__ == "__main__":
    # main()
    # multithread()

    """GIL"""
    # l = list(range(1000000))
    # s_t = time.time()
    # normal(l * 4)
    # # normal(l * 4)
    # print('normal_Time: ', time.time() - s_t)
    # s_t = time.time()
    # multithreading(l)
    # print('multithreadTime: ', time.time() - s_t)
    """Lock"""
    lock = td.Lock()
    A = 0
    t1 = td.Thread(target=job1)
    t2 = td.Thread(target=job2)
    t1.start()
    t2.start()
    t1.join()
    t2.join()