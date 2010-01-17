from django.views.generic.date_based import object_detail 
from d51.django.apps.blogs.models import Post

def post_detail(request, year, month, day, slug):
    object_detail_kwargs = {
        'month_format':'%b',
        'date_field':'published',
        'slug_field':'slug',
        'template_object_name':'post',
        'queryset':Post.objects.all(),
        'year':year,
        'month':month,
        'day':day,
        'slug':slug,
        'allow_future':False,
    }
    return object_detail(request, **object_detail_kwargs)

