import os

import openai
from dotenv import load_dotenv
from llama_index import StorageContext, load_index_from_storage

from config import persist_dir

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

def chat(input_text):
    storage_context = StorageContext.from_defaults(persist_dir = persist_dir)
    index = load_index_from_storage(storage_context)

    query_engine = index.as_chat_engine()
    response = query_engine.chat(input_text)
    return response.response

def main ():
    print("Welcome to the Nextflow chatbot!")
    print("Type 'exit', 'bye', 'quit', or 'goodbye' to exit.")

    while True:
        question = input("\nInput a question:")
        if  ["exit", "bye", "quit", "goodbye"].__contains__(question):
            print("Goodbye!")
            break
        print("")
        print(chat(question))

main()