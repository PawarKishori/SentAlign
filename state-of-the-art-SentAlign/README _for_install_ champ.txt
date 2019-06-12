=========================================================
# This is readme.md [with DETAILS OF CODES]
=========================================================
This tool works in 2 iterations.

# pre-requisite :
1)i)for Termsuite-----
 jdk and jre installation hasto be done:-(link: https://www.wikihow.com/Install-Oracle-Java-on-Ubuntu-Linux)

 ii)for Tree tagger-----
 models folder has to be generated under the path specified below using the command-
 (Major_TH_Tool/TERMSUITE_WORKSPACE/treetagger/): ln -s lib models

2)For Champollion----
 run ./test_installation and check whether installation is good or not. 

3)All files of Major_TH_Tool and Champollion tool should be  made in executable form 
command: chmod u+x *


===========================================================
1. git clone Major-TH-Tool

2. git clone Champollion Tool Kit V1.2 and move this folder inside Major-TH-Tool folder 

3. save english files as english_1 without .txt extension(input corpus) in Major-TH-Tool folder 

4. save hindi files as hindi_1 without .txt extension(input corpus) in Major-TH-Tool folder. 

5. In first iteration:------------ run ./tool.sh from the Major-TH-Tool folder.
Following files/folders will be generated:----AlignedFiles_1,ArrowFiles_1,Module_E_1,Module_H_1,Omitted,a_english_1.txt,eng,hnd,module_aligned_1.txt,no_omitted_1,only_omitted_1

6. For second iteration:--------------

	i)All the previously generated files should be removed from Major-TH-Tool folder and pasted into separate folder.
	ii)From updated_term_match/operated_corpus/doc_req copy the hindi_word.txt file into Dictionary_processing folder.
	iii)open the terminal from Dictionary_proessing folder and run the command: bash process_dict.sh hindi_word.txt. A ehdict.utf8.txt file will be generated inside the Dictionary_processing folder.
	iv)Copy the above ehdict.utf8.txt file and append it inside champollion1.2/lib/ehdict.utf8.txt(default dictionary already present in champollion1.2).
	v)Finally run the command : bash run_indiv_module.sh from Major-TH-Tool folder. 


======================================================
# END TASK
-----------------------------------------------------

1. copy  merge_1 file  from AlignedFiles_1 folder generated in second iteration in separate folder.Also copy reverse_replace.sh in same folder.

2. run command: bash reverse_replace.sh merge_1

3. open the file: do ctrl+h and replace "\n ; " with " ; "
[Coding not present inside reverse_replce.sh (cannot operate)]

4. <merge_1> is your final output file.

[The tool introduces its own ";" while aligning and original ";" may be lost at the end]

=========================================================

[ABOUT FILES]
==============================================
# run_indiv_module.sh
----------------------------------------------

Uses codes:
1. run_sentence_alignment.sh
-for initial paragraph alignment

2. removes empty lines from original files

3. find_and_replace.sh
-for preprocessing of files.
-replaces ; with @
-swaps {[.?!]'} with {'[.?!]}

4. ./align-eng-hin.out
-for producing aligned files of paragraphs (check purpose)

5. div_eng_hin.py
-for creating paragraph files of individual module and removing complete paragraphs that did not align into Omitted folder (backtrack)

6. rename_e.py and rename_h.py
-for renaming files into increasing order
(if a file number is not available the tool crashes)

7. split_para_and_feed.sh
-for running sentence alignment on paragraph files

================================================
# ./align-eng-hin.out  [IMPORTANT]
------------------------------------------------

run command:
	bash compile.sh
-to produce align-eng-hin.out file from align-eng-hin.c file and check the champollion installation

=================================================
# div_eng_hin.py
-------------------------------------------------

requires python
command: python div_eng_hin.py <champollion_output_file> <english_file> <hindi_file> <count_as_a_number(naming purpose[IMP])>

-dividing complete file into paragraphs as they are aligned by champollion
-moves omitted paragraphs into Omitted file along with their module and paragraph number (backtracking)

=================================================
# split_para_and_feed.sh
-------------------------------------------------

uses codes:

1. split_english_para.sh :
	command: bash split_english_para.sh <paragraph_file_english> <sentences_ouput_file_english>
	example: bash split_english_para.sh ./Module_E_$1/e_$i.txt sen_e_$i

	-for accessing paragraph file inside english module and creating corresponding sentence splitted files

2. split_hindi_para.sh :
	command: bash split_hindi_para.sh <paragraph_file_hindi> <sentences_ouput_file_hindi>
	example: bash split_hindi_para.sh ./Module_H_$1/h_$i.txt sen_h_$i

	-for accessing paragraph file inside english module and creating corresponding sentence splitted files

3. run_sentence_alignment.sh :
	-produces alignment arrow files using champollion
	command: bash run_sentence_alignment.sh <english_sentence_file> <hindi_sentence_file>
	-output format:
1 <=> 1
2 <=> 2,3
3,4 <=> omitted
etc...

4. omitted_lines.py :
	-copies the sentences that are not aligned into a file "abc.txt" later appended every new file data into "omitted_lines.txt" file

5. ./align-eng-hin.out:
	-aligning the sentences next to each other
	-output format: english_sentence <=> hindi_sentence

6. At the end every unrequired file in the main folder is copied to another folder for readablity purpose.

7. Finally sentences aligned files of the module are merged into single file.

