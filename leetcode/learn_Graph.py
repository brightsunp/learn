#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/20'

- topological sort: https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
- strong connected: https://www.geeksforgeeks.org/connectivity-in-a-directed-graph/
'''
from collections import defaultdict


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
        visited = [False for _ in range(self.V)]
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
        visited = [False for _ in range(self.V)]
        res = []
        self._dfs_util(s, visited, res)
        return res

    def dfs2(self):
        # for Complete Traversal
        visited = [False for _ in range(self.V)]
        res = []
        for i in range(self.V):
            if not visited[i]:
                self._dfs_util(i, visited, res)
        return res

    def topological_sort(self):
        indegrees = [0 for _ in range(self.V)]
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
        visited = [False for _ in range(self.V)]
        self._dfs_util(0, visited, [])
        if any(not i for i in visited):
            return False
        gr = self._get_reverse()
        visited = [False for _ in range(self.V)]
        gr._dfs_util(0, visited, [])
        if any(not i for i in visited):
            return False
        return True

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
