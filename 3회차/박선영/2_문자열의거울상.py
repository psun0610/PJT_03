import sys

sys.stdin = open("_문자열의거울상.txt")

T = int(input())
for test_case in range(1, T+1):
    # 딕셔너리에 값을 넣자
    mirrored_rule = {'b': 'd',
                'd': 'b',           
                'p': 'q',
                'q': 'p'
    }
    # 문자열을 입력받아서 좌우로 뒤집음
    original = input()[::-1]
    mirrored = ''
    # 반복문으로 상하로 뒤집음
    for i in range(len(original)):
        mirrored += mirrored_rule[original[i]]
    print(f'#{test_case} {mirrored}')