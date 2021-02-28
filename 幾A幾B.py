import random
n=int(input('數字數量:'))
arr=[0]*n#題目
arr2=[0]*n#作答
m=n
while m!=0:#檢驗重複
    m=0
    for i in range(n):
        arr[i]=random.randint(0,9)
        for i in range(n):
            for k in range(i+1,n):
                if arr[i]==arr[k]:
                    m=m+1

j=0#A的個數
l=0#B的個數

while j!=n:#判定AB數量
    print('作答:')
    j=0
    l=0
    for i in range(n):
        arr2[i]=int(input())
    for i in range(n):
        for k in range(n):
            if arr2[i]==arr[k] and i==k:
                j=j+1
            elif arr2[i]==arr[k] and i!=k:
                l=l+1
    print(j,'A',l,'B')
print(arr)
input()
    
