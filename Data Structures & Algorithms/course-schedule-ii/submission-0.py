class Solution:
    def findOrder(self, numCourses: int, prerequisites: list[list[int]]) -> list[int]:
        # Step 1: Map each course to the list of courses it depends on
        pre_map = {i: [] for i in range(numCourses)}
        for crs, pre in prerequisites:
            pre_map[crs].append(pre)

        res = []
        visiting = set()  # Tracks current DFS recursion stack (detects cycles)
        visited = set()   # Tracks courses completely finished and added to res

        def dfs(crs: int) -> bool:
            # Cycle detected: We circled back into the active recursion chain
            if crs in visiting:
                return False
            # Already completed and added to res: Skip to avoid duplicate additions
            if crs in visited:
                return True

            # Mark course as actively being visited
            visiting.add(crs)

            # Visit every prerequisite of this course first
            for pre in pre_map[crs]:
                if not dfs(pre):
                    return False

            # Backtrack: Remove from current recursion branch
            visiting.remove(crs)
            # Mark permanently as completed
            visited.add(crs)

            # Post-Order: Add course only AFTER all its prerequisites are in res
            res.append(crs)
            return True

        # Step 2: Traverse every course (handles disconnected components)
        for crs in range(numCourses):
            if not dfs(crs):
                return []

        return res