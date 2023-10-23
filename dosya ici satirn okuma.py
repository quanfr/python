import urllib.request
url = 'file:///C:/Users/Qompu/Desktop/Lessons/Lessons%20PDFs/Practical%20Programming%20An%20Introduction%20to%20Computer%20Science%20Using%20Python%203.6%20Paul%20Gries,%20Jennifer%20Campbell,%20Jason%20Montojo%20z-lib.org%201.pdf'
with urllib.request.urlopen(url) as webpage:
  for line in webpage:
    line = line.strip()
    line = line.decode('utf-8')
print(line)