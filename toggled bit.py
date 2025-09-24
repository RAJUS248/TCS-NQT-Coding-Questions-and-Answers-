n = int(input())
print(n ^ (1 << n.bit_length()) - 1)

