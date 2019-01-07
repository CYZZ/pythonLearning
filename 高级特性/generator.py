
#找出回数
def is_palindrome(n):
    m = str(n)
    for x in range((n+1)//2):
        return m[x] ==m[-1-x]

output = filter(is_palindrome, range(1,1000))
print(list(output))
