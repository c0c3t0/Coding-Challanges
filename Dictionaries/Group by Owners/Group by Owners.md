## Group by Owners

Implement a group_by_owners function that:
- Accepts a dictionary containing the file owner name for each file name.
- Returns a dictionary containing a list of file names for each owner name, in any order.

For example:
<pre><code>{'Input.txt': 'Randy', 'Code.py': 'Stan', 'Output.txt': 'Randy'} the function should return
{'Randy': ['Input.txt', 'Output.txt'], 'Stan': ['Code.py']}</code></pre>