
import re

Regex_Pattern = r'^[123][012][xs0][03Aa][xsu][\.\,]$'
print(str(bool(re.search(Regex_Pattern, input()))).lower())


#****************SAMPLE_INPUT****************

# 1203x.

#*************OUTPUT*************

# true
