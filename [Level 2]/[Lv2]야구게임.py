def make_candidates():
    import itertools
    pool=['1','2','3','4','5','6','7','8','9']
    return list(map(''.join,itertools.permutations(pool,3)))


def check_correct(input_case,candidate):
    (strike,ball)=0,0
    
    for i in range(0,3):
        if input_case[i]==candidate[i]:
            strike+=1
        elif input_case[i] in candidate:
            ball+=1
    
    return (strike,ball)
    
    

def solution(baseball):
    candidates=make_candidates()
    
    '''for(input_case,strike,ball) in baseball:
        for candidate in candidates:
            if(check_correct(str(input_case),str(candidate))!=(strike,ball)):
                candidates.remove(candidate)'''
    for(input_case,strike,ball) in baseball:
        
            
    
    print(candidates)
    return len(candidates)

print(solution([[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]))
