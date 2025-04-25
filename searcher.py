from deepsearcher.configuration import Configuration, init_config
from deepsearcher.online_query import query

config = Configuration()

# Customize your config here
config.set_provider_config("llm", "Ollama", {"model": "gemma3:27b", "url": "http://27.66.108.30:7860"})
init_config(config = config)

# # Load your local data
# from deepsearcher.offline_loading import load_from_local_files
# load_from_local_files(paths_or_directory=your_local_path)

# (Optional) Load from web crawling (`FIRECRAWL_API_KEY` env variable required)
from deepsearcher.offline_loading import load_from_website
load_from_website(urls="https://twilightsaga.fandom.com/wiki/Twilight_Saga_Wiki")

# Query
result = query("Write a report about this page.") # Your question here