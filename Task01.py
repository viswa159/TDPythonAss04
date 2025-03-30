try:
    with open('sample.txt','r') as file:
        print('Reading file content:')
        i = 1
        for line in file:
            print(f"Line {i}: {line.strip()}")
            i += 1
    file.close()
except FileNotFoundError:
    print(f"Error: The File '{'sample.txt'}' was not found.")
