from typing import List

def two_sum(nums: List[int], target: int) -> List[int]:
    """Return indices of two numbers whose sum equals target, or [-1, -1] if none."""
    seen: dict[int, int] = {}          # value -> index
    for i, num in enumerate(nums):
        complement = target - num
        if complement in seen:         # partner found
            return [seen[complement], i]
        seen[num] = i                  # remember current number
    return [-1, -1]                    # <-- moved outside the loop


# Quick sanity checks
print(two_sum([2, 7, 11, 15], 9))          # [0, 1]
print(two_sum([3, 2, 4], 6))               # [1, 2]
print(two_sum([1, 2, 3], 7))               # [-1, -1]
print(two_sum([-1, -2, -3, -4], -6))       # [1, 3]
print(two_sum([5], 5))                     # [-1, -1]
