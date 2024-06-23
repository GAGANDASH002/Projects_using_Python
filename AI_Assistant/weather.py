
# https://www.google.com/search?q=waether+bhubaneswar
# User Agent : Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36
# span id = wob_tm

def weather():
    from requests_html import HTMLSession
    import speech_to_text

    s = HTMLSession()
    url = f'https://www.accuweather.com/en/in/bhubaneswar/189781/current-weather/189781'
    r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36'})
    temp = r.html.find('div.display-temp',first=True).text
    desc = r.html.find('div.phrase',first=True).text

