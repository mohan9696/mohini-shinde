import re
p='pune123mumbai 22 abab'
result=re.findall('[^abc]',p)
print(result)