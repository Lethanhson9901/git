import os
import glob

#Change directory to your directory
audio_dir = 'test/audio'
srt_dir = 'test/srt'
out_dir = 'test/norm_audio'

def gen_list_file (dir):
    list_files = []
    for filename in glob.glob(os.path.join(dir, '*')):
        list_files.append(filename.split('/')[-1][:-4])
    #print(list_files)
    return list_files

def norm_audio(srt_dir, audio_dir):
    list_srts = gen_list_file(srt_dir)
    list_audios = gen_list_file(audio_dir)
    common_s = set(list_srts) & set(list_audios)
    diff_s = set(list_srts) ^ set(list_audios)
    for i in common_s:
        print(f'{out_dir}/{i}.wav')
        os.system(f'ffmpeg -i {audio_dir}/{i}.m4a -ac 1 -ar 16000 {out_dir}/{i}.wav')
    print(f'#file convert: {len(common_s)}')
    print(f'#file not convert: {len(diff_s)}')
    if len(diff_s) >= 0:
        print(f'Please check careful: {diff_s}')
    
norm_audio(srt_dir, audio_dir)

# os.system(f'ffmpeg -i test/audio/00114-00205.m4a')
# os.system(f'ffmpeg -i test/norm_audio/00114-00205.wav')
