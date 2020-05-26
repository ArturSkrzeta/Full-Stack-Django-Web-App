from django.shortcuts import render, get_object_or_404
from .models import PR
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.db.models import Q

### Search

class SearchView(ListView):
    model = PR
    template_name = 'prs/search.html'
    context_object_name = 'all_search_results'

    def get_queryset(self):
       result = super(SearchView, self).get_queryset()
       query = self.request.GET.get('search')
       if query:
          postresult = PR.objects.filter(pr_number=query)
          result = postresult
       else:
           result = None
       return result

### Control

class CategoryListView(ListView):
    model = PR
    template_name = 'prs/categories.html'
    context_object_name = 'prs'

class BuyerListView(ListView):
    model = User
    template_name = 'prs/buyers.html'
    context_object_name = 'buyers'

### PR List

class PRListView(ListView):
    model = PR
    template_name = 'prs/home.html'
    context_object_name = 'prs'
    ordering = ['-date_posted']
    #paginate_by = 5

    def get_queryset(self):
        return PR.objects.filter(Q(status="Approval") | Q(status="Done") | Q(status="On Hold") | Q(status="Pending") | Q(status="Open")).order_by('-date_posted')

class UserPRListView(ListView):
    model = PR
    template_name = 'prs/user_prs.html'
    context_object_name = 'prs'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        user = get_object_or_404(User, username=self.kwargs.get('username'))
        return PR.objects.filter(author=user).order_by('-date_posted')

class ArchivePRListView(ListView):
    model = PR
    template_name = 'prs/prs_archive.html'
    context_object_name = 'prs'
    ordering = ['-date_posted']
    paginate_by = 5

    def get_queryset(self):
        #status = get_object_or_404(PR, status=self.kwargs.get('closed'))
        return PR.objects.filter(status='Closed').order_by('-date_posted')


##

class PRDetailView(DetailView):
    model = PR
    template_name = 'prs/pr_detail.html'
    context_object_name = 'pr'

class PRCreateView(LoginRequiredMixin, CreateView):
    model = PR
    template_name = 'prs/pr_new.html'
    fields = ['pr_number', 'status', 'category','description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PRUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = PR
    template_name = 'prs/pr_update.html'
    fields = ['status', 'category', 'description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        pr = self.get_object()
        if self.request.user == pr.author or self.request.user.username == 'Admin':
            return True
        return False

class PRDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = PR
    template_name = 'prs/pr_delete.html'
    success_url = '/'

    def test_func(self):
        pr = self.get_object()
        if self.request.user == pr.author or self.request.user.username == 'Admin':
            return True
        return False
