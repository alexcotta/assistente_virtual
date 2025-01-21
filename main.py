import speech_recognition as sr#Biblioteca responsavel por ouvir e reconhecer a fala
import webbrowser
import wikipedia
from gtts import gTTS
from IPython.display import Audio

def get_audio(msg):
    #Habilita o microfone
    Microphone = sr.Recognizer()
    with sr.Microphone() as source:
        #Funcao de reducao de ruido
        Microphone.adjust_for_ambient_noise(source)
        print(msg)
        #Armazena o audio na variavel
        audio = Microphone.listen(source)
        try:
            #Passa o audio para o reconhecedor de padroes do speech_recognitio
            frase = Microphone.recognize_google(audio)
            print("Você disse: " + frase)#Caso nao tenha reconhecido o padrao de fala, exibe esta mensagem
        except sr.UnkownValueError:
            print("Não entendi")
            
    return frase

def text_to_speech(text, language, file_name=None):
    tts = gTTS(text=text, lang=language, slow=False)

    if file_name != None:
        filename = file_name+".mp3"
    else:
        filename = "response.mp3"
    tts.save(filename)
    # Use IPython para reproduzir o áudio no Colab e no terminal
    return Audio(filename, autoplay=True)

def speech_to_text(msg):
    return get_audio(msg)

def search_in_wikipedia(query):
    try:
        result = wikipedia.summary(query, sentences=2)
        print(f"Wikipedia says: {result}")
        text_to_speech(result, "pt-br", "resposta_pesquisa")
    except wikipedia.exceptions.DisambiguationError as e:
        print("Multiple results found, please specify.")
        text_to_speech("Multiple results found, please specify.", "pt-br")
    except Exception as e:
        print("Error accessing Wikipedia.")
        text_to_speech("Error accessing Wikipedia.", "pt-br")

def open_youtube():
    webbrowser.open("https://www.youtube.com")
    text_to_speech("Opening YouTube.","pt-br")
    
def assistant():
    text_to_speech("Olá o que posso fazer por você hoje?", "pt-br","saudacao")
    while True:
        msg = "Diga algo."
        command = speech_to_text(msg)
        print(command)
        if "Wikipedia" in command:
            text_to_speech("O que você quer procurar no wikipedia hoje?","pt-br","dialogo")
            query = speech_to_text("Pergunte algo.")
            if query:
                search_in_wikipedia(query)
        elif "YouTube" in command:
            open_youtube()
        elif "sair" in command or "bye" in command:
            text_to_speech("Goodbye! Have a great day!", "pt-br")
            break
        else:
            text_to_speech("Desculpe, não compreendi.", "pt-br")

assistant()
