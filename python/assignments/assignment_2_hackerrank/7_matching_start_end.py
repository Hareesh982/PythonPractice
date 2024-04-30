
import re

from sqlalchemy import true

Regex_Pattern = r"^\d\w{4}\.$"  # Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())


#*****************SAMPLE_INPUT*************

# 0qwer.

#***************OUTPUT************

# true
