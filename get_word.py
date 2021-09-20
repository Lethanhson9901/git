import os

csv_file = 'output.csv'
text_file = 'txt/bunch_of_strings.txt'

with open(csv_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        text = (line.split('|')[1][:-1]) + ' '
        #print(text)
        with open(text_file, 'a') as fout:
            fout.write(text) 
    fout.close()
f.close()

with open(text_file, 'r') as fout:
    strings = fout.read()
    words = set(strings.split())
    print(len(words))
    #print(len(words))
    # print(len(strings.split()))
    with open('txt/words.txt', 'a') as f:
        for i in words:
            f.write(i)
            f.write('\n')
    f.close()
fout.close()