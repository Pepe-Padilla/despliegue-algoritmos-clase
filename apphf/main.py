from fastapi import FastAPI
import os
import google.generativeai as genai
from dotenv import load_dotenv
from transformers import pipeline 

app = FastAPI()

@app.get('/saluda')
def saluda():
    return {'Message': 'Hola soy Raquel'}

@app.get('/despido')
def despido():
    return {'Message': 'Hola soy Raquel'}

@app.get('/generate')
def sentiment_classification(prompt: str):
    sentiment_pipeline = pipeline('sentiment-analysis')
    return {'Sentiment': sentiment_pipeline(prompt)[0]['label']}

@app.get('/generate2')
def summarization(prompt: str):
    summarization_pipeline = pipeline('summarization')
    return {'Summary': summarization_pipeline(prompt)[0]['summary_text']}







# @app.get("/gemini") 
# def gemini_flash(query: str): 
#   load_dotenv()
#   genai.configure(api_key=os.environ.get("GEMINI_API_KEY"))

#   # Create the model
#   generation_config = {
#     "temperature": 1,
#     "top_p": 0.95,
#     "top_k": 40,
#     "max_output_tokens": 2000
#   }

#   model = genai.GenerativeModel(
#     model_name="gemini-2.0-flash",
#     generation_config=generation_config,
#   )

#   chat_session = model.start_chat(
#     history=[
#     ]
#   )

#   response = chat_session.send_message(query)

#   print(response.text)
#   return response.text

