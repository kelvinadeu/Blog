import urllib.request,json
from .models import Random

base_url =None

#
# def configure_request(app):
#
#     global base_url
#     base_url= app.config['BASE_URL']
#
# def get_single(name):
#     '''
#     function that returns the json response from url
#     :return:
#     '''
#     get_single_url = base_url.format(name)
#     with urllib.request.urlopen(get_single_url) as url:
#         get_single_data = url.read()
#         get_single_response = json.loads(get_single_data)
#
#         single_result = None
#
#         single_result=process_single_result(get_single_response)
#
#
#     return single_result
#
#
# # def process_single_result(single_list):
# #     single_result = []
#     for today_item in single_list:
#         author = today_item.get('author')
#         quote = today_item.get('quote')
#
#         single_object = Random(author,quotes)
#         single_result.append(single_object)
#
#     return single_result
