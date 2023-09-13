from rest_framework.pagination import PageNumberPagination

class LargeSetPagination(PageNumberPagination):
    page_size = 18
    page_query_param = 'p'
    page_size_query_param = 'p'
    max_page_size = 18
    

class MediumSetPagination(PageNumberPagination):
    page_size = 12
    page_query_param = 'p'
    page_size_query_param = 'p'
    max_page_size = 12
    

class SmallSetPagination(PageNumberPagination):
    page_size = 8
    page_query_param = 'p'
    page_size_query_param = 'p'
    max_page_size = 8        