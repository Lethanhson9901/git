import re
txt_file = 'test.txt'

def change_text(text):
    text = text.lower().strip()
    # text = re.sub('đ/c','đồng chí', text)
    # text = re.sub('facebook', 'phây búc', text)
    # text = re.sub('site', 'sai', text)
    # text = re.sub('timviec365', 'tìm việc ba sáu năm', text)
    # text = re.sub('traffic', 'tra phích',text)
    # text = re.sub('track', 'trách',text)
    # text = re.sub('key', 'ki',text)
    # text = re.sub('tag','tác',text)
    # text = re.sub('.com', ' chấm com', text)
    # text = re.sub('.vn', ' chấm vê nờ', text)
    # text = re.sub('banthe24h', 'bán thẻ hai từ giờ', text)
    # text = re.sub('googmap', 'gu gồ máp', text)
    # text = re.sub('ko', 'không', text)
    # text = re.sub('min', 'tối thiểu')
    # text = re.sub('1', 'một', text)
    # text = re.sub('2', 'hai', text)
    # text = re.sub('3', 'ba', text)
    # text = re.sub('4', 'bốn', text)
    # text = re.sub('5', 'năm', text)
    # text = re.sub('6', 'sáu', text)
    # text = re.sub('7', 'bảy', text)
    # text = re.sub('8', 'tám', text)
    # text = re.sub('9', 'chín', text)
    # text = re.sub('0', 'không', text)
    with open ('dict.txt', 'r') as dic:
        lines = dic.readlines()
        for line in lines:
            x = line.split('|')
            #print(x)
            text = re.sub(x[0],x[1][:-1], text)
    text = text.replace('+', 'cộng ')
    text = text.replace('(', ',(')
    
    return text.strip()
with open('preprocess.txt', 'r+') as fout:
    fout.truncate(0)
fout.close()

with open (txt_file, 'r') as f:
    lines = f.readlines()
    for line in lines:
        ok = change_text(line)
        with open('preprocess.txt', 'a') as fout:
            fout.write(ok)
            fout.write('\n')
            #print(ok)
    fout.close()
f.close()