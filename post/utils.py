from django.shortcuts import render, get_object_or_404



from .models import *


class ObjectDetailMixin:
    model = None
    template = None

    def get(self, request, slug):
        obj = get_object_or_404(self.model, slug__iexact=slug)
        latest_posts = Post.published.order_by('created')[:5]

        return render(request, self.template, context = {self.model.__name__.lower(): obj,
                                                            'latest_posts': latest_posts,

                                                         })

