try:
    file = open('output.txt', 'w')
    writeText = input('Enter text to write to the file: ')
    file.write(writeText+'\n')
    print('Data successfully written to output.txt.\n')
    file.close()
    file = open('output.txt', 'a')
    appendText = input('Enter text to append: ')
    file.write(appendText)
    print('Data successfully appended\n')
    file.close()
    file = open('output.txt', 'r')
    print('Final content of output.txt:')
    readText = file.read()
    print(readText)
    file.close()


except FileNotFoundError:
    print("Error: The File 'output.txt' was not found.")
