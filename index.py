from asyncio.exceptions import IncompleteReadError
from quart import Quart
from quart import jsonify
app = Quart(__name__)

import random
from quotes import getQuoteList

@app.route("/")
async def hello():
    return "<h1 style='color:blue'>Hello World!</h1>"

@app.route("/random/quote", methods=["GET"])
async def randomQuote():
    index = random.randrange(0,1641) #1642 quotes total

    return jsonify({
        "text": quotes[index]["text"],
        "author": quotes[index]["author"]
        })

if __name__ == "__main__":    
    quotes = getQuoteList()
    app.run()