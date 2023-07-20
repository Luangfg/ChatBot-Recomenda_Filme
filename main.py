import requests
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

api_key ='f9ddfb66c027ffdbed6901de43616835'
analiza = SentimentIntensityAnalyzer()

def sugestao_filmes():
    frase = input("Como você está se sentindo hoje?")
    emocao = analiza.polarity_scores(frase)['compound']
    
    print(emocao)
    if emocao <= -0.5:
        genero = "18" #GENERO DRAMA
    elif emocao < 0:
        genero = "35" #GENERO COMEDIA
    elif emocao < 0.5:
        genero = "10749" #GERENO ROMANCE
    else:
        genero = "27" #GENERO HORROR
        
    url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&sort_by=popularity.desc&with_genres={genero}&vote_count.gte=4"
    response = requests.get(url).json()
    
    if response['results']:
        titles =[result['title'] for result in response['results'][:3]]
        print("Recomendo os seguintes filmes para você: ")
        for title in titles:
            print(f"- {title}")
    else:
        print("Não encontrei nenhuma sugestão de filme para você.")
    
def chatbot():
    print("Olá, Sou um Chat de sugestão de filmes. Como posso te ajudar hoje?")
    
    while True:
        try:
            response = input().lower()
            if 'filme' in response:
                sugestao_filmes()
            elif 'tchau' in response or 'adeus' in response:
                print("Adeus! Te na vejo na proxima vez!")
                break
            else:
                print("Desulpe, não entendi oque você quis dizer.")
                
        except KeyboardInterrupt:
            break

chatbot()