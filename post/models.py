from django.db import models

# Create your models here.
from django.urls import reverse
# from django.utils import timezone
from django.contrib.auth.models import User


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')


class Post(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published')
    )

    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE,
                               related_name='blog_posts')
    body = models.TextField()

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)
    image = models.ImageField(upload_to='posts/%Y/%m/%d/', blank=True)

    # Менеджер по умолчанию
    objects = models.Manager()
    # Менеджер который мы создали
    published = PublishedManager()

    tags = models.ManyToManyField('Tag', blank = True, related_name = 'posts')


    class Meta:
        ordering = ['-created']
        verbose_name = 'Пост'
        verbose_name_plural = 'Посты'

    def get_absolute_url(self):
        return reverse('post_detail', args=[self.slug])

    def __str__(self):
        return self.title


class Comment(models.Model,):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=50, verbose_name = 'Имя')
    body = models.TextField(verbose_name = 'Комментария')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)



    class Meta:
        ordering = ['-created']
        verbose_name = 'Коментария'
        verbose_name_plural = 'Коментарии'

    def __str__(self):
        return 'Comment by {} on {}'.format(self.name, self.post,)

class Tag(models.Model):
    name = models.CharField(max_length=50,)
    slug = models.SlugField(max_length=50, unique=True)
    objects = models.Manager()

    def get_absolute_url(self):
        return reverse('tag_detail_url', kwargs={'slug': self.slug})

    class Meta:

        verbose_name = 'Тег'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name