
def solution(clothes):
    length=len(clothes)
    
    for i in range (0,length):
        for j in range (0,length):
            if i!=j and len(clothes[i])<=len(clothes[j]):
                if clothes[i]==clothes[j][:len(clothes[i])]:
                    return False
                    
    return True

