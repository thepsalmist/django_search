from django.shortcuts import render
from .models import Journal


def BootstrapFilterView(request):
    qs = Journal.objects.all()
    title_contains_query = request.GET.get('title_contains')
    title_exact_query = request.GET.get('title_exact')
    title_or_author_query = request.GET.get('title_or_author')

    if title_contains_query != '' and title_contains_query is not None:
        qs = qs.filter(title__icontains=title_contains_query)

    context = {
        'queryset': qs
    }

    return render(request, 'core/bootstrap_form.html', context)
