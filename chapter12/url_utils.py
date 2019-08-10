import requests # to interact with the Web

def gen_from_urls(urls: tuple) -> tuple:
    for resp in (requests.get(url) for url in urls): # using a generator
        yield len(resp.content), resp.status_code, resp.url # returns the length of the url's content, the status code and the url the response came from
        
        
''' use 'yield' instead of 'return'
    As 'return' terminates the function and we need to get the results from each time
    the GET function is called by the loop '''
