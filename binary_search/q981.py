# 981. Time Based Key-Value Store
# Topics: Hash Table, String, Binary Search, Design, Weekly Contest 121
# Difficulty: Medium

class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        
        # binary search
        l, r = 0, len(values) - 1
        while l <= r:
            m = (l + r) // 2
            if values[m][1] <= timestamp:
                res = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)



if __name__ == "__main__":
    timeMap = TimeMap()
    timeMap.set("foo", "bar", 1)  # store the key "foo" and value "bar" along with timestamp = 1.
    print(timeMap.get("foo", 1))         # return "bar"
    print(timeMap.get("foo", 3))        # return "bar", since there is no value corresponding to foo at timestamp 3 and timestamp 2, then the only value is at timestamp 1 is "bar".
    timeMap.set("foo", "bar2", 4) # store the key "foo" and value "bar2" along with timestamp = 4.
    print(timeMap.get("foo", 4))         # return "bar2"
    print(timeMap.get("foo", 5))         # return "bar2"




