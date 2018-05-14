# -*- coding:utf-8 -*-
import csv
import numpy as np
import math
import pylab as pl
with open('iris1.csv')as csvfile:
    reader=csv.reader(csvfile, delimiter=',')
    # dates0-9是普通的list
    dates1 = [];dates2 = [];dates3 = [];dates4 = [];dates5=[];dates6=[];dates7=[]
    for row in reader:
        # 第一次实习第一部分等使用
        date1 = float(row[0]);date2 = float(row[1]);date3 = float(row[2]);date4 = float(row[3]);date5=row[4]
        dates1.append(date1);dates2.append(date2);dates3.append(date3);dates4.append(date4);dates5.append(date5)
        #其中0--- 'Iris-versicolor'；1----'Iris-setosa' ；2----Iris-virginica
        if(date5=='Iris-versicolor'):
            date7=0
        elif(date5=='Iris-setosa'):
            date7=1
        else:
            date7=2
        dates6.append(date1);dates6.append(date2);dates6.append(date3);dates6.append(date4);dates6.append(date7)
        dates7.append(dates6)
        dates6=[]
        date7=0

datess1=np.array(dates1);datess2=np.array(dates2);datess3=np.array(dates3);datess4=np.array(dates4);datess5=np.array(dates5)
#print(datess1);print(datess2);print(datess3);print(datess4);print(dates5)
print(dates7)
print(len(dates7))
#a,b,c三个数组是存储对应'Iris-versicolor'、'Iris-setosa'、 'Iris-virginica'的序号
a=[];b=[];c=[]
m=0
for i in dates5:#dates5数组是存储鸢尾花数据其类别的数组
    if i=='Iris-versicolor':
        a.append(m)
    elif i=='Iris-setosa':
        b.append(m)
    else:
        c.append(m)
    m=m+1
print(a);print(b);print(c)
print(len(a));print(len(b));print(len(c))

#x为对应的属性的数组，y为其在D中的编号，D为所有数据的数组
def numeric(x,y,D):
    #给属性的数组进行排序
    x.sort()
    n1=0;n2=0;n3=0
    a=x.sum()/len(x)
    print("中点的值是：")
    print(a)
    for i in D:
        if(i[0]<=a and i[4]=='Iris-versicolor'):
            n1=n1+1
        elif(i[0]<=a and i[4]=='Iris-setosa'):
            n2=n2+1
        elif(i[0]<=a and i[4]=='Iris-virginica'):
            n3=n3+1


#D为数据集合，a为叶子大小，b为叶子纯度阙值
def DecisionTree(D,a,b):
    n=len(D);n1=0;n2=0;n3=0
    for i in D:
        if(i[4]==0):
            n1=n1+1
        elif(i[4]==1):
            n2=n2+1
        else:
            n3=n3+1
    if(n<=a or n1>=b ):
        maxlabel='Iris-versicolor'
    elif(n<=a or n2>=b):
        maxlabel='Iris-setosa'
    else:
        maxlabel='Iris-virginica'

    numeric(datess1, 0, D)
    numeric(datess2, 1, D)
    numeric(datess3, 2, D)
    numeric(datess4, 3, D)

DecisionTree(dates7,5,0.95)
print("因后续部分没有时间完成，未完待续")