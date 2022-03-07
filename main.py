"""
Given a String as input, reverse the string. Use recursion. Do not use loops.
Input-> "Hello@#"
Output-> #@olleH
"""

def recur(st):
  ln = len(st)
  if ln == 0:
    return ""
  ch = st[-1]
  if (ch==ch):
    return ch + recur(st[1:])

st = "Hello@#"
print(recur(st))
  