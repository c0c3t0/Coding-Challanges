## Problem
Chef has a string S with him. Chef is happy if the string contains a contiguous substring of length strictly greater than 2 in which all its characters are vowels.

Determine whether Chef is happy or not.

Note that, in english alphabet, vowels are a, e, i, o, and u.

### Input Format
- First line will contain T, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, a string S.

### Output Format
For each test case, if Chef is happy, print HAPPY else print SAD.

You may print each character of the string in uppercase or lowercase (for example, the strings hAppY, Happy, haPpY, and HAPPY will all be treated as identical).

### Sample 1:
<pre><code>Input:
4
aeiou
abxy
aebcdefghij
abcdeeafg
</code></pre>
<pre><code>
Output:
Happy
Sad
Sad
Happy
</code></pre>
