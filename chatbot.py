from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import Trainer


def get_response(usrText):
    bot = ChatBot('Bot',
                  storage_adapter='chatterbot.storage.SQLStorageAdapter',
    logic_adapters=[
        {
            'import_path': 'chatterbot.logic.BestMatch'
        },
        {
            'import_path': 'chatterbot.logic.LowConfidenceAdapter',
            'threshold': 0.60,
            'default_response': 'I am sorry, I did not Recognized this.'
        }
    ],
    trainer='chatterbot.trainers.ListTrainer')
    bot.set_trainer(ListTrainer)
    while True:
        if usrText.strip() !='Bye':
            result =bot.get_response(usrText)
            reply= str(result)
            return (reply)
        elif usrText.strip()=='Bye':
            return('Bye!')
        elif usrText.strip()=='bye':
            return('Bye!')



"""
class ChatterBotCorpusTrainer(Trainer):
    #Allows the chat bot to be trained using data from the ChatterBot dialog corpus.
   
    def __init__(self, storage, **kwargs):
        super(ChatterBotCorpusTrainer, self).__init__(storage, **kwargs)
        from .corpus import Corpus

        self.corpus = Corpus()

    def train(self, *corpora):
        trainer = ListTrainer(self.storage)

        # Allow a list of corpora to be passed instead of arguments  
        if len(corpora) == 1:
            if isinstance(corpora[0], list):
                corpora = corpora[0]

        # Train the chat bot with each statement and response pair
        for corpus in corpora:
            corpus_data = self.corpus.load_corpus(corpus)
            for data in corpus_data:
                for pair in data:
                    trainer.train(pair)

"""