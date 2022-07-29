import sys

sys.stdin = open("_신용카드만들기2.txt")

T = int(input())
for test_case in range(1, T+1):
    card_num = list(input())
    allow = ['3', '4', '5', '6', '9']
    ans = 0
    if card_num[0] in allow and (len(card_num) == 16 or len(card_num) == 19):
        ans = 1
    print(f'#{test_case} {ans}')