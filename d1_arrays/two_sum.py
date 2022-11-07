class TwoSum:
    """Given an array of ints, return the indices of the 2 numbers that add up to a given target."""

    def __init__(self, nums: list, target: int) -> None:
        
        self.nums = nums
        self.target = target
        
    def get_indices_bf(self) -> list:
        if (self.nums is not None) and (len(self.nums) > 1):
            for p1 in range(len(self.nums) - 1):
                value_to_find = self.target - self.nums[p1]
                for p2 in range(p1+1, len(self.nums)):
                    if self.nums[p2] == value_to_find:
                        indices = [p1, p2]
                        return indices
        return None

    @staticmethod
    def test():
        assert TwoSum([], 10).get_indices_bf() is None, "Empty array case does not pass test."
        assert TwoSum([1], 10).get_indices_bf() is None, "Length one array case does not pass test."
        assert TwoSum([1, 2], 3).get_indices_bf() == [0, 1], "Length 2 array case does not pass test."
        assert TwoSum([1,2,3,4], 10).get_indices_bf() is None, "No solution case does not pass test."
        assert TwoSum([1,5,2,3], 7).get_indices_bf() == [1, 2], "Did not find existing solution."
        print("Test cases passed.")

if __name__ == "__main__":
    TwoSum.test()