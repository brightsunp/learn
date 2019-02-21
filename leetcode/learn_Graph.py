#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/20'

- topological sort: https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
- strong connectivity: https://www.geeksforgeeks.org/connectivity-in-a-directed-graph/
- cyclic: https://www.geeksforgeeks.org/detect-cycle-direct-graph-using-colors/
- Dijkstra: https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
- Prim: https://www.geeksforgeeks.org/prims-minimum-spanning-tree-mst-greedy-algo-5/
'''
from collections import defaultdict
import sys


class Graph(object):
    '''
    Represented with adjacency lists.
    '''
    def __init__(self, n_vertices):
        self.graph = defaultdict(list)
        self.V = n_vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def count_edges(self, is_directed=False):
        res = 0
        for i in self.graph:
            res += len(self.graph[i])
        return res if is_directed else res >> 1

    def bfs(self, s):
        visited = [False] * self.V
        queue, res = [s], []
        while queue:
            u = queue.pop(0)
            visited[u] = True
            res.append(u)
            for i in self.graph[u]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True
        return res

    def dfs1(self, s):
        # only for Connected Graph
        visited = [False] * self.V
        res = []
        self._dfs_util(s, visited, res)
        return res

    def dfs2(self):
        # for Complete Traversal
        visited = [False] * self.V
        res = []
        for i in range(self.V):
            if not visited[i]:
                self._dfs_util(i, visited, res)
        return res

    def topological_sort(self):
        indegrees = [0] * self.V
        for i in self.graph:
            for j in self.graph[i]:
                indegrees[j] += 1
        queue = []
        for i, indegree in enumerate(indegrees):
            if indegree == 0:
                queue.append(i)
        count, order = 0, []
        while queue:
            u = queue.pop(0)
            order.append(u)
            for i in self.graph[u]:
                indegrees[i] -= 1
                if indegrees[i] == 0:
                    queue.append(i)
            count += 1
        if count != self.V:
            print('There exists a cycle in the graph.')
        return order

    def is_SC(self):
        visited = [False] * self.V
        self._dfs_util(0, visited, [])
        if any(not i for i in visited):
            return False
        gr = self._get_reverse()
        visited = [False] * self.V
        gr._dfs_util(0, visited, [])
        if any(not i for i in visited):
            return False
        return True

    def is_cyclic(self):
        color = ['WHITE'] * self.V
        for i in range(self.V):
            if color[i] == 'WHITE':
                if self._cyclic_util(i, color):
                    return True
        return False

    def _dfs_util(self, u, visited, tmp):
        visited[u] = True
        tmp.append(u)
        for i in self.graph[u]:
            if not visited[i]:
                self._dfs_util(i, visited, tmp)

    def _get_reverse(self):
        g = Graph(self.V)
        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    def _cyclic_util(self, u, color):
        color[u] = 'GRAY'
        for i in self.graph[u]:
            if color[i] == 'GRAY':
                return True
            if color[i] == 'WHITE' and self._cyclic_util(i, color):
                return True
        color[u] = 'BLACK'
        return False


class Graph2(object):
    '''
    Represented with adjacency matrix.
    '''
    def __init__(self, n_vertices):
        self.V = n_vertices
        self.graph = [[0 for _ in range(self.V)] for _ in range(self.V)]

    def dijkstra(self, src):
        # Shortest Path Tree
        spt_set = [False] * self.V
        dist = [sys.maxsize] * self.V
        dist[src] = 0
        for _ in range(self.V):
            u = self._min_util(dist, spt_set)
            spt_set[u] = True
            # update dist[v] related to u
            for v in range(self.V):
                if (not spt_set[v] and self.graph[u][v] > 0 and
                        dist[u]+self.graph[u][v] < dist[v]):
                    dist[v] = dist[u] + self.graph[u][v]
        return dist

    def prim(self):
        # Minimum Spanning Tree(only Undirected Graph)
        mst_set = [False] * self.V
        key = [sys.maxsize] * self.V
        # array to store constructed MST
        parent = [None] * self.V
        key[0] = 0
        # first node always the root
        parent[0] = -1
        for _ in range(self.V):
            u = self._min_util(key, mst_set)
            mst_set[u] = True
            # update key[v] related to u
            for v in range(self.V):
                if not mst_set[v] and 0 < self.graph[u][v] < key[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u
        for v, u in enumerate(parent[1:], 1):
            print('Edge {}-{}:'.format(u, v), 'Weight {}'.format(self.graph[u][v]))

    def _min_util(self, vals, spt_set):
        min_val, min_idx = sys.maxsize, -1
        for v in range(self.V):
            if not spt_set[v] and vals[v] < min_val:
                min_val, min_idx = vals[v], v
        return min_idx


if __name__ == '__main__':
    test = Graph(6)
    test.add_edge(5, 2)
    test.add_edge(5, 0)
    test.add_edge(4, 0)
    test.add_edge(4, 1)
    test.add_edge(2, 3)
    test.add_edge(3, 1)

    assert test.count_edges(is_directed=True) == 6
    assert test.topological_sort() == [4, 5, 2, 0, 3, 1]
    assert not test.is_SC()
    assert not test.is_cyclic()
    test.add_edge(0, 5)
    assert test.is_cyclic()

    test2 = Graph2(9)
    test2.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
                   [4, 0, 8, 0, 0, 0, 0, 11, 0],
                   [0, 8, 0, 7, 0, 4, 0, 0, 2],
                   [0, 0, 7, 0, 9, 14, 0, 0, 0],
                   [0, 0, 0, 9, 0, 10, 0, 0, 0],
                   [0, 0, 4, 14, 10, 0, 2, 0, 0],
                   [0, 0, 0, 0, 0, 2, 0, 1, 6],
                   [8, 11, 0, 0, 0, 0, 1, 0, 7],
                   [0, 0, 2, 0, 0, 0, 6, 7, 0]]

    assert test2.dijkstra(0) == [0, 4, 12, 19, 21, 11, 9, 8, 14]

    test3 = Graph2(5)
    test3.graph = [[0, 2, 0, 6, 0],
                   [2, 0, 3, 8, 5],
                   [0, 3, 0, 0, 7],
                   [6, 8, 0, 0, 9],
                   [0, 5, 7, 9, 0]]
    test3.prim()
