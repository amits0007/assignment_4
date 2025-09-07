try:
    with open('sample.txt','r') as file1:
        reading_file=file1.read()
        print(reading_file)
except FileNotFoundError:
    print("the file 'sample.txt' not found")
