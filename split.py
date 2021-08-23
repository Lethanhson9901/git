# with open('scripts.txt', 'r') as f:
#     lines = f.readlines()
#     for line in lines:
#         x = line.split('|')[:-1]
#         print(x)
#         with open('out.txt', 'a') as fout:
#             fout.write(x[0] + '|')
#             fout.write(x[1])
#             fout.write('\n')
#     fout.close()
# f.close()
counter  = 15241
with open('prompts.txt', 'r') as f:
    lines = f.readlines()
    for line in lines:
        x = line.split(' ', 1)[1].lower()
        with open('prompts_lower.txt', 'a') as fout:
            fout.write(str(counter) + '| ' + x)
        counter+=1
    fout.close()
f.close()

