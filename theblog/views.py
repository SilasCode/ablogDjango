from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView #builtin query functions
from .models import Post, Category, Comment #calling model Post
from .forms import PostForm, EditForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect

#def home(request):
	#return render(request, 'home.html', {})

def LikeView(request, pk):
	post = get_object_or_404(Post, id=request.POST.get('post_id'))
	liked = False
	if post.likes.filter(id=request.user.id).exists():
		post.likes.remove(request.user)
		liked = False
	else: 
		post.likes.add(request.user)
		liked = True

	return HttpResponseRedirect(reverse('article-detail', args=[str(pk)]))

class HomeView(ListView):
	model = Post
	template_name = 'home.html'
	ordering = ['-post_date']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		cat_menu2 = Category.objects.all()[:6]
		slide_post = Post.objects.all()[:6]
		pull_three_post = Post.objects.all()[:6]
		single_posts = Post.objects.filter(category= 'World Topic').all()[3:3]
		single_posts2 = Post.objects.filter(category= 'Sport').all()[:3]
		single_posts3 = Post.objects.filter(category= 'Africa News').all()[:3]
		single_posts4 = Post.objects.filter(category= 'Religion').all()[:3]
		single_posts5 = Post.objects.filter(category= 'Politics').all()[:3]
		single_posts6 = Post.objects.filter(category= 'Tv Shows').all()[:3]
		context = super(HomeView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		context["cat_menu2"] = cat_menu2
		context["pull_three_post"] = pull_three_post
		context["slide_post"] = slide_post
		context["single_posts"] = single_posts
		context["single_posts2"] = single_posts2
		context["single_posts3"] = single_posts3
		context["single_posts4"] = single_posts4
		context["single_posts5"] = single_posts5
		context["single_posts6"] = single_posts6
		return context

def CategoryListView(request):
	cat_menu_list = Category.objects.all()
	return render(request, 'category_list.html', {'cat_menu_list':cat_menu_list})

def CategoryView(request, cats):
	category_posts = Post.objects.filter(category=cats.replace('-', ' ').title()) #query to filter stuff in a model
	return render(request, 'categories.html', {'cats':cats.title().replace('-', ' '), 'category_posts':category_posts})


class ArticleDetailView(DetailView):
	model = Post
	template_name = 'article_details.html'

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		pull_related_post = Post.objects.all()[:3]
		context = super(ArticleDetailView, self).get_context_data(*args, **kwargs)
		

		stuff = get_object_or_404(Post, id=self.kwargs['pk'])
		total_likes = stuff.total_likes()

		liked = False
		if stuff.likes.filter(id=self.request.user.id).exists():
			liked = True

		context["cat_menu"] = cat_menu
		context["pull_related_post"] = pull_related_post
		context["total_likes"] = total_likes
		context["liked"] = liked
		return context

class AddPostView(CreateView):
	model = Post
	form_class = PostForm
	template_name = 'add_post.html'
	#fields = '__all__' #//for selecting all fields 
	#fields = ('title', 'title_tag', 'body') #to select only title and body from model

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(AddPostView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class AddCommentView(CreateView):
	model = Comment
	form_class = CommentForm
	template_name = 'add_comment.html'
	#fields = '__all__' #//for selecting all fields 
	#fields = ('title', 'title_tag', 'body') #to select only title and body from model
	success_url = reverse_lazy('home') #change to redirect to aricle page

	def form_valid(self, form):
		form.instance.post_id = self.kwargs['pk']
		return super().form_valid(form)


class AddCategoryView(CreateView):
	model = Category
	
	#form_class = PostForm
	template_name = 'add_category.html'
	fields = '__all__' #//for selecting all fields 
	#fields = ('title', 'title_tag', 'body') #to select only title and body from model

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(AddCategoryView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class UpdatePostView(UpdateView):
	model = Post
	form_class = EditForm
	template_name = 'update_post.html'
	#fields = ['title', 'title_tag', 'body']

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(UpdatePostView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context

class DeletePostView(DeleteView):
	model = Post
	template_name = 'delete_post.html'
	success_url = reverse_lazy('home')

	def get_context_data(self, *args, **kwargs):
		cat_menu = Category.objects.all()
		context = super(DeletePostView, self).get_context_data(*args, **kwargs)
		context["cat_menu"] = cat_menu
		return context