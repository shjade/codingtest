def solution(k, dungeons):
    visited = [False] * len(dungeons)
    answer = 0

    def dfs(current_k, count):
        nonlocal answer
        answer = max(answer, count)

        for i in range(len(dungeons)):
            if not visited[i]:
                need, cost = dungeons[i]
                if current_k >= need:
                    visited[i] = True
                    dfs(current_k - cost, count + 1)
                    visited[i] = False

    dfs(k, 0)
    return answer
