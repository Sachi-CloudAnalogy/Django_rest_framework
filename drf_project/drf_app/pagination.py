from rest_framework.pagination import PageNumberPagination

class MyPagination(PageNumberPagination):
    page_size = 5
    # page_query_param = 'p'   # by default it is page
    page_size_query_param = 'records'    #it let client decide what page_size they want
    max_page_size = 8
    # last_page_strings = 'end'     #by default it is last
