arr=[0]*100_001
arr[0], arr[1] = 0, 1

def solution(n):
    for i in range(2, 100_001):
        arr[i] = arr[i-1] + arr[i-2]
    answer = 0
    answer = arr[n]%1234567
    return answer