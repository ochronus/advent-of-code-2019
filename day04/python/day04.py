range_low, range_high = [int(x) for x in open('../input.txt').read().strip().split('-')]

def is_valid_p1(pw_candidate):
    digits = str(pw_candidate)
    # sorted == original means they were never decreasing
    return list(digits) == sorted(digits) and any(digits[i] == digits[i+1] for i in range(5))

def is_valid_p2(pw_candidate):
    digits = str(pw_candidate)
    return list(digits) == sorted(digits) and any(
            digits[i] == digits[i+1] and 
            (i == 0 or digits[i-1] != digits[i]) and
            (i == 4 or digits[i+2] != digits[i])
            # counter-examples for above (last 3 conditions for the repeated groups):
            # 123336 --> 333 --> TTF (because digits[i+2] == digits[i])
            # 111234 --> 111 --> TTF (because digits[i+2] == digits[i])
            # 111234 --> 112 --> TFT (digits[i-1] == digits[i])
            # 123444 --> 444 --> TTF (because digits[i+2] == digits[i])
        for i in range(5))

def is_valid_p2_optimized(pw_candidate):
    pw_candidate_str = str(pw_candidate)
    any(pw_candidate_str.count(digit) == 2 for digit in list(set(pw_candidate_str))) and is_valid_p1(pw_candidate)

print(sum(1 for pw_candidate in range(range_low, range_high+1) if is_valid_p1(pw_candidate)))
print(sum(1 for pw_candidate in range(range_low, range_high+1) if is_valid_p2_optimized(pw_candidate)))
