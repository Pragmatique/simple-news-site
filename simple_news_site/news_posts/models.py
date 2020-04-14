import datetime
from django.db import models
from django.urls import reverse
from authuser.models import MyUser
# from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify

# Create your models here.
POST_STATUSES=(
    ('DRAFT', "DRAFT"),
    ('APPROVE', "APPROVE"),
    ('DECLINE', "DECLINE"),
)


class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager, self).get_queryset().filter(status='APPROVE')


class Post(models.Model):
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, default='slug-field')
    body = RichTextUploadingField(null=True)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_posts')
    status = models.CharField(max_length=50, choices=POST_STATUSES, default=POST_STATUSES[0][0])
    publish = models.DateTimeField(default=datetime.datetime.now())
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created', 'status')

    objects = models.Manager()
    published = PublishedManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('news_posts:post_detail', args=[self.publish.year, self.publish.month,
                                                      self.publish.day, self.slug]
                       )


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='post_comments')
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='user_comments')
    text = models.CharField(max_length=500)
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ('-created',)

    def __str__(self):
        return 'Comment by {} on {}'.format(self.author, self.post.title)