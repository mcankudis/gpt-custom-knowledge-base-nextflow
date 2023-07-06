from llama_hub.github_repo import GithubRepositoryReader
owner                   = "nextflow-io"
repo                    = "nextflow"
filter_directories      = (["docs"], GithubRepositoryReader.FilterType.INCLUDE)
filter_file_extensions  = ([".md"], GithubRepositoryReader.FilterType.INCLUDE)
concurrent_requests     = 10
branch                  = "master"

persist_dir             = "./nextflow-md-index"