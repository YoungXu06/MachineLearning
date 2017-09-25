# -*- coding: utf-8 -*-
'''
NOTE: This Code is borrowed from: http://blog.csdn.net/v_victor/article/details/51131283 
Created on 2017年9月24日
@author: XY
'''
import numpy as np  
import BinaryTree as bt
import copy as cp  
import stack as st  
def sim_distance(item1,item2):  
    diff = (item1-item2)**2  
    sum_diff = np.sum(diff)  
    sqrt = sum_diff**0.5  
    return sqrt  
#递归插入  
def insertRecursively(k,tree,testArray,length,start,stop):  
    if start>=stop:  
        return  
    middleIndex = (start+stop)//2  
    count = k%length  
    tmp = testArray[start:stop,count]  
    #排序  
    sortedId = tmp.argsort()  
    nextArray = cp.deepcopy(testArray)  
    for i,x in enumerate(sortedId):  
        nextArray[i+start] = testArray[x+start]  
    value = (nextArray[middleIndex])  
    tree.insert(value)  
    k +=1  
    insertRecursively(k,tree,nextArray,length,start,middleIndex)  
    insertRecursively(k,tree,nextArray,length,middleIndex+1,stop)  
#创建kd树  
def makeTree(tree,testArray):  
    k = 0  
    length = testArray.shape[1]  
    insertRecursively(k,tree,testArray,length,0,len(testArray))  
#寻找当前最近点  
def findNode(tree,goal,length):  
    root = tree.root  
    k = 0  
    value = root.getValue()  
    #最小距离  
    max_distance = 0.0  
    min_distance = 0.0  
    #通过栈保存搜索路径  
    path = st.Stack()  
    while True:  
        index = k%length  
        value = root.getValue()  
        path.push(root)  
        k +=1  
        if goal[index]<root.getValue()[index]:  
            if root.getLeft()!=None:  
                root = root.getLeft()  
            else:  
                max_distance = sim_distance(goal,value)  
                nearest = value  
                break  
        else:  
            if root.getRight()!=None:  
                root = root.getRight()  
            else:  
                max_distance = sim_distance(goal,value)  
                nearest = value  
                break  
    min_distance = cp.deepcopy(max_distance)  
    path.pop()  
    while not path.isEmpty():  
        print(nearest)  
        back_point = path.pop()  
        index = back_point.getS()  
        value = back_point.getValue()  
        tmp_dis = sim_distance(goal[index],value[index])  
        #判断进入子结点  
        if tmp_dis <= max_distance:  
            kd_point = None  
            if goal[index] < value[index]:  
                kd_point = back_point.getRight()  
                if kd_point != None:  
                    path.push(kd_point)  
            else:  
                kd_point = back_point.getLeft()  
                if kd_point != None:  
                    path.push(kd_point)  
        #判断是否与当前结点，距离更近  
        tmp_dis = sim_distance(goal,value)  
        if min_distance >= tmp_dis:  
            min_distance = tmp_dis  
            nearest = value  
  
    #print(nearest)  
  
def main():  
    testNum = [2,3,5,4,9,6,4,7,8,1,7,2,3,4,7,2,3,5,6,4,5]
    goal = np.array([4,6,7])
    testArray = np.reshape(testNum, (7,3)) 
    tree = bt.BinaryTree(3)
    makeTree(tree,testArray)  
  
    findNode(tree,goal,len(goal))  
  
if __name__ == '__main__':  
    main()  