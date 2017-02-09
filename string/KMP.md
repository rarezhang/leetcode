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
    """
    O(K): K=length(s) 
    """
    length = len(s)
    partial_match_table = [0]*length
    s = list(s)
    i,j=0,1
    while i<length and j<length:
        if s[i]==s[j]:  # case 1: the substring continues  
            partial_match_table[j]=i+1
            i+=1
            j+=1
        else:  # case 2: the substring doesn't continues, but can fall back
            if i==0:
                partial_match_table[j]=0
                j+=1
            else:  # case 3: run out of candates
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

```
def kmp_search(P, S, kmp_table):
    """
    O(n)
    P: the pattern(word) sought
    S: the text to be searched
    return: an integer (the zero-based position in S at which P is found)

    """
    m = 0  # the beginning of the current match in S
    i = 0  # the position of the current character in P
    
    while m + i < len(S):
        if P[i] == S[m+i]:
            if i == len(P) - 1:
                return m
            i += 1
        else:
            if kmp_table[i] > -1:
                m = m + i - kmp_table[i]
                i = kmp_table[i]
            else:
                m += 1
                i = 0
    return None  # have searche all of S unsuccessfully
    
s="ababab"
print(kmp_search('aba', s, kmp_table(s)))
# 0 
```      
[code visualization](http://pythontutor.com/composingprograms.html#code=def%20kmp_table%28s%29%3A%20%20%20%0A%20%20%20%20length%20%3D%20len%28s%29%0A%20%20%20%20partial_match_table%20%3D%20%5B0%5D*length%0A%20%20%20%20s%20%3D%20list%28s%29%0A%20%20%20%20i,j%3D0,1%0A%20%20%20%20while%20i%3Clength%20and%20j%3Clength%3A%0A%20%20%20%20%20%20%20%20if%20s%5Bi%5D%3D%3Ds%5Bj%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20partial_match_table%5Bj%5D%3Di%2B1%0A%20%20%20%20%20%20%20%20%20%20%20%20i%2B%3D1%0A%20%20%20%20%20%20%20%20%20%20%20%20j%2B%3D1%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20i%3D%3D0%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20partial_match_table%5Bj%5D%3D0%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20j%2B%3D1%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20i%20%3D%20partial_match_table%5Bi-1%5D%0A%20%20%20%20return%20partial_match_table%0A%0Adef%20kmp_search%28P,%20S,%20kmp_table%29%3A%0A%20%20%20%20%22%22%22%0A%20%20%20%20O%28n%29%0A%20%20%20%20P%3A%20the%20pattern%28word%29%20sought%0A%20%20%20%20S%3A%20the%20text%20to%20be%20searched%0A%20%20%20%20return%3A%20an%20integer%20%28the%20zero-based%20position%20in%20S%20at%20which%20P%20is%20found%29%0A%0A%20%20%20%20%22%22%22%0A%20%20%20%20m%20%3D%200%20%20%23%20the%20beginning%20of%20the%20current%20match%20in%20S%0A%20%20%20%20i%20%3D%200%20%20%23%20the%20position%20of%20the%20current%20character%20in%20P%0A%20%20%20%20%0A%20%20%20%20while%20m%20%2B%20i%20%3C%20len%28S%29%3A%0A%20%20%20%20%20%20%20%20if%20P%5Bi%5D%20%3D%3D%20S%5Bm%2Bi%5D%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20i%20%3D%3D%20len%28P%29%20-%201%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20return%20m%0A%20%20%20%20%20%20%20%20%20%20%20%20i%20%2B%3D%201%0A%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20if%20kmp_table%5Bi%5D%20%3E%20-1%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20m%20%3D%20m%20%2B%20i%20-%20kmp_table%5Bi%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20i%20%3D%20kmp_table%5Bi%5D%0A%20%20%20%20%20%20%20%20%20%20%20%20else%3A%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20m%20%2B%3D%201%0A%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20i%20%3D%200%0A%20%20%20%20return%20None%20%20%23%20have%20searche%20all%20of%20S%20unsuccessfully%0A%20%20%20%20%0As%3D%22ababab%22%0Aprint%28kmp_search%28'aba',%20s,%20kmp_table%28s%29%29%29&cumulative=true&curInstr=0&mode=display&origin=composingprograms.js&py=3&rawInputLstJSON=%5B%5D)