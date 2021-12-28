qsn1):-
problem statement:------
Given an input string, you have to encrypt the string in such a manner that ‘a’ becomes ‘z’, ‘z’ becomes ‘a’ and accordingly.

 

Input format:-
The input is a lower case string

 

Output format:-
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



2)
qsn2:-
Question 2.
Given an input integer T. For each T,  you have to accept an integer and calculate the area of the area of the circle using that integer as the radius.

Area of Circle = πr²

 

Input
T determining the number of testcases. For each testcase, radius of the circle.

NOTE – The radius should be in range 20-30.

 

Output
Area of circle with the radius passed as input for every testcase nearest to decimal place. If the radius is out of range, print “Radius not in range”

 

Example
Input:
3
22
10
25

Output:
1520.53
Radius not in range
25
1963.49 

python solution:-
 
 
n = int(input())
for x in range(n):
   radius = int(input())
   if ((radius >= 20) and (radius <= 30)):
      area = 3.14159 * radius * radius
      print(area)
   else:
      print(“Radius not in range”)
     
