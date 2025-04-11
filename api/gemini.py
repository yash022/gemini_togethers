from flask import Flask 
from together import Together

import os
import logging

logging.warning("togethers api key: %s", os.environ.get("togethers_api"))


client = Together(api_key=os.environ['togethers_api'])


app = Flask(__name__) 
@app.route('/') 
def hello_world(): 
    return 'Hello, World!' 

@app.route('/reply/<string:query>')
def reply(query):
  response = client.chat.completions.create(
    model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
    messages=[{"role": "user", "content": query}]
    )
  return str(response.choices[0].message.content)
    

if __name__ == "__main__":
    app.run()

