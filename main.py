
#Question 1 — “First Unique Character”

def first_unique_char(s: str) -> int:
    counts = [0] * 26          # Step 1: count occurrences
    for ch in s:
        counts[ord(ch) - ord('a')] += 1

    for i, ch in enumerate(s): # Step 2: find first index with a single occurrence
        if counts[ord(ch) - ord('a')] == 1:
            return i
    return -1
print(first_unique_char("leetcode")) #0
print(first_unique_char("loveleetcode")) #2
print(first_unique_char("aabb")) #1
