import re

str='The advancements in biomarine studies franky@google.com, with the investments necessary and Davos sinatra123@yahoo.com Then The New Yorker article on wind farms...'
#Type your answer here.

regex= r'[\w\.-]+@'
emails=re.findall(regex, str, flags=re.MULTILINE)


print(emails)
