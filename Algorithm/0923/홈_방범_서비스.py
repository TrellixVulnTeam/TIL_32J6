import sys
sys.stdin = open('input.txt','r')

T = int(input())

for t in range(1,T+1):
    N, M = map(int, input().split())

    arr = [list(map(int, input().split())) for _ in range(N)]

    max_profit = 0
    max_count = 0



    for i in range(N):
        for j in range(N):
            location = arr[i][j]
            K = 1

            for k in range(N):
                if location == 1:
                    cnt = 1
                else:
                    cnt = 0

                K += 1
                move = 1
                while move<=K:
                    for di, dj in ((0,1),(0,-1),(1,0),(-1,0)):
                        ni, nj = i+di, j+dj
                        move +=1
                        if 0<=ni<N and 0<=nj<N and arr[ni][nj] == 1:
                            cnt += 1

                income = cnt * M  # 집들을 통해 얻는 수익
                cost = K * K + (K - 1) * (K - 1)  # 운영 비용
                profit = income - cost  # 보안 회사의 이익

                if profit > max_profit:
                    max_profit = profit
                    max_count = cnt

                    print("<<<<<<<<<<<<<여기닷!!!",i,j,cnt)

                print(K, profit)

    print(f'#{t} {max_count}')