import sys

sys.stdin = open("_직사각형길이찾기.txt")

T = int(input())
for test_case in range(1, T+1):
    rect_ = list(map(int, input().split()))
    ans = 0
    if rect_[0] == rect_[1] and rect_[1] == rect_[2] and rect_[2] == rect_[0]:
        ans = rect_[0]
    elif rect_[0] == rect_[1]:
        ans = rect_[2]
    elif rect_[1] == rect_[2]:
        ans = rect_[0]
    elif rect_[2] == rect_[0]:
        ans = rect_[1]
        
    print(f'#{test_case} {ans}')