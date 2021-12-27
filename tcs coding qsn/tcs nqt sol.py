problem statement:------
Given an input string, you have to encrypt the string in such a manner that ‘a’ becomes ‘z’, ‘z’ becomes ‘a’ and accordingly.

 

Input format
The input is a lower case string

 

Output format
Encrypted lower case string

 

Example
Input:
programmings

Output:
kiltiznnrmt
slo:=
s=input("input the string->")
res=" "
for i in range(len(s)):
    res+=chr(ord('a')-ord(s[i])+ord('z'))



print(res)
