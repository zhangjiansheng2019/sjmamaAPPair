# -*- encoding=utf8 -*-
__author__ = "Administrator"

from airtest.core.api import *

auto_setup(__file__)

import time
import os
import random

def sleep(s):#睡觉时间
    time.sleep(s)

def de(file):#是否存在一个文件，删除它
    if (os.path.exists(file)):
        os.remove(file)

def nowadaytime():  #当前时间
   return (time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))
nowadaytime()

def tim():#时间戳
    return  time.time()

def catalog(cataname):  #创建一个文件夹
    if(os.path.exists(cataname)==False):
        os.makedirs(cataname)
catalog('logs')

def writelog(file,txt):
    logfile=file+'-'+str(tim())+'.txt'
    l=open('logs//'+logfile,'a+',encoding='utf-8') #创建一个文件，放在之前的logs里面
    l.write(str(tim())+'\t'+txt+'\n')#写入文本
    print(str(tim())+'\t'+txt)
writelog('手机麻麻','明天去吃饭')

def randomno(num):
    numbers='123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+=-'
    container=[]
    for i in range(num):
        container.append(random.choice(numbers))#choice是从中选择一个随机数，append将每个随机数放进列表里。
    names=''.join(container)#通过‘’里的连接符，将列表或括号里的词连接起来。
    print (names)
randomno(5)

def randomno2(type,num):
    numbers=''#变量=以下几种情况
    if(type==1):
        numbers='1234567890'
    elif(type==2):
        numbers='1234567890abcdefghijklmnopqrstuvwxyz'
    elif(type==3):
        numbers='1234567890abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWSYZ'
    container=[]#定义一个空列表
    for i in range(num):
        container.append(random.choice(numbers))#choice是从中选择一个随机数，append将每个随机数放进列表里。
        names=''.join(container)#通过‘’里的连接符，将列表或括号里的词连接起来。
        return (names) #如果该方法要被调用，就要返回值
#randomno2(3,3)


def randomno3(type,num,count):
    container=[]
    for i in range(count):
        container.append(randomno2(type,num))#调用方法2，将方法2的result连接起来
        return (container)#返回值，因为传参进去后，randomno2要得到参数
        print (container)
randomno3(3,3,2)

def del_file(path):
    ls = os.listdir(path)#该路径的所有文件夹和文件名
    for i in ls:
        c_path = os.path.join(path, i)#把目录和遍历到的文件合成一条路径
        if os.path.isdir(c_path):#判断否为目录
            print (c_path)  #是目录显示
        else:
            os.remove(c_path)#是文件删除


a =100
if (a <=100 and a >=60):
    print ('good')
else :
    print ('out')