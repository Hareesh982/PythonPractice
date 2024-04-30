
import re

from sqlalchemy import true

Regex_Pattern = r'^[a-z][1-9][^a-z][^A-Z][A-Z]'  # Do not delete 'r'.

print(str(bool(re.search(Regex_Pattern, input()))).lower())


#**************SAMPLE_INPUT**************

# h4CkR

#***************OUTPUT***************

# true
