import sys

sys.stdin = open("_신용카드만들기1.txt")

T = int(input())
for test_case in range(1, T+1):
    card_num = list(map(int, input().split()))
    # 1번, 2번 더하기(but 인덱스는 짝수임)
    sum_ = 0
    for i in range(len(card_num)):
        if i % 2 == 0:
            sum_ += card_num[i] * 2
        else:
            sum_ += card_num[i]
    # 3번 sum_과 N을 더해서 10으로 나눠떨어지게 하기 => 10 - sum_의 뒷자리 숫자 = N
    if int(str(sum_)[-1]) != 0:
        N = 10 - int(str(sum_)[-1])
    else:
        N = 0
    print(f'#{test_case} {N}')