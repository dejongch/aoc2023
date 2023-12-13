from functools import cache
def count_permutations(pattern, guide):
    pattern_len, guide_len = len(pattern), len(guide)

    @cache
    def dp(index, guide_index, consecutive_hashes):
        # Base case: Reached the end of the pattern
        if index == pattern_len:
            # Special handling if we're in the middle of a hash group
            if consecutive_hashes > 0:
                # Check if we are at the last guide number and it matches the current hash count
                return guide_index == guide_len - 1 and consecutive_hashes == guide[guide_index]
            else:
                return guide_index == guide_len

        count = 0

        # If the current character is '.', or '?' acting as '.'
        if pattern[index] in {'.', '?'}:
            # If we just completed a group of '#' as per the guide, move to the next group
            if guide_index < guide_len and consecutive_hashes == guide[guide_index]:
                count += dp(index + 1, guide_index + 1, 0)
            # If we are not in a group of '#'
            elif consecutive_hashes == 0:
                count += dp(index + 1, guide_index, 0)

        # If the current character is '#', or '?' acting as '#'
        if pattern[index] in {'#', '?'}:
            # If adding a '#' does not exceed the current guide number
            if guide_index < guide_len and consecutive_hashes < guide[guide_index]:
                count += dp(index + 1, guide_index, consecutive_hashes + 1)

        return count

    # Start the recursion from the beginning of the pattern string
    return dp(0, 0, 0)

number_of_arangements = 0

with open("input.txt", 'r') as file:
    for line_index, line in enumerate(file):
        springs, guide = line.strip().split()
        springs = "?".join([springs]*5)
        guide = [int(item) for item in guide.split(",")]*5
        
        number_of_arangements += count_permutations(springs, guide)
print(number_of_arangements)
