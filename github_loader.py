import os
from typing import Sequence

import openai
from dotenv import load_dotenv
from llama_hub.github_repo import GithubClient, GithubRepositoryReader
from llama_index import GPTVectorStoreIndex, download_loader
from llama_index.schema import Document

from config import (branch, concurrent_requests, filter_directories,
                    filter_file_extensions, owner, persist_dir, repo)

load_dotenv()
download_loader("GithubRepositoryReader")
openai.api_key = os.getenv("OPENAI_API_KEY")


def load_documents() -> Sequence[Document]:
    github_client = GithubClient(os.getenv("GITHUB_TOKEN"))
    
    loader = GithubRepositoryReader(
        github_client           = github_client,
        owner                   = owner,
        repo                    = repo,
        filter_directories      = filter_directories,
        filter_file_extensions  = filter_file_extensions,
        concurrent_requests     = concurrent_requests
    )
    
    return loader.load_data(branch = branch)


def index_documents(documents: Sequence[Document]):
    index = GPTVectorStoreIndex.from_documents(documents)
    index.storage_context.persist(persist_dir = persist_dir) 


def main():
    documents = load_documents()
    print(f"Loaded {len(documents)} documents")

    char_sum = 0
    for document in documents: char_sum += len(document.text)
    print(f"Approx. total number of tokens: {char_sum/4}")

    confirmation = input("Continue? (y/n)")
    if confirmation != "y": return

    index_documents(documents)

main()