from django.shortcuts import render, get_object_or_404

from .forms import CommentForm
from .models import Post
from django.core.paginator import Paginator

def post_list(request):
    post = Post.published.all()
    latest_posts = Post.published.order_by('created')[:5]
    pages_data = Paginator(post, 2)
    page_number = request.GET.get('page', 1)
    page = pages_data.get_page(page_number)
    is_paginated = page.has_other_pages()
    if page.has_previous():
        prev_url = '?page={}'.format(page.previous_page_number())
    else:
        prev_url = ''
    if page.has_next():
        next = '?page={}'.format(page.next_page_number())
    else:
        next = ''
    context = {
        'latest_posts': latest_posts,
        'post_data': page,
        'is_paginated': is_paginated,
        'next': next,
        'prev_url': prev_url,
    }
    return render(request, 'list.html', context)


def post_detail(request, post):
    post = get_object_or_404(Post, slug=post, status='published')
    comments = post.comments.filter(active=True)

    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()

    else:
        comment_form = CommentForm()


    context = {

        'post': post,
        'comments': comments,
        'new_comment': new_comment,
        'comment_form': comment_form
    }

    return render(request, 'detail.html', context)


