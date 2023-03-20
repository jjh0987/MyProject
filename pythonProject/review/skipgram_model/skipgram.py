import numpy as np

# def P_WO_WI(word_vector,vector_wo,vector_wi):
#     np.exp(np.array(vector_wo)*np.array(vector_wi))/np.exp(np.array(word_vector)*np.array(vector_wi))


text = 'the quick brown fox jumps the red dog'
token = text.split()
token = {token[i]:0 for i in range(len(token))}

def skip_gram(text,window_size):
    text = text.split()
    answer = dict()
    for t in range(len(text)):
        for i in range(t-window_size,t+window_size+1):
            if i == t:
                continue
            if i < 0 or i > len(text)-1:
                continue
            answer[text[t]] = text[i]
    return answer

vector_target = skip_gram(text,2)
vector_target




zero = vector = np.zeros((1,len(token)))

token


hidden_layer = np.random.random((len(token),len(token))) # H X H
hidden_layer
