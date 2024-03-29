## Problem
Given a positive integer N, MoEngage wants you to determine if it is possible to rearrange the digits of N (in decimal representation) and obtain a multiple of 5.

For example, when N=108, we can rearrange its digits to construct 180=36⋅5 which is a multiple of 5.

### Input Format
- The first line contains an integer T, the number of test cases. The description of the T test cases follow.
- Each test case consists of two lines
- The first line contains a single integer D, the number of digits in N.
- The second line consists of a string of length D, the number N (in decimal representation). It is guaranteed that the string does not contain leading zeroes and consists only of the characters 
0, 1,…9.

### Output Format
For each test case, print Yes if it is possible to rearrange the digits of N so that it becomes a multiple 5. Otherwise, print No.

You may print each character of the string in uppercase or lowercase.

### Sample 1:
<pre><code>Input:
3
3
115
3
103
3
119
</code></pre>
<pre><code>
Output:
Yes
Yes
No
</code></pre>
