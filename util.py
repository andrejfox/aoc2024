def read_file():
    with open("input.txt", "r") as file:
        return [line.strip() for line in file]