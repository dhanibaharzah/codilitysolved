def solution(N):
    maximum_gap = 0
    current_gap = 0
    while N > 0 and N%2 == 0: # Skip the tailing zero(s)
        N //= 2
    while N > 0:
        remainder = N%2# Inside a gap
        if remainder == 0:
            current_gap += 1 
        else: # Gap ends
            if current_gap != 0:
                maximum_gap = max(current_gap, maximum_gap)
                current_gap = 0
        N //= 2
    return maximum_gap
