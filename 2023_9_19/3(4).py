from heapq import *


def dijkstra(graph, start):
    vnum = len(graph)  # 顶点个数
    paths = {}
    cands = [(0, start, start)]
    heapify(cands)  # 转化为小顶堆，便于找到权重最小的边
    count = 0
    while count < vnum and cands is not None:
        print(cands)
        plen, u, vmin = heappop(cands)  # 选出累计路径最短的边
        if paths.get(vmin) is not None:  # 如果已经找到到vmin的最短路径就跳过
            continue
        paths[vmin] = plen  # 存入最短路径
        for next_edge in graph[vmin]:
            if not paths.get(next_edge[2]):
                heappush(cands, (plen + next_edge[0], u, next_edge[2]))
        count += 1
    return paths


graph = {'A': [(7, 'A', 'B'), (5, 'A', 'D')],
         'C': [(8, 'C', 'B'), (5, 'C', 'E')],
         'B': [(7, 'B', 'A'), (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E')],
         'E': [(7, 'E', 'B'), (5, 'E', 'C'), (15, 'E', 'D'), (8, 'E', 'F'), (9, 'E', 'G')],
         'D': [(5, 'D', 'A'), (9, 'D', 'B'), (15, 'D', 'E'), (6, 'D', 'F')],
         'G': [(9, 'G', 'E'), (11, 'G', 'F')],
         'F': [(6, 'F', 'D'), (8, 'F', 'E'), (11, 'F', 'G')]}
print(dijkstra(graph, 'A'))
