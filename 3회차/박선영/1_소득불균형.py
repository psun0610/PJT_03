import sys

sys.stdin = open("_소득불균형.txt")

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    sodeuk_list = list(map(int, input().split()))
    aver = sum(sodeuk_list) / N
    count = 0
    for sodeuk in sodeuk_list:
        if sodeuk <= aver:
            count += 1
    print(f'#{test_case} {count}')