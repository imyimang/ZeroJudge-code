while True:
    try:
        import re
        a = input().lower()
        a = re.sub(r'[^a-z]', '', a)
        b = {}
        c = 0
        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
                    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for char in a:
            if char in letters:
                if not char in b:
                    b[char] = 0
                b[char] += 1
        for key in b:
            if b[key] % 2 == 1:
                c+=1
        if c>1:
            print("no...")
        else:
            print("yes !")
    except EOFError:
        break
#這題有點難 我是先把輸入全部轉成小寫然後用正規表達式挑出字母
#然後計算每個字母出現的次數，出現奇數次數的字母最多只能有一個，超過就無法重組成迴文
