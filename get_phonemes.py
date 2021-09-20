import os

consonants = [
    'ngh', 
    'ch', 'gh', 'gi', 'kh', 'ng', 'nh', 'ph', 'qu', 'tr', 'th', 
    'b', 'c', 'd', 'đ', 'g', 'h', 'k', 'l', 'm', 'n', 'p', 'r', 's', 't', 'v', 'x'
]
vowels = (
    ['a', 'ă', 'â', 'e', 'ê', 'i', 'o', 'ô', 'ơ', 'u', 'ư', 'y'] +
    ['á', 'ắ', 'ấ', 'é', 'ế', 'í', 'ó', 'ố', 'ớ', 'ú', 'ứ', 'ý'] +
    ['à', 'ằ', 'ầ', 'è', 'ề', 'ì', 'ò', 'ồ', 'ờ', 'ù', 'ừ', 'ỳ'] +
    ['ả', 'ẳ', 'ẩ', 'ẻ', 'ể', 'ỉ', 'ỏ', 'ổ', 'ở', 'ủ', 'ử', 'ỷ'] +
    ['ã', 'ẵ', 'ẫ', 'ẽ', 'ễ', 'ĩ', 'õ', 'ỗ', 'ỡ', 'ũ', 'ữ', 'ỹ'] +
    ['ạ', 'ặ', 'ậ', 'ẹ', 'ệ', 'ị', 'ọ', 'ộ', 'ợ', 'ụ', 'ự', 'ỵ']
)

punctuations  = ['.', '?', '"', '\'', ',', '-', '–', '!', ':', ';', '(', ')', '[', ']', '\n' ]

alphabet = sorted(set(''.join(consonants + vowels)))
print(alphabet)
# phonemes = sorted(consonants + vowels, key=len, reverse=True)
phonemes = consonants + vowels
print(phonemes)

import unicodedata
def text_to_phonemes(text, keep_punctuation=False):
  text = unicodedata.normalize('NFKC', text.strip().lower())
  idx = 0
  out = []
  while idx < len(text):
    # length: 3, 2, 1
    for l in [3, 2, 1]:
      if idx + l <= len(text) and text[idx: (idx+l)] in phonemes:
        out.append(text[idx: (idx+l)])
        idx = idx + l
        break
    else:
      if idx < len(text):
        if keep_punctuation and text[idx] in punctuations:
          out.append(text[idx])
        if text[idx] == ' ':
          out.append(text[idx])
      idx = idx + 1
  return out

lines = open('txt/words.txt', 'r').readlines()
f = open('txt/phonemes.txt', 'w')
for line in lines:
  t = ' '.join(text_to_phonemes(line))
  f.write(t + '\n')
f.close()

ws = open('txt/words.txt').readlines()
ps = open('txt/phonemes.txt').readlines()
f = open('txt/lexicon.txt', 'w')
for w, p in zip(ws, ps):
  w = w.strip()
  p = p.strip()

  # this is a hack to match phoneme set in the vietTTS repo
  p = p.split()
  p = [ " ".join(list(x)) for x in p]
  p = " ".join(p)
  # hack ends
  
  if w == "q":
    p = "qu i"
  f.write(f'{w}\t{p}\n')
f.close()