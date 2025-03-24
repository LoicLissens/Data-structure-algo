import re

def lottery(s:str) -> str:
    match =  re.findall('\d', s)
    return ''.join(dict.fromkeys(match)) if match else 'One more run!'

# Without Regexp
def lottery(s):
    return "".join(dict.fromkeys(filter(str.isdigit, s))) or "One more run!"