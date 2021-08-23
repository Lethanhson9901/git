import os

# with open('ten.txt', 'r') as f:
#     lines = f.readlines()
#     count = 0
#     for line in lines:
#         print(line.split('.')[1][:-1])
#         with open('ten_merge.txt', 'a') as fout:
            
#             fout.write(line.split('.')[1][:-1])
#             if (count % 5 == 0):
#                 fout.write('\n')
#         count+=1
#     fout.close()
# f.close()

with open('ten_merge.txt', 'r') as f:
    lines = f.readlines()
    count = 150001
    for line in lines:
        x = str(count) + '|' +line
        with open('ten_merge_2.txt', 'a') as fout:
            fout.write(x)
        count+=1
    fout.close()
f.close()