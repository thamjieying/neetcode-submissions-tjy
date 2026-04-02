from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses <= 0: 
            return True

        # build the adjacency list and indegree count: 
        indegree = { i: 0 for i in range(numCourses) }
        adjacency_list = { i : [] for i in range(numCourses) }

        # populate adjacency list
        for src_course, dep_course in prerequisites: 
            indegree[dep_course] +=1
            adjacency_list[src_course].append(dep_course)
        
        #start a queue with course that has no dependency
        q = deque()
        for course, count in indegree.items():
            if count == 0: 
                q.append(course)
        
        # remove all course without dependency recursively
        counter = 0
        while q: 
            course = q.popleft()
            counter +=1
            for nei in adjacency_list[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)

        return counter == numCourses  

