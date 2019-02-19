import urllib.request,json
from .models import Single



api_key = None

base_url = get_news=None


def configure_request(app):

    global base_url_single,base_url_random
    base_url_single='http://quotes.stormconsultancy.co.uk/quotes.json'
    base_url_random='GET http://quotes.stormconsultancy.co.uk/random.json'

def get_single():
    '''
    function that returns the json response from url
    :return:
    '''
    # get_single_url = base_url_single.format(category)
    with urllib.request.urlopen(base_url_single, timeout=5) as url:
        get_single_data = url.read()
        get_single_response = json.loads(get_single_data)

        single_result = None


        single_result=process_single_result(get_single_response)



    return single_result


def process_single_result(single_list):
    single_result = []
    for single in single_list:
        id = single.get('id')
        author = single.get('author')
        quotes = single.get('quotes')

        single_object = Single(id,author,quotes)
        single_result.append(single_object)

    return single_result
