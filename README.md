# Unix-Commands

Command line interface that shows a collection of Unix common commands re-implemented in Python 3.6

-------------------------------------------

COMMAND:    cp  source  [destinations...]

It copies a file to single/multiple destinations.
You can rename it while copying. Specify absolute paths for both source and destinations.

Usage Example:

cp  C:/Users/Giacomo/Source/file_to_copy.txt    C:/Users/Giacomo/Destination_1/file_copied.txt    C:/Users/Giacomo/Destination_2/file_copied_1.txt

-------------------------------------------

COMMAND:    mv  source  [destinations...]

It moves a file to single/multiple destinations.
You can rename it while copying. Specify absolute paths for both source and destinations.

Usage Example:

mv  C:/Users/Giacomo/Source/file_to_copy.txt    C:/Users/Giacomo/Destination_1/file_moved.txt    C:/Users/Giacomo/Destination_2/file_moved_2.txt

-------------------------------------------

COMMAND:    diff  file1   file2

It finds differences between files returning a list of words (the words of one file which aren't in the other, and vice versa).

Usage Example:

diff  C:/Users/Giacomo/Source/file_1.txt   C:/Users/Giacomo/Destination_1/file_2.txt

-------------------------------------------

COMMAND:    ls  -t  dir

It show the content of the directory. ls -t show the actual directory, ls <path>  shows the content of the directory specified.

Usage Example:

ls -t

ls C:/Users
