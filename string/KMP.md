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

```
def kmp_table(s):   
    length = len(s)
    partial_match_table = [0]*length
    s = list(s)
    i,j=0,1
    while i<length and j<length:
        if s[i]==s[j]:
            partial_match_table[j]=i+1
            i+=1
            j+=1
        else:
            if i==0:
                partial_match_table[j]=0
                j+=1
            else:
                i = partial_match_table[i-1]
    return partial_match_table

s="ababab"
print(kmp_table(s))
# [0, 0, 1, 2, 3, 4]
```
[code visualization](http://pythontutor.com/composingprograms.html#code=def%20kmp_table%28s%29%3A%20%20%20%0A%20%20%20%20length%20%3D%20len%28s%29%0A%20%20%20%20partial_match_table%20%3D%20%5B0%5D*length%0A%20%20%20%20s%20%3D%20list%28s%29%0A%20%20%20%20i,j%3D0,1%0A%20%20%20%20while%20i%3Clength%20and%20j%3Clength%3A%0A%20%20%20%20%20%20%20%20if%20s%5Bi%5D%3D%3Ds%5Bj%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20partial_match_table%5Bj%5D%3Di%2B1%0A%20%20%20%20%20%20%20%20%20%20%20%20i%2B%3D1%0A%20%20%20%20%20%20%20%20%20%20%20%20j%2B%3D1%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20i%3D%3D0%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20partial_match_table%5Bj%5D%3D0%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20j%2B%3D1%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20i%20%3D%20partial_match_table%5Bi-1%5D%0A%20%20%20%20return%20partial_match_table%0A%0As%3D%22ababab%22%0Aprint%28kmp_table%28s%29%29&cumulative=true&curInstr=36&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D)  

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
        
| b | a | c | b | a | b | a | b | a | a | b | c | b | a | b |   |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|   |   |   |   |   |   | x | x | l |   |   |   |   |   |   |   |
|   |   |   |   |   |   |   |   | a | b | a | b | a | b | c | a |
        
- pattern is longer than the remaining characters in the text, so we know there’s no match.        