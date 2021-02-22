import webbrowser as wb
import covid_scrap as cs


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
    if any(x in keyword for x in ['covid', 'Covid', 'covid-19', 'Covid-19', 'coronavirus', 'corona', 'Coronavirus',
                                  'Corona', 'CoronaVirus']):
        string = cs.scrap(input_string.split(' ', 1)[1])
        response_text = 'Covid-19 fresh news (24h) - ' + string.split('[', 1)[0]

    return response_text
