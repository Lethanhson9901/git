### CHANGE ME!
# directory with wav files that need TextGrids
dir$ = "/home/son/Downloads/hhp/scripts/preprocess/test/piece_audio/"
word_dir$ = "/home/son/Downloads/hhp/scripts/preprocess/test/piece_word/"
out_dir$ = "/home/son/Downloads/hhp/scripts/preprocess/test/textGrid/"

# text of transcript
text$ = "Here is the full text of my transcript. Please change me!"
###

## Maybe change me
# insert initial boundary 200 ms from start of file
boundary_start = 0.200

# insert final boundary 500 ms from end of file
boundary_end = 0.500
##

Create Strings as file list: "files", dir$ + "*.wav"
nFiles = Get number of strings




for i from 1 to nFiles
	selectObject: "Strings files"
	filename$ = Get string: i
	basename$ = filename$ - ".wav"
	Read Strings from raw text file: word_dir$ + basename$ + ".txt"
	numberOfStrings = Get number of strings

	for stringNumber from 1 to numberOfStrings
		string$ = Get string: stringNumber
		
	endfor
	Read from file: dir$ + basename$ + ".wav"
	dur = Get total duration
	To TextGrid: "utt", ""
	Insert boundary: 1, boundary_start
	Insert boundary: 1, dur-boundary_end
	Set interval text: 1, 2, string$
	Save as text file: out_dir$ + basename$ + ".TextGrid"
	select all
	minusObject: "Strings files"
	Remove
	
endfor