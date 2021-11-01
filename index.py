from quart import Quart
from quart import jsonify
import random
from quotes import getQuoteList

quotes = getQuoteList()
app = Quart(__name__)


@app.route("/")
async def hello():
    return jsonify({
        "randomQuotesEndpoint": "https://api.alexx.lol/random/quote"
        })



@app.route("/random/quote", methods=["GET"])
async def randomQuote():
    index = random.randrange(0,1641) #1642 quotes total

    return jsonify({
        "text": quotes[index]["text"],
        "author": quotes[index]["author"]
        })

# if __name__ == "__main__":    
#     app.run()
# removed this debug only code not meant for production