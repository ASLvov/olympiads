n = int(input())
t = input().split()
res = []
for i in range(n-1):
	for j in range(i+1,n):
		if abs(int(t[i])-int(t[j]))<=5:
			res.append(j-i-1)
if res:
	print(min(res))
else:
	print(-1)