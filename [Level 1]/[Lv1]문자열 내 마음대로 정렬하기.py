def solution(strings, n):
    answer = []
    answer=sorted(strings, key=lambda string:(string[n],string) )
    return answer

print(solution(["abce", "abcd", "cdx"],2))