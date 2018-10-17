# http://www.stokastik.in/using-kd-tree-for-nearest-neighbor-search/
    
import numpy as np
import time, math, heapq
from collections import deque
"""
Class for defining all variables that goes into the queue while
constructing the KD Tree
"""
class QueueObj(object):
    def __init__(self, indices, depth, node, left, right):
        self.indices, self.depth, self.node = indices, depth, node
        self.left, self.right = left, right
"""
Class for defining the node properties for the KD Tree
"""
class Node(object):
    def __init__(self, vector, split_value, split_row_index):
        self.vector, self.split_value, self.split_row_index = vector, split_value, split_row_index
        self.left, self.right = None, None
"""
KD Tree class starts here
"""
class KDTree(object):
    def __init__(self, vectors):
        self.vectors = vectors
        self.root = None
        self.vector_dim = vectors.shape[1]
    def construct(self):
        n = self.vectors.shape[0]
        queue = deque([QueueObj(range(n), 0, None, 0, 0)])
        while len(queue) > 0:
            qob = queue.popleft()
            q_front, depth, parent, l, r = qob.indices, qob.depth, qob.node, qob.left, qob.right
            axis = depth % self.vector_dim
            vectors = np.argsort(self.vectors[q_front, :][:, axis])
            vectors = [q_front[vec] for vec in vectors]
            m = len(vectors)
            median_index = int(m / 2)
            split_value = self.vectors[vectors[median_index]][axis]
            left, right = median_index + 1, m - 1
            while left <= right:
                mid = int((left + right) / 2)
                if self.vectors[vectors[mid]][axis] > split_value:
                    right = mid - 1
                else:
                    left = mid + 1
            median_index = left - 1
            node = Node(self.vectors[vectors[median_index]], split_value, vectors[median_index])
            if parent is None:
                self.root = node
            else:
                if l == 1:
                    parent.left = node
                else:
                    parent.right = node
            if median_index > 0:
                queueObj = QueueObj(vectors[:median_index], depth + 1, node, 1, 0)
                queue.append(queueObj)
            if median_index < m - 1:
                queueObj = QueueObj(vectors[median_index + 1:], depth + 1, node, 0, 1)
                queue.append(queueObj)
