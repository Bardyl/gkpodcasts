import requests
import urllib
import urlparse

from lxml import html

USERNAME = ""
PASSWORD = ""

LOGIN_URL = "https://www.gamekult.com/utilisateur/connexion.html"
SHOWS_URL = "https://www.gamekult.com/emissions.html"

def main():
    session_requests = requests.session()

    # Create payload
    payload = {
        "_username": USERNAME, 
        "_password": PASSWORD, 
    }

    # Perform login
    result = session_requests.post(LOGIN_URL, data = payload, headers = dict(referer = LOGIN_URL))

    # Scrape url
    result = session_requests.get(SHOWS_URL, headers = dict(referer = SHOWS_URL))
    tree = html.fromstring(result.content)

    showTitle = tree.xpath("//div[@class='ed__show__list']/header/h2/text()")
    showLastItem = tree.xpath("//div[@class='ed__show__list']//h4[1]/a/text()")
    showLastItemUrl = tree.xpath("//div[@class='ed__show__list']//h4[1]/a/@href")

    showsLen = len(showTitle)

    shows = []
    i = 0
    while (i < showsLen):
        shows.append([showTitle[i], showLastItem[i], 'https://www.gamekult.com' + showLastItemUrl[i]])
        i+=1

    for show in shows:
        result = session_requests.get(show[2], headers = dict(referer = show[2]))
        tree = html.fromstring(result.content)
        iframeSrc = tree.xpath("//div[@class='pm__article__container']/iframe/@src")

        if len(iframeSrc) > 0:
            url = urllib.unquote(iframeSrc[0]).decode('utf8')
            params = urlparse.urlparse(url)
            soundCloudApiUrl = urlparse.parse_qs(params.query)['url'][0]

            url = soundCloudApiUrl.split('?')[0]

            # show title: show last episode title - show last episode url
            print show[0] + ': ' + show[1] + ' - ' + url

main()
