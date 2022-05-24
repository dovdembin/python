from array import array
a = array('H', [4000, 10, 700, 22222])
print(sum(a))
print(a[1:3])

# ================================

from collections import deque
d = deque(["task1", "task2", "task3"])
d.append("task4")
print("Handling", d.popleft())

# BFS
# unsearched = deque([starting_node])
# def breadth_first_search(unsearched):
#     node = unsearched.popleft()
#     for m in gen_moves(node):
#         if is_goal(m):
#             return m
#         unsearched.append(m)

# =============================

import bisect
scores = [(100, 'perl'), (200, 'tcl'), (400, 'lua'), (500, 'python')]
bisect.insort(scores, (300, 'ruby'))
scores