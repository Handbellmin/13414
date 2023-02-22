import sys
input = sys.stdin.readline
n1,n2 = map(int,input().split(" "))
ls = {}

for i in range(n2):
  str = input().rstrip()
  ls[str] = i

ls = (sorted(ls.items(),key=lambda x:x[1]))
cnt = 0 
for i in ls:
  if cnt < n1:
    print(i[0])
    cnt += 1
  elif cnt > n1:
    break
    