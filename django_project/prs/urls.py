from django.urls import path
from . import views
from .views import SearchView, CategoryListView, BuyerListView, PRListView, ArchivePRListView, PRDetailView, PRCreateView, UserPRListView, PRUpdateView, PRDeleteView

urlpatterns = [
    path('', PRListView.as_view(), name='prs-home'),
    path('user/<str:username>', UserPRListView.as_view(), name='user-prs'),
    path('pr/<int:pk>/', PRDetailView.as_view(), name='pr-detail'),
    path('pr/new/', PRCreateView.as_view(), name='pr-create'),
    path('pr/<int:pk>/update/', PRUpdateView.as_view(), name='pr-update'),
    path('post/<int:pk>/delete/', PRDeleteView.as_view(), name='pr-delete'),
    path('categories/', CategoryListView.as_view(), name='pr-categories'),
    path('buyers/', BuyerListView.as_view(), name='buyers'),
    path('archive/', ArchivePRListView.as_view(), name='pr-archive'),
    path('search/', SearchView.as_view(), name='pr-search'),
]
