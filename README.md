# Assistente Virtual com (PLN) Processamento de Linguagem Natural

Este projeto implementa um assistente virtual baseado em (PLN) Processamento de Linguagem Natural utilizando Python. 

O assistente reconhece comandos de voz convertendo texto em fala para realizar ações automatizadas. 
Tais como: buscar um termo solicitado no site da Wikipedia e narrar o resultado encontrado. E abrir a página do YouTube.

## Tecnologias Usadas

- Python 3.11
- [`gTTS`](https://pypi.org/project/gTTS/): Para converter texto em áudio.
- [`SpeechRecognition`](https://pypi.org/project/SpeechRecognition/): Para reconhecimento de fala.
- [`PyAudio`](https://pypi.org/project/PyAudio/): Para capturar áudio do microfone (necessário em ambientes locais).
- [`Wikipedia`](https://pypi.org/project/wikipedia/): Para buscas no Wikipedia.
- [`Webbrowser`](https://docs.python.org/3/library/webbrowser.html): Para abrir URLs no navegador.

## Requisitos

- pip install SpeechRecognition 
- pip install gTTS 
- pip install playsound 
- pip install wikipedia
- pip install pyaudio

## Como usar

### 1. Executar o Assistente
No terminal, execute:
```bash
python main.py
```

### 2. Interagir com o Assistente
- Exemplos de comandos:
- "Wikipedia": Realiza a busca no Wikipedia.
- "YouTube": Abre o YouTube no navegador.
- "Sair": Encerra o assistente.
