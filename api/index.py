

def tikly():
    try:
        BASE_URL = "https://api.tiklydown.eu.org"
        r = requests.get(BASE_URL + f"/api/download?url={url}", timeout=8)
        return r.json()
    except BaseException:
        raise Exception("No results found!")
