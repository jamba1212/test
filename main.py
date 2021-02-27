def open_file():
    numbers = [random.randint(1, 100) for x in range(1, 50)]
    numbers.sort()
    with open("text.txt", "w") as f:
        f.write(f'{numbers}')
    with open("text.txt", "r") as x:
        num = x.read()
    return num

print(open_file())