from flask import Flask 
import google.generativeai as genai
from together import Together

import os
import logging

logging.warning("gemini api key: %s", os.environ.get("gemini_api"))
logging.warning("togethers api key: %s", os.environ.get("togethers_api"))


client = Together(api_key=os.environ['togethers_api'])

genai.configure(api_key=os.environ['gemini_api'])

generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 40,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-pro",
  generation_config=generation_config,
)

chat_session = model.start_chat(
  history=[
  ]
)

app = Flask(__name__) 
@app.route('/') 
def hello_world(): 
    return 'Hello, World!' 

@app.route('/replygemini/<string:query>')
def replygemini(query):
  response = chat_session.send_message(query)
  return str(response.text)

@app.route('/replytogethers/<string:query>')
def replytogethers(query):
  response = client.chat.completions.create(
    model="meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8",
    messages=[{"role": "user", "content": query}]
    )
  return str(response.choices[0].message.content)
    

if __name__ == "__main__":
    app.run(debug=True)

