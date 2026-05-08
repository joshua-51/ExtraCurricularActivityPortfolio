import trexTalkForChatBot
import GeminiTapping
import fileName

NAME = trexTalkForChatBot.determiningName()
trexTalkForChatBot.printingDinoStuff(NAME)
TOPIC = trexTalkForChatBot.gettingGeminiTopic()
FILENAME = fileName.gettingFileName()
GeminiTapping.GeminiPromptSynthesis(TOPIC, FILENAME)

