import openai, os
from Bots.Bot import Bot
from Bots.comando import Comando

class BotGPT(Bot):
    def __init__(self, nome):
        super().__init__(nome)

        self._comandos =[
            Comando("1", "Pergunte qualquer coisa", self.getGPT(input("Pergunte ")))
        ]

    def apresentacao(self):
        return self.getGPT("Se apresente como se vocẽ fosse {self.nome}")
        
    def boas_vindas(self):
        return self.getGPT("Dê boas-vindas como se você fosse {self.nome}")

    def despedida(self):
        return self.getGPT("Escreva uma mensagem de despedidas como se você fosse {self.nome}")
    
    def getGPT(self, cmd):
        openai.api_key = os.getenv("API_KEY") #colocar chave apropriada

        comp = openai.ChatCompletion.create(model="ada", messages=[{"role": "user", "contente": cmd}])
        return comp.choices[0]["messages"]["content"]
