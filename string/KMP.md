## Knuth–Morris–Pratt algorithm  


### Partial Match Table
The length of the longest proper prefix in the (sub)pattern that matches a proper suffix in the same (sub)pattern.  

"abababca":

char:  | a | b | a | b | a | b | c | a |
-------|---|---|---|---|---|---|---|---|
index: | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 
value: | 0 | 0 | 1 | 2 | 3 | 4 | 0 | 1 |


- third cell: first three characters ("aba")  
    + prefixes ("a" and "ab")  
    + suffixes ("a" and "ba")  
    + the proper prefix "a" matches the proper suffix "a" --> value=1  

- cell 4: ("abab")  
    + prefixes ("a","ab","aba")  
    + suffixes ("b","ab","bab")  
    + matches = "ab" --> value=2  

- cell 5: ("ababa")  
    + prefixes ("a","ab","aba","abab")  
    + suffixes ("a","ba","aba","baba")  
    + matches = "aba" --> value=3  

- cell 7: ("abababc")  
    + there aren’t going to be any matches; all the suffixes will end with the letter “c”, and none of the prefixes will  


### Use Partial Match Table
We can use the values in the partial match table to skip ahead (rather than redoing unnecessary old comparisons) when we find partial matches.  
If a partial match of length ```partial_match_length``` is found and ```table[partial_match_length] > 1```, we may skip ahead ```partial_match_length - table[partial_match_length - 1]``` characters.  

example:  
matching the pattern "abababca" against the text "bacbababaabcbab"  

-------------------------------------------------------------------------------------  
  
| b | a | c | b | a | b | a | b | a | a | b | c | b | a | b |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   | l |   |   |   |   |   |   |   |   |   |   |   |   |   |
|   | a | b | a | b | a | b | c | a |   |   |   |   |   |   |
 
- partial_match_length=1   
- table[partial_match_length - 1]=table[0]=0  
- don't skip  

-------------------------------------------------------------------------------------  
    
| b | a | c | b | a | b | a | b | a | a | b | c | b | a | b |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   | l | l | l | l | l |   |   |   |   |   |   |
|   |   |   |   | a | b | a | b | a | b | c | a |   |   |   |
    
- partial_match_length=5  
- table[partial_match_length - 1]=table[4]=3  
- skip=partial_match_length-table[4]=5-3=1  

-------------------------------------------------------------------------------------
      
| b | a | c | b | a | b | a | b | a | a | b | c | b | a | b |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   | x | x | l | l | l |   |   |   |   |   |   |
|   |   |   |   |   |   | a | b | a | b | a | b | c | a |   |
      
- partial_match_length=3  
- table[partial_match_length - 1]=table[2]=1  
- skip=partial_match_length-table[2]=3-1=2  

-------------------------------------------------------------------------------------  
bacbababaabcbab  
      xx|  
        abababca  
        
| b | a | c | b | a | b | a | b | a | a | b | c | b | a | b |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | x | x | l |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | a | b | a | b | a | b | c | a |
        
- pattern is longer than the remaining characters in the text, so we know there’s no match.        