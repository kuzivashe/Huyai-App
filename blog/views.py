from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Item


def video(request):
	obj = Item.objects.all()
	return render(request, 'blog/home.html', {'obj': obj})


def home(request):
	context = {
		'posts': Post.objects.all()
	}
	return render(request,'blog/home.html', context)



class PostListView(ListView):
	model = Post
	template_name = 'blog/home.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	ordering = ['-date_posted']
	paginate_by = 3

class UserPostListView(ListView):
	model = Post
	template_name = 'blog/user_posts.html' #<app>/<model>_<viewtype>.html
	context_object_name = 'posts'
	paginate_by = 3

	def get_queryset(self):
		user = get_object_or_404(User, username=self.kwargs.get('username'))
		return Post.objects.filter(author=user).order_by('-date_posted')

class PostDetailView(DetailView):
	model = Post

'''fields will be required since we have to fill in a form'''
class PostCreateView(LoginRequiredMixin, CreateView):
	model = Post
	fields = ['title', 'content']

	#so that we can put in the author of a post, we must override default forms system
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form) 

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Post
	fields = ['title', 'content']

	#so that we can put in the author of a post, we must override default forms system
	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form) 
	
	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
	model = Post
	success_url = '/'

	def test_func(self):
		post = self.get_object()
		if self.request.user == post.author:
			return True
		return False

def about(request):
	return render(request, 'blog/about.html', {'title': about})
