while True:
    try:
        a = int(input())
        b = list(map(int, input().split(" ")))
        
        b = sorted(b, key=lambda x: (x % 10, -x))
        
        print(' '.join(map(str, b)))
    except EOFError:
        break

#原本是直接用a104的泡沫排序法來改，但效率太低了會TLE，所以後來改用內建的sorted
