truncate
========
> truncate string in python

##Code
```Python
import sys

def truncate(str, limit, ellipsis='...'): 
    return str[:limit] + ellipsis if len(str) > limit else str 

sys.modules[__name__] = truncate
```

##Install
```Bash
$ pip install trunkate
```

##Usage
```Bash
import truncate

truncate('Hello world!', 4)
# Hell...

truncate('Hello world!', 100)
# Hello world!
```
