def write_to_file(text, file_name):
    with open(file_name, mode='a+', encoding='utf-8') as f:
        f.write(text + '\n')
        f.seek(0)
        lines = f.readlines()

    for i, line in enumerate(lines):
        if (i + 1) % 2 == 0:
            print(line.strip())

write_to_file('some text', 'test.txt')
