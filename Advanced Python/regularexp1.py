import re

sen="hello its my number 999-3654-112"

sentecnce=re.compile(r'\d\d\d-\d\d\d\d-\d\d\d')
no=searchresult=sentecnce.search(sen)

print("match Found :"+no.group())
