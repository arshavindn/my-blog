from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template import loader
from django.utils import timezone
from .models import Post
from .forms import PostForm


def post_list(request):
    if 'page' not in request.session:
        request.session['page'] = page = 0
    else:
        page = request.session['page']
    post_per_page = 3
    print(page)
    if request.GET.get("ajax_call") == '1':
        posts = Post.objects.filter(
            published_date__lte=timezone.now()).order_by('-published_date')[page*post_per_page:page*post_per_page+post_per_page]
        if posts:
            print(posts)
            request.session['page'] += 1
            template = loader.get_template('blog/post.html')
            context = {
                'posts': posts,
            }
            return HttpResponse(template.render(context, request),
                                content_type='html')
        else:
            return HttpResponse(status=404)
    else:

        request.session['page'] = 1

        posts = Post.objects.filter(
            published_date__lte=timezone.now()).order_by('-published_date')[:post_per_page]
        return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})


def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
