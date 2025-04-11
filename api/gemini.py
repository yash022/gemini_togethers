from flask import Flask 
import google.generativeai as genai
import os
import logging

logging.warning("togethers api key: %s", os.environ.get("gemini_api"))

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

@app.route('/reply/<string:query>')
def replygemini(query):
  response = chat_session.send_message(query)
  return str(response.text)


if __name__ == "__main__":
    app.run()

