from quart import Quart
from quart import jsonify
import random
from quotes import getQuoteList
from jokes import getJokeList
from words import getWordList

quotes = getQuoteList()
words = getWordList()
jokes = getJokeList()

app = Quart(__name__)


@app.route("/")
async def hello():
    return "Try /random/quote, /random/word and /random/joke"



@app.route("/random/quote", methods=["GET"])
async def randomQuote():
    index = random.randrange(0,1641) #1642 quotes total

    return jsonify({
        "text": quotes[index]["text"],
        "author": quotes[index]["author"]
        })


@app.route("/random/joke", methods=["GET"])
async def randomJoke():
    index = random.randrange(0,376) #377 jokes total

    return jsonify({
        "type": jokes[index]["type"],
        "setup": jokes[index]["setup"],
        "punchline": jokes[index]["punchline"]
        })

@app.route("/random/word", methods=["GET"])
async def randomWord():

    index = random.randrange(0,1951) #1952 words total 

    return jsonify({
        "word": words[index],
        "length": len(words[index]),
        "firstLetter": words[index][0]
        })

@app.route("/random/word/10", methods=["GET"])
async def randomWordTen():
    return jsonify({
        "words": [
            words[random.randrange(0,1951)],
            words[random.randrange(0,1951)],
            words[random.randrange(0,1951)],
            words[random.randrange(0,1951)],
            words[random.randrange(0,1951)],
            words[random.randrange(0,1951)],
            words[random.randrange(0,1951)],
            words[random.randrange(0,1951)],
            words[random.randrange(0,1951)],
            words[random.randrange(0,1951)]
        ]

        })


# if __name__ == "__main__":    
#     app.run()
# removed this debug only code not meant for production