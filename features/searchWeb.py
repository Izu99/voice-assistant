import webbrowser

def search_youtube(command):
    search_url = "https://www.youtube.com/results?search_query="
    query_string = "+".join(command.split())
    url = search_url + query_string
    webbrowser.open(url)
    return "searching" + command + " on youtube" 

