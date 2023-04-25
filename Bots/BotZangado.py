from Bots.Bot import Bot

class BotZangado(Bot):
    def __init__(self,nome):
        super().__init__(nome)
        self._comandos['1'] = "Por que vocẽ é bravo assim ?"
        self._comandos['2'] = "O que você gosta de fazer?"
        self._comandos['3'] = "Não fale assim comigo!"

    def apresentacao(self):
        return f"Mau dia!, eu sou {self.nome} quem ousa me incomdodar!?"
  
    def executa_comando(self, cmd):
        if cmd == '1':
            return "Como assim bravo?! Eu estou completamente calmo!"
        elif cmd == '2':
            return "Eu não gosto de falar com você!"
        elif cmd == '3':
            return  "Eu falo do jeito que eu quiser!"
        else:
            return None
        
    def boas_vindas(self):
        return "Diga logo o que você quer!"

    def despedida(self):
        return "Até que enfim vou embora!"
