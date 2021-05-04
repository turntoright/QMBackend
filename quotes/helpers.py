from django.core.paginator import Paginator, EmptyPage

from .validators import fail_response, data_response_with_paging


PAGE_SIZE = 20


def paginate_queryset(request, queryset, result_parsing_func):
    try:
        page_num = int(request.GET['page'])
    except:
        page_num = 1

    paginator = Paginator(queryset, PAGE_SIZE)
    try:
        page = paginator.page(page_num)
    except EmptyPage:
        return fail_response('Invalid Page.')

    _filter = request.GET.get('filter')
    if _filter:
        data = result_parsing_func(page.object_list, _filter)
    else:
        data = result_parsing_func(page.object_list)
    return data_response_with_paging(
        paginator.count,
        paginator.num_pages,
        page.next_page_number() if page.has_next() else None,
        page.previous_page_number() if page.has_previous() else None,
        data
    )
