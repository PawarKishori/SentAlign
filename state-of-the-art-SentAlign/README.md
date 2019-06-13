

Readme

1.Copy Hindi text from the PDF to a textfile(name it as Hin_in). This textfile is the input for Walkman-Fontconverter.
We will get wx file as an output.

2.This wx fie is the input for Convert_utf_wx's wx_to_utf8.sh program.(Refer to Convert_utf_wx Readme for execution).
We will get utf file, (name it as hindi_1) as an output.

3.Copy English text from the PDF to a textfile, (name it as english_1).
Now we have 2 files hindi_1 and english_1.

4.Run champollion-1.2 by pasting hindi_1 and english_1 in Major-TH-Tool folder(refer Readme in Major-TH-Tool folder).
We will be getting a sentence aligned merge file as an output.

5.Now we have to split that merge file into hindi and english separate files using split_merged_file.py .
WE will get 2 files containing english and hindi texts.

6.On the hindi text file created in step 5, run utf8_to_wx.sh program from Convert_utf_wx folder(refer to Readme in the folder for the same).
The hindi file feed as input will be converted to wx format.

7.On this wx format file run pre_punc.sh program as follows:
pre_punc.sh path/to/file
ex: pre_punc.sh /home/rajrajeshwari/Convert_utf_wx/myout (give extension if any)

We will get the output file with the same name but all the labels will be removed.



 



