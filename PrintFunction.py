#Read an integer N .
#Without using any string methods, try to print the following:
#123...N
#Note that "" represents the values in between.

#Input Format
#The first line contains an integer N .

#Output Format
#Output the answer as explained in the task.

#Sample Input 0
#3

#Sample Output 0
#123

n = int(input())
r=[]
while n>0:
    r.append(n)
    n=n-1
r1=reversed(r)
for i in r1:
    print(i,end='')
