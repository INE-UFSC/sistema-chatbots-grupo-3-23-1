from Bots.Bot import Bot
from Bots.comando import Comando

class BotZangado(Bot):
    def __init__(self,nome):
        super().__init__(nome)

        self._comandos =[
            Comando('1', 'Por que vocẽ é bravo assim ?', 'Como assim bravo?! Eu estou completamente calmo!' ),
            Comando('2', 'O que você gosta de fazer?', 'Essa é fácil: Há uma série de coisas que gosto de fazer. Entretanto, falar com você com certeza não e uma delas!'),
            Comando('3', 'Não fale assim comigo!', ' Minha resposta para você é: Eu falo do jeito que eu quiser!')
        ]

    def apresentacao(self):
        return f"Mau dia!, eu sou {self.nome} quem ousa me incomdodar!?"
        
    def boas_vindas(self):
        return "-- Diga logo o que você quer!"

    def despedida(self):
        return "-- Até que enfim vou embora!"
