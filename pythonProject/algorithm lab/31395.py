import sys
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
n = int(input())
A = list(map(int,input().split()))

target = []
cnt = 1
for i in range(n-1):
    if A[i] < A[i+1]:
        cnt += 1
    else:
        target.append(cnt)
        cnt = 1

def factorial(n):
    if n == 1:
        return 1
    else:
        return n + factorial(n - 1)

target.append(cnt)
answer = 0
for i in target:
    answer += factorial(i)
print(answer)



from collections import deque
import sys
input = sys.stdin.readline
# 나이트의 이동 방향
moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]

def knight_min_moves(board_size, start, end):
    # 시작 위치와 끝 위치가 같으면 이동 필요 없음
    if start == end:
        return 0

    # 방문 여부와 큐 초기화
    visited = [[False] * board_size for _ in range(board_size)]
    queue = deque([(start[0], start[1], 0)])  # (x, y, 이동 횟수)
    visited[start[0]][start[1]] = True

    # BFS 탐색
    while queue:
        x, y, moves_count = queue.popleft()

        # 목표 위치에 도달하면 이동 횟수 반환
        if (x, y) == end:
            return moves_count

        # 나이트의 이동 가능한 모든 방향 탐색
        for dx, dy in moves:
            nx, ny = x + dx, y + dy
            # 체스판 범위 내에 있고 방문하지 않은 경우
            if 0 <= nx < board_size and 0 <= ny < board_size and not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, moves_count + 1))

    # 이동 불가능한 경우 -1 반환 (일반 체스판에서는 모든 위치에 도달 가능)
    return -1


# 예시 입력
board_size = 100  # 체스판 8x8
start = (0, 0)  # 시작 위치
end = (30, 50)  # 목표 위치

T = int(input())
for _ in range(T):
    board_size = int(input())
    start = tuple(map(int,input().split()))
    end = tuple(map(int,input().split()))
    print(knight_min_moves(board_size, start, end))  # 출력: 최단 이동 횟수
