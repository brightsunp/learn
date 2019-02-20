#!/usr/bin/python
# coding=utf-8
'''
__author__ = 'sunp'
__date__ = '2019/2/20'

- topological sort: https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/
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

    def bfs(self, s):
        visited = [False for _ in range(self.V)]
        queue = [s]
        while queue:
            u = queue.pop(0)
            visited[u] = True
            print(u, end=' ')
            for i in self.graph[u]:
                if not visited[i]:
                    queue.append(i)
                    visited[i] = True

    def dfs1(self, s):
        # only for Connected Graph
        visited = [False for _ in range(self.V)]
        self._dfs_util(s, visited)

    def dfs2(self):
        # for Complete Traversal
        visited = [False for _ in range(self.V)]
        for i in range(self.V):
            if not visited[i]:
                self._dfs_util(i, visited)

    def _dfs_util(self, u, visited):
        visited[u] = True
        print(u, end=' ')
        for i in self.graph[u]:
            if not visited[i]:
                self._dfs_util(i, visited)

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
        else:
            print(order)
