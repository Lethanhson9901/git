import os
import errno

split_folder = '/home/son/Downloads/hhp/split/'
file_name = 'preprocess.txt'

file_dir = os.path.join(split_folder, file_name[:-4])
os.makedirs(file_dir, exist_ok=True)
num_of_char = 1000
file = open(file_name, "rt")
data = file.read()
print(len(data))
#words = data.split()
temp = data
count = 0 
i = 0
while count+num_of_char < len(data):
    cut_file = file_dir +'/'+ file_name[:-4]+ '_' + str(i) +'.txt'
    print(cut_file)
    x = temp[count:count+num_of_char].rindex(".")
    with open (cut_file, 'w+') as f:
        f.write(temp[count:count+x+1])
        #print(temp[count:count+x+1])
    f.close()
    print('------------------------------------')
    count = count + x + 1
    i +=1
left = temp[count:len(data)]
final_cut_file = file_dir +'/'+ file_name[:-4] + '_' + str(i) +'.txt'
with open(final_cut_file, 'w+') as final:
    final.write(left)
f.close()
