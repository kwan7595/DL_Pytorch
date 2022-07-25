import sys
from collections import defaultdict
from collections import deque
n,s,p = map(int,input().split())
adj = defaultdict(deque)
visit = [0]*(n+1)
for i in range(n-1):
    a,b = map(int,sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)
queue = deque()
queue.append(p)
level=0
ans=[]
while len(queue)!=0:
    depth = len(queue)
    while(depth !=0):
        depth-=1
        temp=queue.popleft()
        if temp<=s:
            ans.append((temp,level))
            continue
        if len(ans)==2:
            queue.clear()
            break
        for node in adj[temp]:
            if visit[node] is not True:
                visit[node]=True
                queue.append(node)
    level+=1
answer = n - (ans[0][1]+ans[1][1]+1)
print(answer)