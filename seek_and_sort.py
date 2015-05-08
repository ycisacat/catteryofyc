#coding=utf-8
from __future__ import division
#问题：1怎么N行同时加#和去除#号？ 2类名和函数名是不是一定要大写的？貌似不大写没问题？
__metaclass__ =type
class SortAndSeek:
    def bisearch(sequence,number,lower=0,upper=None): #二分法查找
        list.sort()
        if upper is None: upper = len(list)-1
        if lower == upper:
            assert number == list[upper]
            return 'bisearch:the location of %s is' %a,upper
        else:
            middle =(lower + upper)//2 #亲测单独def不会有问题,进类会cannot concatenate 'str' and 'int' objects
            if number > list[middle]:
                return bisearch(list,number,middle+1,upper)
            else:
                return bisearch(list,number,lower,middle)


    def seqsearch(self,list):   #顺序查找
        for i in range(0,len(list),1):
            if a==list[i]:
                print 'location of %s is' %a,list.index(a)+1
            else:
                if i==len(list):
                    print "I've told you not to find something not in the list"
                else:
                    i+=1
        return ""

    def bsort(self,list): #冒泡排序
        length = len(list)
        for i in range(length -1,0,-1):
            for j in range(i):
                if list[j]>list[j+1]:
                    list[j],list[j+1]=list[j+1],list[j]
        return 'bsorted list is',list

    def insort1(self,list): #插入排序
        for i in range(len(list)-1):
            min=list[i]
            if list[i]<=list[i+1]:
                i+=1
            else:
                list[i],list[i+1]=list[i+1],list[i]
                min=list[i+1]
        return "insort1ed list is",list

    def insort2(self,list):#我总觉得上面那个像选择排序,默默写多一个
        import bisect
        list.sort()
        bisect.insort_left(list,a)
        return 'insort2ed list is',list

    def chsort(self,list): #选择排序
        length= len(list)
        for i in range(length -1,0,-1): #为毛线range(length 0,-1,1)就不行啊?一定要我倒着来我也是醉了
            max=i #选出最大的,逐一和最大的比较
            for j in range(i):
                if list[j]>list[max]:
                    list[j],list[max]=list[max],list[j]
        return "chsorted list is",list

    def mergesort(self,list): #归并排序
        left=[] #用来放前半的
        right=[] #用来放后半的
        result=[] #用来放结果的
        if len(list)<=1:
            print 'mergesorted list is',list
        else:
            m=len(list)//2 #从这里断开
            for i in range(len(list)): #分段中
                if i<m:
                    left.append(list[i])
                else:
                    right.append(list[i])
            left.sort()
            right.sort()
            i,j=0,0 #归并中
            while i<len(left) and j<len(right):
                if left[i]<=right[j]:#哪边小取哪个为结果
                    result.append(left[i])
                    i+=1
                else:
                    result.append(right[j])
                    j+=1
            while i<len(left):#把剩下没比较的放进去
                result.append(left[i])
                i+=1
            while j<len(right):
                result.append(right[j])
                j+=1
        return "mergesorted list is",result

list=[] #输入序列
i=''
while not i.isspace():
    i=raw_input('please input list,end with space')
    list.append(i)
del list[-1]
print 'your list is',list
a=raw_input("what do you want to find?Don't try to find something not in the list")
list0,list1,list2,list3,list4=[],[],[],[],[]
list0[:]=list1[:]=list2[:]=list3[:]=list4[:]=list[:]
me=SortAndSeek()
print me.bisearch(list,a)
print me.seqsearch(list)
print me.chsort(list0)
print me.mergesort(list1)
print me.insort1(list2)
print me.insort2(list3)
print me.bsort(list4)













