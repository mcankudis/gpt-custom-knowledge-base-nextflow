# Custom knowledge base for Nextflow using ChatGPT
A project for my paper "Using AI as assistance in creating scientific workflows with Nextflow" for "Operating Complex IT Systems" seminar at the TU Berlin.

## Running the scripts

This project requires python3.9. It may work with 3.8, but it has not been tested.


Copy `.env.example` to `.env` and replace the values inside it:


|   |   |
| - | - |
| OPENAI_API_TOKEN | Your token for OpenAI's API, get it [here](https://platform.openai.com/account/api-keys) |
| GITHUB_TOKEN | GutHub Access Token (Classic) with read acces to your repositiories |



Make sure you have all the required dependencies installed. For that you, can f.e. use pip and pipenv:


Create the virtual environment
``` sh
pipenv --python 3.9
```

Install dependencies
``` sh
pipenv --sync
```

Run the chat
``` sh
python3.9 chat.py
```

If you want to build your own knowledge base, you can modify the data in `config.py` and index a GitHub repository of your choice by running:
```sh
python3.9 github_loader.py
```
