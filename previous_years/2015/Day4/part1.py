import hashlib

def find_lowest_number(prefix, num_zeros):
    counter = 0

    while True:
        candidate = f"{prefix}{counter}"
        hash_result = hashlib.md5(candidate.encode()).hexdigest()

        if hash_result.startswith('0' * num_zeros):
            return counter

        counter += 1

# Example usage:
prefix = "iwrupvqb"
num_zeros = 5

result = find_lowest_number(prefix, num_zeros)
print(f"The lowest number to get a hash with {num_zeros} leading zeros is: {result}")
