from django.shortcuts import render, get_object_or_404
from django.views.generic.edit import CreateView

# Create your views here.

from .models import postagem, autor, comentario
from django.views import generic
from django.urls import reverse
from django.contrib.auth.mixins import PermissionRequiredMixin


def index(request):
    ultimos_artigos = postagem.objects.order_by('-data_postagem')[:3]
    context = {
        'ultimos_artigos': ultimos_artigos
    }
    return render(request, 'blog/index.html', context)


# def postagem_detail(request, postagem_id):
#    post = get_object_or_404(postagem, pk=postagem_id)
#    return render(request, 'blog/postagem_detail.html', {'post': post})

# Fazer por classe parece ser melhor nesse caso.
class PostagemDetailView(generic.DetailView):
    model = postagem


class AutorDetailView(generic.DetailView):
    model = autor


class PostagemListView(generic.ListView):
    model = postagem
    paginate_by = 5


class AutorListView(generic.ListView):
    model = autor
    paginate_by = 5


class ComentarioListView(generic.ListView):
    model = comentario


class ComentarioCreate(PermissionRequiredMixin, CreateView):
    model = comentario
    fields = ['conteudo']
    permission_required = 'blog.add_comentario'

    def get_context_data(self, **kwargs):
        context = super(ComentarioCreate, self).get_context_data(**kwargs)
        context['post'] = get_object_or_404(postagem, pk=self.kwargs['pk'])
        return context

    def form_valid(self, form):
        form.instance.usuario = self.request.user
        form.instance.postagem = get_object_or_404(
            postagem, pk=self.kwargs['pk'])
        return super(ComentarioCreate, self).form_valid(form)

    def get_success_url(self):
        pk = self.kwargs['pk']
        print(pk)
        return reverse('postagem-detail', kwargs={'pk': self.kwargs['pk']})
