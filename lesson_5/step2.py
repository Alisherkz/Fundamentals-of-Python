try:
    with open("test2.txt", "r+", encoding="utf-8") as test:
        # test.write("test\npython\nintel\ncomputer")
        s = test.readlines()
        words = 0
        lines = 0
        letters = 0
        for line in s:
            lines += 1
            post = 'out'

            for letter in line:
                if letter != ' ' and post == 'out':
                    words += 1
                    post = 'in'
                elif letter == ' ':
                    post = 'out'

        print("lines:" ,lines)
        print("words:", words)

except IOError:
    print("ERROR")