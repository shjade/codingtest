def solution(numbers, target):
    
    answer = 0
    
    # dfs 함수
    def dfs(index, total):
        nonlocal answer
        
        # 종료조건
        if index == len(numbers):
            if target == total:
                answer += 1
            return
        
        # +, -
        dfs(index+1,total+numbers[index])
        dfs(index+1,total-numbers[index])
    
    # 함수 시작
    dfs(0,0)
    
    return answer