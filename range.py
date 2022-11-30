'''
DAY:WEDNESDAy
DATE:30th NOV 2022
TOPIC:range
AUTHOR:KIRANMAI
'''
r=1,2,3,4
print(r) #(1,2,3,4)
print(*r) #1 2 3 4
# h=10,20,30
# for i in h:
#   print(i) #10 20 30(vertically)
# for i in h: 
#   print(i,end=' ') #10 20 30(horizontally)
# g=int(input('enter the value of g:')) #10
# for i in range(1,g+1):
#   print(i) #1 2 3 4 5 6 7 8 9 10
# for i in range(1,10,2):
#   print(i) #1 3 5 7 9
# for i in range(2,10,2):
#   print(i) #2 4 6 8
# for i in range(10,0,-1):
#   print(i)  #10 9 8 7 6 5 4 3 2 1
# for i in range(10,-1,-1):  
#   print(i) #10 9 8 7 6 5 4 3 2 1 0
l=[1,2.0,'kiranmai']
for i in l[::-1]:
  print(i)  #kiranmai 2.0 1
k='kiranmai'
for i in k[::2]:
  print(k)  