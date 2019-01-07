def thirds(n):
    return n*n*n

value = sorted([36,5,-12,9,21,0],key=thirds)
print(value)