
import re

Regex_Pattern = r"\d\d\D\d\d\D\d\d\d\d"
print(str(bool(re.search(Regex_Pattern, input()))).lower())


#****************SAMPLE_INPUT************

# 06-11-2015

#***************OUTPUT**************

# true
