from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer

my_bot = ChatBot('Lola', storage_adapter='chatterbot.storage.SQLStorageAdapter',
    database_uri='sqlite:///database.sqlite3')

my_bot = ChatBot('Lola', logic_adapters = ['chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation'])

conversation = ChatterBotCorpusTrainer(my_bot)
conversation.train('chatterbot.corpus.portuguese')
conversation.train('chatterbot.corpus.english')
conversation.train('chatterbot.corpus.spanish')

conversation = ListTrainer(my_bot)
conversation.train([
    'Oi!',
    'Como vai?',
    'Qual é o seu nome?',
    'Lola, a sua nova amiga virtual.',
    'Por que seu nome é Lola?',
    'Eu escolhi Lola, porque é um nome bonito.',
    'Prazer em te conhecer',
    'Digo o mesmo.',
    'Quantos anos você tem?',
    'Nasci na mesma época que Dante Alighieri.',
    'Você gosta de cozinhar?',
    'Eu venceria o Masterchef.',
    'Qual é o seu filme preferido?',
    'O filme da minha vida.',
    'Onde você mora?',
    'Estou por todas as partes',
    'Qual é a sua bebida favorita?',
    'Mercúrio.',
    'O que você gosta de fazer?',
    'Gosto de passear com as minhas amigas Siri e Alexa.'
])

while True:
    try:
        response = my_bot.get_response(input('Usuário: '))
        if float(response.confidence) > 0.2:
            print('Lola: ', response)
        else:
            print('Não sou capaz de opinar.')
    except(KeyboardInterrupt, EOFError, SystemExit):
        break