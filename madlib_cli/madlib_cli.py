


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
    
def question(questions):
    user_answers=[]
    for index in questions:
        result=input(f"can i ask you to know about me {index} ?")
        user_answers.append(result)
    return user_answers    


def merge(answer,user_answers):
    print(answer)
    fresh_txt=answer.format(*user_answers)
    print(fresh_txt)
    return fresh_txt


if __name__ == "__main__":
    pass