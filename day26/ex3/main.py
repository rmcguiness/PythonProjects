def read_text_file(path):
    with open(file=path) as f:
        lines = f.read().splitlines()
    return lines

text1 = read_text_file('file1.txt')
text2 = read_text_file('file2.txt')

common = [i for i in text1 if i in text2]

print(common)