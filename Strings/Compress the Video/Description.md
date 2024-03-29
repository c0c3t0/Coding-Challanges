## Problem
Chef recorded a video explaining his favorite recipe. However, the size of the video is too large to upload on the internet. He wants to compress the video so that it has the minimum size possible.

Chef's video has N frames initially. The value of the i<sup>th</sup> frame is A<sub>i</sub>. Chef can do the following type of operation any number of times:
- Choose an index i(1≤i≤N) such that the value of the i<sup>th</sup> frame is equal to the value of either of its neighbors and remove the i<sup>th</sup> frame.
Find the minimum number of frames Chef can achieve.

### Input Format
- First line will contain T, the number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer N - the number of frames initially.
 - The second line contains N space-separated integers, A<sub>1</sub>, A<sub>2</sub>,…,A<sub>N</sub> - the values of the frames.

### Output Format
For each test case, output in a single line the minimum number of frames Chef can achieve.

### Sample 1:
<pre><code>Input:
4
1
5
2
1 1
3
1 2 3
4
2 1 2 2
</code></pre>
<pre><code>
Output:
1
1
3
3
</code></pre>
