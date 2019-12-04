from django.shortcuts import render
from django.db.models import Q
from .models import Journal

# helper function to remove the repetition


def is_valid_queryparam(param):
    return param != '' and param is not None


def BootstrapFilterView(request):
    qs = Journal.objects.all()
    title_contains_query = request.GET.get('title_contains')
    id_exact_query = request.GET.get('ID_exact')
    title_or_author_query = request.GET.get('title_or_author')

    if is_valid_queryparam(title_contains_query):
        qs = qs.filter(title__icontains=title_contains_query)
    elif is_valid_queryparam(id_exact_query):
        qs = qs.filter(id=id_exact_query)
    elif is_valid_queryparam(title_or_author_query):
        qs = qs.filter(Q(title_icontains=title_or_author_query) | Q(
            author__name__icontains=title_or_author_query)).distinct()

    context = {
        'queryset': qs
    }

    return render(request, 'core/bootstrap_form.html', context)
