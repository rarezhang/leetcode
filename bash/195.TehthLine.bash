"""
How would you print just the 10th line of a file?

For example, assume that file.txt has the following content:

Line 1
Line 2
Line 3
Line 4
Line 5
Line 6
Line 7
Line 8
Line 9
Line 10
Your script should output the tenth line, which is:
Line 10
[show hint]

Hint:
1. If the file contains less than 10 lines, what should you output?
2. There's at least three different solutions. Try to explore all possibilities.
"""

# solution 1
head -10 file.txt | tail -1 # wrong answer if there is less than 10 lines

# solution 2
tail -n+10 file.txt | head -1

# solution 3
sed -n '10p;11q' file.txt
