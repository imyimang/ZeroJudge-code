def f(n):
    return (n*(n+1))//2
    
def g(n):
    return f(n)*(n+1)-n*(n+1)*(2*n+1)//6

while True:
    try:
        a = int(input())
        print(f(a),g(a))

    except EOFError:
        break