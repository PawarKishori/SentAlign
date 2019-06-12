-----------------------------------------------------------------------------------------------------------------------------------------------
Installation of charus_wx
-----------------------------------------------------------------------------------------------------------------------------------------------
Compilation steps:
1. sh comp.sh utf8_to_wx
2. sh comp.sh replace_nukta
3. sh comp.sh replace_a_
4. sh comp.sh remove_non_ascii_chars
5. sh comp.sh wx_to_utf8
6. sh comp.sh wx_replace_a_
7. sh comp.sh remove_unnecessary_dev_chars


Step to run:
To convert UTF8 to wx:
sh utf8_to_wx.sh < input_utf8_file > output_wx_file

To convert wx to UTF8:
sh wx_to_utf8.sh < input_wx_file > output_utf8_file
