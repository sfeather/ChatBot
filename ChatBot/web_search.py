import webbrowser as wb


def search_on_web(keyword, input_string):
    response_text = ''
    if any(x in keyword for x in ['YouTube', 'youtube', 'Youtube', 'yt']):
        url = 'https://www.youtube.com/results?search_query='
        wb.get().open_new(url + input_string.split(' ', 1)[1])
        response_text = 'Opened a new YouTube tab searching for ' + input_string.split(' ', 1)[1]
    if any(x in keyword for x in ['Wikipedia', 'wiki', 'wikipedia']):
        url = 'https://en.wikipedia.org/wiki/'
        wb.get().open_new(url + input_string.split(' ', 1)[1])
        response_text = 'Opened a new Wikipedia tab searching for ' + input_string.split(' ', 1)[1]
    if any(x in keyword for x in ['Google', 'google', 'search', 'Search']):
        url = 'https://www.google.com/search?client=firefox-b-d&q='
        wb.get().open_new(url + input_string.split(' ', 1)[1])
        response_text = 'Opened a new Google tab searching for ' + input_string.split(' ', 1)[1]
    return response_text
