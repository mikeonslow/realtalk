from langchain.utilities import SerpAPIWrapper


def get_audio_url(name: str):
    """Searches for audio files of the given name and returns the first result."""
    search = SerpAPIWrapper()
    res = search.run(f"{name}")
    return res
