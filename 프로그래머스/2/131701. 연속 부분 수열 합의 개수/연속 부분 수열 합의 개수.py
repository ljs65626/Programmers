def solution(elements):
    leng = len(elements)
    elements = elements * 2
    # print(elements)
    answer = []
    for i in range(1, leng+1):
        for j in range(leng):
            answer.append(sum(elements[j:j+i]))
    # print(list(set(answer)))
    ans = len(list(set(answer)))
    return ans