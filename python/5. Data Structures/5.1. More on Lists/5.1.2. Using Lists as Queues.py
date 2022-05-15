from collections import deque


def list_as_queue():
    queue = deque(["Eric", "John", "Michael"])

    queue.append("Terry")  # Terry arrives # deque(['Eric', 'John', 'Michael', 'Terry'])

    queue.append("Graham")  # Graham arrives # deque(['Eric', 'John', 'Michael', 'Terry', 'Graham'])

    queue.popleft()  # The first to arrive now leaves # deque(['John', 'Michael', 'Terry', 'Graham'])

    queue.popleft()  # The second to arrive now leaves # deque(['Michael', 'Terry', 'Graham'])

    print(queue)  # Remaining queue in order of arrival

    """
    It is also possible to use a list as a queue (list.pop(i) by using pop at index)
    but lists are not efficient because all of the other elements have to be shifted

    """


list_as_queue()