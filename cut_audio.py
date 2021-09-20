import os
import glob
from pathlib import Path
import pysrt
from pydub import AudioSegment


#Change directory to your directory
audio_dir = 'test/norm_audio'
srt_dir = 'test/srt'
out_dir = 'test/piece_audio'
word_dir = 'test/piece_word'
csv_output = 'output.csv'

def gen_list_file (dir):
    list_files = []
    for filename in glob.glob(os.path.join(dir, '*')):
        list_files.append(filename.split('/')[-1][:-4])
    #print(list_files)
    return list_files

def cut_audio():
    list_srts = gen_list_file(srt_dir)
    list_audios = gen_list_file(audio_dir)
    common_s = set(list_srts) & set(list_audios)
    diff_s = set(list_srts) ^ set(list_audios)
    for i in common_s:
        audio_name = audio_dir + '/'+ i + '.wav'
        sub_name = srt_dir + '/'+ i + '.srt'
        csv_output = 'output.csv'
        print(audio_name, sub_name)
        song = AudioSegment.from_file(audio_name)
        subs = pysrt.open(sub_name, encoding='utf-8')

        # Define lambda function convert time to miliseconds 
        time_to_ms = lambda x: (x.hours*3600 + x.minutes * 60 + x.seconds) * 1000 + x.milliseconds

        # Extract data 
        with open(csv_output, 'w') as fd:
            c=0
            for sub in subs:
                c+=1
                # Get start time, end time in miliseconds
                start_ms = time_to_ms(sub.start)
                end_ms = time_to_ms(sub.end)   
                # Audio extracted file name
                audio_extract_name = '{}/{}_{}_{}_{}.wav'.format(out_dir, i, c, start_ms, end_ms)
                #print(audio_extract_name)
                text = str(sub.text)
                
                # Extract file
                extract = song[start_ms:end_ms]
                # Saving 
                extract.export(audio_extract_name, format="wav")
                # # Write to csv file
                fd.write('{}|{}\n'.format(audio_extract_name, text))

                #create word files
                word_file = '{}/{}_{}_{}_{}.txt'.format(word_dir, i, c, start_ms, end_ms)
                with open(word_file, 'w') as f:
                    f.write(text)
                f.close()
    print(f'#file convert: {len(common_s)}')
    print(f'#file not convert: {len(diff_s)}')
    if len(diff_s) >= 0:
        print(f'Please check careful: {diff_s}')

cut_audio()