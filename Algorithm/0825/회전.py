import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())

    q= list(map(int, input().split()))

    for i in range(M):
        q.append(q.pop(0))

    print(f'#{t} {q[0]}')