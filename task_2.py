from task_1 import create_graph
from collections import deque


def dfs(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            stack.extend(set(graph[vertex]) - visited)


def bfs(graph, start):
    visited = set()
    queue = deque([start])
    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            print(vertex, end=" ")
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)


def main():
    G = create_graph()

    print("BFS:")
    bfs(G, "Україна")

    print("\n")

    print("DFS:")
    dfs(G, "Україна")


if __name__ == "__main__":
    main()
