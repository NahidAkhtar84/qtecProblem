from django import template
from searchhistory.models import searchhistory
register = template.Library()


@register.filter(name ='keywords_count')
def keywords_count(keyword):
    try:
        return searchhistory.objects.filter(searchkey=keyword).count()
    except:
        return None
