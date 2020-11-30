from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from .models import Post
from .forms import PostForm

# Create your views here.
def home_view(request, *args, **kwargs):
	print(args, kwargs)
	print(request.user)
	
	item_list = Post.objects.order_by("-created_on")
	new_post = None
	# Post posted
	if request.method == 'POST':
		post_form = PostForm(request.POST)
		if post_form.is_valid():
			# Create Post object but don't save to database yet
			new_post = post_form.save(commit=False)
			# Save the post to the database
			new_post.save()
			return redirect('home')
	else:
		post_form = PostForm()


	
	page = {
			"Post" : Post,
			"list" : item_list,
			"post_form" : post_form,
	}
	# return HttpResponse("<h1>Hello World!</h1>")
	return render(request, "index.html", page)

def about_view(request):
	return render(request, "about.html")