try:
    with open("test1.txt", "w", encoding="utf-8") as test:
        test.write("123")
except IOError:
    print("Error")