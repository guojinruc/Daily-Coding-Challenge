class TwoSum:
    """Given an array of ints, return the indices of the 2 numbers that add up to a given target."""
    
    @staticmethod
    def get_indices_bf(nums: list, target: int) -> list:
        if (len(nums) > 1):
            for p1 in range(len(nums) - 1):
                value_to_find = target - nums[p1]
                for p2 in range(p1+1, len(nums)):
                    if nums[p2] == value_to_find:
                        indices = [p1, p2]
                        return indices
        return None

    @staticmethod
    def get_indices(nums:list, target: int)-> list:
        mapping = {}
        if (len(nums) > 1):
            for p1 in range(len(nums)):
                p2 = mapping.get(nums[p1]) 
                if p2 is not None:
                    return [p2, p1]
                else:
                    value_to_find = target - nums[p1]
                    mapping[value_to_find] = p1 
            return None


    @staticmethod
    def test(method):
        assert getattr(TwoSum, method)([], 10) is None, "Empty array case does not pass test."
        assert getattr(TwoSum, method)([1], 10) is None, "Length one array case does not pass test."
        assert getattr(TwoSum, method)([1, 2], 3) == [0, 1], "Length 2 array case does not pass test."
        assert getattr(TwoSum, method)([1,2,3,4], 10) is None, "No solution case does not pass test."
        assert getattr(TwoSum, method)([1,5,2,3], 7) == [1, 2], "Did not find existing solution."
        print("Test cases passed.")

if __name__ == "__main__":
    TwoSum.test("get_indices_bf")
    TwoSum.test("get_indices")