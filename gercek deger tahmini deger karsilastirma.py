import math

def taylor_exp(x, n):
    # f(0) = 1
    result = 1
    # f'(0) = 1
    term = 1
    for i in range(1, n+1):
        # f''(0), f'''(0), ... hesapla
        term *= x / i
        result += term
    return result

# x=2 ve 5 iterasyonlu değeri hesapla
x = 2
n = 5
result = taylor_exp(x, n)

# gerçek değer ile karşılaştır
true_value = math.exp(x)
print("Gerçek değer:", true_value)
print("Tahmini değer:", result)
