Write a program that performs certain processing on the manga.txt file that contains data about manga. 
One line of the file contains information about a single manga volume: 
manga name (one or more words)
publisher name (one or more words)
publication date in mm.yyyy format
number of pages in the volume (positive integer),
and page numbers on which start the chapters within the volume (arbitrary number of positive integers).
All data is separated by exactly one comma (,) and any number of blank characters. 
Based on the input file, it is necessary to create a text file that will contain information 
about the manga of the publisher whose name is specified in the standard input. 
The name of the output file consists of the name of the publisher and the suffix .txt. 
If the name of the publisher consists of several words, they should be separated by an underscore (_). 
Each pair of lines in this file contains data about one manga. 
The first line contains the following information: 
the name of the manga, 
the number of published volumes, 
the total number of chapters in all published volumes, and the average chapter length written to two decimal places.
The second row contains the lengths of all manga chapters. Chapters are sorted in ascending order by publication date. 
The manga are sorted ascending by ASCII/UTF encoding. Data is separated by exactly one comma (,) and exactly one blank character. 
If the given publisher has not published any manga, do not print anything.

The program should:

Load the publisher name from standard input.
Loads data from the given file.
Perform the required processing according to the task text.
Forms an output file according to the task text.
Takes care and processes possible exceptions that may arise during program operation.