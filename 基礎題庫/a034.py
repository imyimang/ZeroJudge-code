while True:
    try:
        number = int(input())
        print(bin(number)[2:])
    except:
        break