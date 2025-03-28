MAX_TERM_VALUE = 10000

curr_term = 0  # Pehla Fibonacci Number (0)
next_term = 1  # Dusra Fibonacci Number (1)

while curr_term <= MAX_TERM_VALUE:
    print(curr_term)
    term_after_next = curr_term + next_term  # Agla number calculate karna
    curr_term = next_term  # Current term ko update karna
    next_term = term_after_next  # Next term ko update karna