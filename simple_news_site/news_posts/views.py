from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Post, Comment
from .forms import PostForm, CommentForm
from authuser.models import USER_GROUPS
from news_posts.models import POST_STATUSES


# Create your views here.
def	post_list(request):
    posts = Post.published.all()
    return render(request, 'post/list.html', {'posts': posts})


def	post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post, slug=slug, status='APPROVE', publish__year=year, publish__month=month,
                             publish__day=day)
    comments = post.post_comments.filter(active=True)
    new_comment = None

    if request.method == "POST":
        if not request.user.is_authenticated:
            return redirect('authuser:signing_in')
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.author = request.user
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'post/detail.html', {'post': post, 'comments':comments, 'comment_form':comment_form})


@login_required(login_url='/auth/sign-in/')
def	post_create(request):
    post_form = PostForm()
    context_dictionary = {
        "post_form": post_form,
    }

    if request.method == "POST":
        post_form = PostForm(request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            if request.user.group != USER_GROUPS[0][0]:
                new_post.status = POST_STATUSES[1][0]
            new_post.save()
            return redirect('news_posts:post_list')

    return render(request, 'post/create.html', context_dictionary)


