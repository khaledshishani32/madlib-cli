


import re 

def read_template(filepath: str)->str:
    with open(filepath,'r') as file:
        text = file.read()
    return text.strip()


def parse_template(text):
    new_list = re.findall(r'\{(.*?)\}',text)
    for item in new_list:
        text = text.replace(item,'',1)
        
    return text,tuple(new_list)
    
def merge():
     pass