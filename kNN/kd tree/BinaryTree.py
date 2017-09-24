# -*- coding: utf-8 -*-
'''
NOTE: This Code is borrowed from: http://blog.csdn.net/v_victor/article/details/51131283 
Created on 2017年9月24日
@author: XY
'''
class BinaryTree(object):  
    '''
    创建结点 
    '''  
    class __node(object):  
        def __init__(self, value, k,left=None, right=None):  
            self.value = value  
            self.left = left  
            self.right = right  
            self.s = k  
  
        def getValue(self):  
            return self.value  
  
        def setValue(self, value):  
            self.value = value  
  
        def getLeft(self):  
            return self.left  
  
        def getRight(self):  
            return self.right  
  
        def setLeft(self, newLeft):  
            self.left = newLeft  
  
        def setRight(self, newRight):  
            self.right = newRight  
  
        def getS(self):  
            return self.s  
  
        def __iter__(self):  
            if self.left != None:  
                for elem in self.left:  
                    yield elem  
  
            yield self.value  
  
            if self.right != None:  
                for elem in self.right:  
                    yield elem  
    '''
    创建根 
    '''  
    def __init__(self, length):
        self.length = length
        self.root = None
        
    def insert(self, value):
        k = 0
        length = self.length
        def __insert(k, root, value):
            index = k % length   # length是特征空间维数，k是树的深度
            k += 1
            if root == None:
                return BinaryTree.__node(value, index)
            if value[index] < root.getValue()[index]:
                root.setLeft(__insert(k, root.getLeft(), value))
            else:
                root.setRight(__insert(k, root.getRight(), value))
            return root
        self.root = __insert(k, self.root, value)
        
    def __iter__(self):
        if self.root != None:
            return self.root.__iter__()
        else:
            return [].__iter__()
        
def main():
    pass
if __name__=='__main__':
    main()
        