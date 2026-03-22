## Python language
## solution link(含註解): https://github.com/CBJ0519/CBJsProgramDiary.com/blob/main/zj/a010.py
 
n=int(input())
tmp=[]
for i in range(2,int(1e9)):
    if n==1: break
    cnt=0
    while not n%i:
        cnt+=1
        n//=i
    if cnt: tmp.append([i,cnt])
ans=[]
for i,cnt in tmp:
    if cnt>1: ans.append(f'{i}^{cnt}')
    else: ans.append(i)
print(*ans,sep=' * ')
