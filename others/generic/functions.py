#!/usr/bin/env python
# -*- encoding: utf-8 -*-

'''
@Time    :   2023/11/13 23:40:22
@Author  :   Xing ZiShuai 
@Version :   1.0
@Contact :   xwatson@163.com
@Description    :
1、冒泡排序
2、计算x的n次方
3、计算a*a+b*b+c*c+....
4、计算阶乘n!
5、列出当前目录下所有文件和目录名
6、把一个list中所有的字符串变成小写
7、输出某个路径下的所有文件和文件路径
8、输出某个路径及其子目录下的所有文件路径
9、输出某个路径及其子目录下所有以.html为后缀的文件
10、把原字典的键值对颠倒并生成新的字典
11、打印九九乘法表
12、替换列表中所有的3为3a
13、打印list每个名字
14、合并去重
15、随机生成验证码的两种方式
16、计算平方根
17、判断字符串是否只由数字组成
18、判断奇偶数
19、判断闰年
20、获取最大值
21、斐波那契数列
22、十进制转二进制、八进制、十六进制
23、最大公约数
24、最小公倍数
25、简单计算器
26、生成日历
27、文件IO
28、字符串判断
29、字符串大小写转换
30、计算每个月的天数
31、获取昨天的日期
'''

def sort_port_01():
    '''
    1、比较相邻的元素。如果第一个比第二个大,就交换它们两个；
    2、每一对相邻元素作同样的工作,从开始第一对到结尾的最后一对，这样在最后的元素应该会是最大的数；
    3、针对所有的元素重复以上的步骤,除了最后一个；
    4、重复步骤1~3,直到排序完成。
    更多排序算法动图： https://www.cnblogs.com/onepixel/articles/7674659.html
    '''
    lis = [56,12,1,18,234,10,190,100,34,56,78,456,-20]
    for i in range(len(lis)-1):
        for j in range(len(lis)-1-i):
            if lis[j] > lis[j+1]:
                lis[j],lis[j+1] = lis[j+1],lis[j]
    return lis


def power_02(x,n):
    s = 1
    while n>0:
        n = n-1
        s = s * x
    return s

def calc_03(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

def factorial_04(n):
    result = n
    for i in range(1,n):
        result *= i
    return result

def get_dir_05():
    import os
    return [d for d in os.listdir('.')]

def get_lower_06():
    L = ['Hello','World','IBM','Apple']
    return [s.lower() for s in L]

def print_dir_07():
    import os
    filepath = input("请输入一个路径: ")
    if filepath == "":
        print("请输入正确的路径")
    else:
        for i in os.listdir(filepath):
            print(os.path.join(filepath,i))

def show_dir_08(filepath):
    import os
    for i in os.listdir(filepath):
        path = (os.path.join(filepath,i))
        print(path)
        if os.path.isdir(path):
            show_dir(path)

def print_file_09(filepath):
    import os
    for i in os.listdir(filepath):
        path = os.path.join(filepath,i)
        if os.path.isdir(path):
            print_file_09(path)
        if path.endswith(".html"):
            print(path)

def change_key_value_10():
    dict1={"A":"a","B":"b","C":"c"}
    print({y:x for x,y in dict1.items()})


def nine_take_nine_11():
    for i in range(1,10):
        for j in range(1,i+1):
            print('{}*{}={}\t'.format(j,i,i*j),end='')


if __name__ == "__main__":
    print(sort_port_01())

