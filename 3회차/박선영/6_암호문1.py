import sys

sys.stdin = open("_암호문1.txt")

# 1개짜리 insert 해보기
# # 원본 암호문의 길이
# N = 11
# # 원본 암호문
# amho = [449047, 855428, 425117, 532416, 358612, 929816, 313459, 311433, 472478, 589139, 568205]
# # 명령어의 개수
# S = 7
# # 명령어
# command_ = ['I', '1', '5', '400905', '139831', '966064', '336948', '119288']
# x, y= int(command_[1]), int(command_[2])
# tmp = 0

# # y개를 insert함
# for i in range(y):
#     amho.insert(x + tmp, int(command_[3 + tmp]))
#     tmp += 1

# # 10개만 출력함
# for i in range(10):
#     print(amho[i], end=' ')

# ========================================================================================================
# 여러 개 받아서 insert 해보기

for test_case in range(1, 11):
    # 원본 암호문의 길이
    N = int(input())
    # 원본 암호문
    amho = list(map(int, input().split()))
    # 명령어의 개수
    S = int(input())
    # 명령어
    command_ = list(input().split())
    length = 0
    
    # 명령어의 개수만큼 반복함
    for i in range(S):
        x = int(command_[length+1])
        y = int(command_[length+2])
        tmp = 0
        # y개를 insert함
        for j in range(y):
            amho.insert(x + tmp, int(command_[3 + tmp + length]))
            tmp += 1
        length = length + y + 3
    print(f'#{test_case}', end = ' ')
    for i in range(10):
        print(amho[i], end=' ')
    print()