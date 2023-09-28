import random
import json
from nltk_utils import bag_of_words, tokenize
import pickle

with open('files/intents.json', 'r', encoding='utf-8') as f:
    intents = json.load(f)

model = pickle.load(open('model/model.pkl', 'rb'))
loaded_vec = pickle.load(open('model/count_vec.pkl', 'rb'))

bot_name = 'Refriartec bot'

def get_response(query):
    print(query)
    tag = model.predict(loaded_vec.transform([query]))
    print(tag[0])

    for intent in intents['intents']:
        if tag[0] == intent['tag']:
            answer = random.choice(intent["responses"])
            print(f'{bot_name}: {answer}')
            return answer
    return 'Não entendi...'
    
if __name__ == "__main__":
    print('Como posso ajudar? Caso queira sair digite "Sair"')
    while True:
        sentence = input('Você: ')
        if sentence == 'Sair':
            break

        resp = get_response(sentence)
        print(resp)

   

   
    

    

   
        