import sys

sys.stdin = open("_최빈수구하기.txt")

T = int(input())
for testcase in range(1, T+1):
    t = int(input())
    student = list(map(int, input().split()))    # 인덱스가 학생수, 값이 점수
    ans = [0] * 101    # 인덱스가 점수, 값이 그 점수를 맞은 학생 수
    for i in range(1000):
        ans[student[i]] += 1
    max_student = 0
    max_grade = 0
    for answer in range(1, 101):
        if max_student <= ans[answer]:
            max_student = ans[answer]
            max_grade = answer
    print(f'#{t} {max_grade}')