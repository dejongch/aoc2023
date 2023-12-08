import hashlib

def find_lowest_number(prefix, num_zeros, counter):

    while True:
        candidate = f"{prefix}{counter}"
        hash_result = hashlib.md5(candidate.encode()).hexdigest()

        if hash_result.startswith('0' * num_zeros):
            return counter

        counter += 1

# Example usage:
prefix = "iwrupvqb"
num_zeros = 6

result = find_lowest_number(prefix, num_zeros, 346386)
print(f"The lowest number to get a hash with {num_zeros} leading zeros is: {result}")
