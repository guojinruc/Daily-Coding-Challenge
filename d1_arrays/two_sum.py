class TwoSum:
    """Given an array of ints, return the indices of the 2 numbers that add up to a given target."""

    def __init__(self, arr: list, target: int) -> None:
        self.arr = arr
        self.target = target
        
    def get_indices_bf(self) -> list:
        if (self.arr is not None) and (len(self.arr) > 1):
            for p1 in range(len(self.arr) - 1):
                value_p1 = self.arr[p1]
                value_to_find = self.target - value_p1
                for p2 in range(p1+1, len(self.arr)):
                    if self.arr[p2] == value_to_find:
                        indices = [p1, p2]
                        return indices
        return None

    @staticmethod
    def test():
        assert TwoSum([], 10).get_indices() is None, "Empty array case does not pass test."
        assert TwoSum([1], 10).get_indices() is None, "Length one array case does not pass test."
        assert TwoSum([1, 2], 3).get_indices() == [0, 1], "Length 2 array case does not pass test."
        assert TwoSum([1,2,3,4], 10).get_indices() is None, "No solution case does not pass test."
        assert TwoSum([1,5,2,3], 7).get_indices() == [1, 2], "Did not find existing solution."
        print("Test cases passed.")

if __name__ == "__main__":
    TwoSum.test()