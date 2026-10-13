class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # Step 1: Build adjacency list: course -> list of prerequisite courses
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        # visiting: tracks nodes currently in the active DFS path (for cycle detection)
        visiting = set()
        # visited: tracks nodes already verified to have no cycles (optimization)
        visited = set()

        def dfs(crs: int) -> bool:
            # Cycle detected: We encountered a course currently on the active path
            if crs in visiting:
                return False
            # Already verified: This course can be completed safely
            if crs in visited:
                return True

            # Mark course as currently being explored
            visiting.add(crs)

            # Explore all prerequisites for the current course
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False

            # Backtrack: Remove from current active path
            visiting.remove(crs)
            # Cache: Mark as fully verified with no cycles
            visited.add(crs)

            return True

        # Step 2: Run DFS for every course (in case the graph is disconnected)
        for crs in range(numCourses):
            if not dfs(crs):
                return False

        return True
        