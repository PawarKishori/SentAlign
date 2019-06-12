-----------------------------------------------------------------------------------------------------------------------------------------------
This is README for installation of fontconverter.
-----------------------------------------------------------------------------------------------------------------------------------------------
1.Unzip folder the roja_font_converter folder
2.Preriquisites - install flex,lex. 
    -command to install flex is- 
          sudo apt-get update
          sudo apt-get install flex
    -command to install lex is-
          sudo apt-get upgrade
          sudo apt-get install bison

3.In fontconversion.sh the 7-line should be -
./mapping_Walkman_Chankya_to_Unicode.out < $1.tmp1_2 >  $1.tmp2 
------------------------------------------------------------------------------------------------------------------------------------------------
 RUN below commands to use Font-converter
------------------------------------------------------------------------------------------------------------------------------------------------
1. sh compile.sh

2. sh addseparator.sh   
      Note:: provide 'args' file to run separately. 
             this shell adds a separator for english word in hindi xml file
             (to avoid font conversion of an english word)

3. sh fontconversion.sh  <file>
      Ex:  sh fontconversion.sh HND
           O/p::  HND.wx
		(Note: Input can be xml or text
		       If input is not xml then no need to run step 2.)



