from django.shortcuts import render, redirect
from .models import Articals
from .forms import ArticalsForm
from django.views.generic import DetailView, UpdateView, DeleteView
# Create your views here.
def news_home(request):
    news = Articals.objects.order_by('-date')
    return render(request, 'news/news_home.html', {'news': news})


class NewsDeleteView(DeleteView):
    model = Articals
    success_url = '/news/'
    template_name = 'news/news_delete.html'

class NewsDetailView(DetailView):
    model = Articals
    template_name = 'news/detail_view.html'
    context_object_name = 'article'


class NewsUpdateView(UpdateView):
    model = Articals
    template_name = 'news/create.html'
    form_class = ArticalsForm


def create(request):
    error = ""
    if request.method == 'POST' :
        form = ArticalsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Найдена ошибка в оформлении, попробуйте еще раз)"

    form = ArticalsForm()
    data = {
        'form': form,
        'error': error
    }
    return render(request, 'news/create.html', data)