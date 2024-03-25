from django.shortcuts import render, redirect, get_object_or_404
from . import models
from .forms import CodeListingForm
from django.http import HttpRequest, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from django.db.models import Q
from chat.models import Discussion

User = get_user_model()

def index(request: HttpRequest) -> HttpResponse:
    discussions = Discussion.objects.all().order_by('-created_at')[:5]
    context = {
        'codes_count': models.CodeListing.objects.count(),
        'users_count': models.User.objects.count(),
         'discussions': discussions,
    }
    return render(request, 'codes/index.html', context)

@login_required
def codes_create(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        form = CodeListingForm(request.POST, request.FILES)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.user = request.user
            listing.save()
            return redirect('codes_detail', listing.pk)
    else:
        form = CodeListingForm()
    return render(request, 'codes/codes_create.html', {'form': form})

def codes_list(request: HttpRequest) -> HttpResponse:
    return render(request, 'codes/codes_list.html', {
        'codes_list': models.CodeListing.objects.all(),
    })

def codes_detail(request: HttpRequest, pk) -> HttpResponse:
    return render(request, 'codes/codes_detail.html', {
        'listing': get_object_or_404(models.CodeListing, pk=pk),
    })

def codes_search(request: HttpRequest) -> HttpResponse:
    search_term = request.GET.get('search', '')
    codes_list = models.CodeListing.objects.all()
    print(f"Search term: {search_term}")
    if search_term:
        codes_list = codes_list.filter(
            Q(title__icontains=search_term) | 
            Q(category__icontains=search_term)
        )

    context = {'codes_search': codes_list}
    return render(request, 'codes/codes_search.html', context)