class TimeMap:

    def __init__(self):
        # Step 1: Initialize a dictionary where:
        # Key -> string (e.g., "alice")
        # Value -> list of pairs: [[value, timestamp], [value, timestamp], ...]
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key doesn't exist yet, initialize it with an empty list
        if key not in self.store:
            self.store[key] = []
        # Append the [value, timestamp] pair
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        # Get the list of pairs for the key; if it doesn't exist, return empty string
        values = self.store.get(key, [])

        # Step 2: Binary search on the list of pairs based on the timestamp
        l, r = 0, len(values) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            # Check the timestamp of the middle pair
            if values[mid][1] <= timestamp:
                # This is a valid historic value! Save it as a temporary result.
                # Then look to the right to see if there's a closer/more recent valid timestamp.
                res = values[mid][0]
                l = mid + 1
            else:
                # If the middle timestamp is strictly greater than the requested timestamp,
                # it's from the future. Look to the left half.
                r = mid - 1
                
        return res
