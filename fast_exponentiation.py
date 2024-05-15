def fast_pow(a, b):
    state = (a, 1, b)
    while state[2] != 0:
        r = state[2] % 2
        if r == 0:
            state = (state[0] ** 2, state[1], state[2]/2)
        elif r == 1:
            state = (state[0] ** 2, state[1] * state[0], (state[2] - 1)/2)
    return state[1]

# only works on natural numbers a, b

print("fast_pow(0, 0):", fast_pow(0, 0))
print("fast_pow(5, 4):", fast_pow(5, 4))