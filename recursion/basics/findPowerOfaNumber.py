'''
    simple approach: return 1 if n == 0 otherwise return x * pow(n-1)
    optimal approach: return x * half * half for odd power otherwise half * half
'''
def pow(x, n):
    if n == 0:
        return 1
    if n % 2 == 0:
        half = pow(x, n//2)
        return half * half
    else:
        half = pow(x, n-1//2)
        return x * half * half
