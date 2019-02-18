import urllib.request,json
from .models import Single,Random



api_key = None

base_url = get_news=None


def configure_request(app):

    global base_url_single,base_url_random
    base_url_single='      GET http://quotes.stormconsultancy.co.uk/quotes/1.json'
    base_url_random='GET http://quotes.stormconsultancy.co.uk/random.json'

def get_single(category):
    '''
    function that returns the json response from url
    :return:
    '''
    get_single_url = base_url_single.format
    with urllib.request.urlopen(get_single_url) as url:
        get_single_data = url.read()
        get_single_response = json.loads(get_single_data)

        single_result = None

        if get_single_response['singles']:
            single_result_list = get_single_response['single']
            single_result=process_single_result(single_result_list)



    return single_result


def process_single_result(single_list):
    single_result = []
    for single in single_list:
        id = single.get('id')
        author = single.get('author')
        quotes = single.get('quotes')
        single = Single(id,author,quotes)

        source_object = Sources(id,author,quotes)
        single_result.append(single_object)

    return single_result

def get_articles(category):
    get_articles_details_url = 'https://newsapi.org/v2/everything?sources={}&apiKey={}'.format(category,api_key)
    print(get_articles_details_url)

    with urllib.request.urlopen('https://newsapi.org/v2/sources?cartegory/general?&apiKey=854b811928a24b52a41fb275bc9bb457') as url:
        articles_details_data = url.read()
        articles_details_response = json.loads(articles_details_data)

        articles_object = None
        if articles_details_response["articles"]:
            articles_list=articles_details_response['articles']
            articles_object= process_article_results(articles_list)

    return articles_object
    news_results = process_article_results(articles_results_list)

    def process_article_results(article_list):
        """
        Function that processes the sourc list of articles that contain news details

        Args:
            articles_list:A list of articles that contain news details

        Returns :
               articles_results:A list of article objects

        """
        articles_results = []
        for articles in article_list:
            id = source.get('id')
            name = source.get(name)
            description = source.get(description)
            url = source.get(url)
            category = source.get(category)

            articles = Articles(id,name,description,url,category)
    return articles_results
