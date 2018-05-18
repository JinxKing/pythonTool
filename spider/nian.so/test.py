# from multiprocessing import Pool
from multiprocessing import Process
import time


def function(index1,index2):
    print ('Start process: ', str(index1)+"\t"+str(index2))
    time.sleep(3)
    print ('End process', str(index1)+"\t"+str(index2))

if __name__ == '__main__':
    # pool = Pool(processes=4)
    task=[]
    for i in range(4):
        t=Process(target=function, args=(i,i+10,))
        task.append(t)
        # pool.apply_async(function, (i,))
        # print( result.get())
    print ("Started processes")
    for i in range(4):
        task[i].start()
    # pool.close()
    # pool.join()
    print ("Subprocess done.")



