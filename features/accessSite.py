import pywhatkit
import wikipediaapi
import webbrowser
import time


def play_youtube_video(song_name):
    try:
        pywhatkit.playonyt(song_name)
        return f"Playing {song_name} on YouTube..."
    except Exception as e:
        return f"Error playing {song_name} on YouTube: {str(e)}"

def play_youtube_audio(song_name):
    try:
        pywhatkit.playonyt(song_name)
        return f"Playing {song_name} audio on YouTube..."
    except Exception as e:
        return f"Error playing {song_name} audio on YouTube: {str(e)}"

def get_wikipedia_summary(topic):
    # Specify a user agent to comply with Wikipedia's User-Agent policy
    wiki_wiki = wikipediaapi.Wikipedia(language='en', user_agent="YourUserAgent/1.0")
    page = wiki_wiki.page(topic)
    if page.exists():
        summary = page.summary
        # Split the summary into sentences
        sentences = summary.split(". ")
        # Select the first three sentences
        summary = ". ".join(sentences[:3]) + "."
        return summary
    else:
        return f"Sorry, {topic} not found on Wikipedia."



def play_youtube_playlist(playlist_url):
    # Open the playlist URL
    webbrowser.open(playlist_url)
    time.sleep(5)  # Wait for the page to load (optional)
    return "Playing Your Favorite Playlist"
 
