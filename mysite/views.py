from django.shortcuts import render
from django.views import generic

from .filters import NewsFilter
from .forms import ApplicationForm
from .models import *


class HomePage(generic.TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['directors'] = Teacher.objects.filter(is_manage=True)
        context['cafedras'] = Cafedra.objects.all()[:10]
        context['site'] = SiteSetting.objects.all().first()
        context['news'] = News.objects.all()[:2]
        context['brands'] = Brands.objects.all()
        context['pages'] = Page.objects.all()
        return context


class CafedraListView(generic.ListView):
    model = Cafedra
    queryset = Cafedra.objects.all()
    template_name = 'course.html'
    paginate_by = 5
    context_object_name = 'cafedras'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cafedras'] = Cafedra.objects.all()[:10]
        context['site'] = SiteSetting.objects.all().first()
        context['pages'] = Page.objects.all()
        return context


class NewsListView(generic.ListView):
    template_name = 'blog-standard.html'
    model = News
    paginate_by = 5
    filter_class = NewsFilter
    context_object_name = 'news'
    queryset = News.objects.all()

    def get_queryset(self):
        query = self.queryset
        filter = self.filter_class(self.request.GET, queryset=query)
        query = filter.qs
        return query

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['cafedras'] = Cafedra.objects.all()[:10]
        context['new_news'] = News.objects.all()[:5]
        context['categories'] = Category.objects.all()
        context['site'] = SiteSetting.objects.all().first()
        context['pages'] = Page.objects.all()
        return context


class NewsDetailView(generic.DetailView):
    template_name = 'blog-details.html'
    model = News
    queryset = News.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['new_news'] = News.objects.all()[:5]
        context['site'] = SiteSetting.objects.all().first()
        context['cafedras'] = Cafedra.objects.all()[:10]
        context['related_news'] = News.objects.all().order_by('?')[:2]
        context['pages'] = Page.objects.all()
        return context


class TeacherDetailView(generic.DetailView):
    template_name = 'team-single.html'
    model = Teacher
    queryset = Teacher.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['site'] = SiteSetting.objects.all().first()
        context['pages'] = Page.objects.all()
        context['cafedras'] = Cafedra.objects.all()[:10]
        return context


class CafedraDetailView(generic.DetailView):
    template_name = 'course-single.html'
    model = Cafedra
    queryset = Cafedra.objects.all()
    context_object_name = 'cafedra'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['cafedras'] = Cafedra.objects.all()[:10]
        context['site'] = SiteSetting.objects.all().first()
        context['pages'] = Page.objects.all()
        return context


class ApplicationCreateView(generic.CreateView):
    success_url = '/'
    template_name = 'contact.html'
    form_class = ApplicationForm
    context_object_name = 'form'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['cafedras'] = Cafedra.objects.all()[:10]
        context['site'] = SiteSetting.objects.all().first()
        context['pages'] = Page.objects.all()
        return context


class AboutUsView(generic.TemplateView):
    template_name = 'about-us.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['cafedras'] = Cafedra.objects.all()[:10]
        context['site'] = SiteSetting.objects.all().first()
        context['pages'] = Page.objects.all()
        return context


class PageDetailView(generic.DetailView):
    template_name = 'page.html'
    queryset = Page.objects.all()
    model = Page
    context_object_name = 'page'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        context['cafedras'] = Cafedra.objects.all()[:10]
        context['site'] = SiteSetting.objects.all().first()
        context['pages'] = Page.objects.all()
        return context