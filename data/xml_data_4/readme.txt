Congratulations, you received export from OpenSubtitles. 

How to process the data:
1) extract metadata file export.txt.gz to get the txt file, which is actually CSV TAB delimited file.
2) as SECOND Column you will find "IDSubtitleFile" - which means ID of subtitle file, take this ID
3) IDSubtitleFile is for example "12345" so you will find this subtitle in path as 5/4/3/2/12345.gz
   (just reverse the numbers 12345 => 54321 and then make 4 sub-directories path 5/4/3/2/ where is located
   file as 5/4/3/2/12345.gz) - which is subtitles itself, just extract it. 


We hope this helps and it is clear how to link Subtitle Files with meta data located in export.txt.gz
We needed to do this, because 1 directory can not hold too much files, it is slow...so if you want to save
a lot of files on hard drive, now you know the simple way :)

Enjoy the export and don't forget to put references to OpenSubtitles everywhere where it is appropriate. 
