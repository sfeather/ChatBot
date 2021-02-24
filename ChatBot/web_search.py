import webbrowser as wb
import covid_scrap as cs


def search_on_web(keyword, input_string):
    response_text = ''

    if any(x in keyword.lower() for x in ['youtube', 'yt']):
        if len(input_string.split(' ', 1)) != 1:
            url = 'https://www.youtube.com/results?search_query='
            wb.get().open_new(url + input_string.split(' ', 1)[1])
            response_text = 'Opened a new YouTube tab searching for ' + input_string.split(' ', 1)[1]
        else:
            response_text = 'ChatBot: You are using a wrong command syntax\n' \
                            'The command syntax should be: command + keyword'
    if any(x in keyword.lower() for x in ['wiki', 'wikipedia']):
        if len(input_string.split(' ', 1)) != 1:
            url = 'https://en.wikipedia.org/wiki/'
            wb.get().open_new(url + input_string.split(' ', 1)[1])
            response_text = 'Opened a new Wikipedia tab searching for ' + input_string.split(' ', 1)[1]
        else:
            response_text = 'ChatBot: You are using a wrong command syntax\n' \
                            'The command syntax should be: command + keyword'
    if any(x in keyword.lower() for x in ['google', 'search', 'find']):
        if len(input_string.split(' ', 1)) != 1:
            url = 'https://www.google.com/search?client=firefox-b-d&q='
            wb.get().open_new(url + input_string.split(' ', 1)[1])
            response_text = 'Opened a new Google tab searching for ' + input_string.split(' ', 1)[1]
        else:
            response_text = 'ChatBot: You are using a wrong command syntax\n' \
                            'The command syntax should be: command + keyword'
    if any(x in keyword.lower() for x in ['covid', 'covid-19', 'coronavirus', 'corona']):
        if len(input_string.split(' ', 1)) != 1:
            string = cs.scrap(input_string.split(' ', 1)[1])
            response_text = 'Covid-19 fresh news (24h) - ' + string.split('[', 1)[0]
        else:
            response_text = 'ChatBot: You are using a wrong command syntax\n' \
                            'The command syntax should be: command + keyword'

    return response_text
