import spacy
import pdfplumber
import pandas as pd

def tokenization_spacy(pdf):
    nlp = spacy.load('en_core_web_sm')
    temp_token = [[j.text for j in nlp(page.extract_text()).sents] for page in pdf.pages]
    
    return temp_token

def promise10(num_of_candidate):
    candidate_text = []
    candidate = []
    policy = ['공약순위 1', '공약순위 2', '공약순위 3', '공약순위 4', '공약순위 5',
              '공약순위 6', '공약순위 7', '공약순위 8', '공약순위 9', '공약순위 10']
    for number in range(1, num_of_candidate+1):
        path = f'/Users/junho/Desktop/pycharmProjects/pythonProject/dacon/visualization/data/open/기호_{number} 공약.pdf'
        pdf = pdfplumber.open(path)
        temp_1list = sum(tokenization_spacy(pdf),[])
        temp_text = ''.join(temp_1list)
        text_space = []
        
        if number != 12 and number != 14:
            for num in range(1,11):
                premise_text = temp_text[temp_text.find(f'공약순위 {num}')+9 :temp_text.find('\n목', temp_text.find(f'공약순위 {num}'))]
                if '\n' in premise_text:
                    premise_text = ''.join(premise_text.splitlines())
                    
                if f'기호 {number}' in premise_text:
                    premise_text = premise_text[:premise_text.find(f'기호 {number}')]
                text_space.append(premise_text)
                
            candidate_text.append(text_space)
        else:
            for num in range(1,11):
                premise_text = temp_text[temp_text.find(f'공약순위 {num}')+9 :temp_text.find('\n', temp_text.find(f'공약순위 {num}'))]
                if '\n' in premise_text:
                    premise_text = ''.join(premise_text.splitlines())
                text_space.append(premise_text)
            candidate_text.append(text_space)
        candidate.append(f'기호_{number}')
        
    premise10 = pd.DataFrame(candidate_text, index = candidate, columns = policy)
    
    return premise10

a = promise10(14)
print(a)
