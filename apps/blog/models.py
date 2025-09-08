from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify
import uuid

User = get_user_model()


class Post(models.Model):
    """
    Blog Post (Main Entity)
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True, blank=True)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    # SEO + metadata
    meta_title = models.CharField(max_length=255, blank=True, null=True)
    meta_description = models.TextField(blank=True, null=True)

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(f"{self.title}-{str(uuid.uuid4())[:8]}")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class PostImage(models.Model):
    """
    Store multiple images per post
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="images")
    image = models.URLField()  #  Store Cloudinary/AWS S3 link
    caption = models.CharField(max_length=255, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)  # For image ordering


class PostVideo(models.Model):
    """
    Store multiple videos per post
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="videos")
    video = models.URLField()  # cloudinary links or AWS S3 link
    caption = models.CharField(max_length=255, blank=True, null=True)
    order = models.PositiveIntegerField(default=0)


class Comment(models.Model):
    """
    Nested comments system
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    parent = models.ForeignKey("self", on_delete=models.CASCADE, null=True, blank=True, related_name="replies")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comment by {self.user} on {self.post}"


class Like(models.Model):
    """
    Like system for posts and comments
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True, related_name="likes")
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, null=True, blank=True, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ("user", "post", "comment")  # Prevent duplicate likes


class Tag(models.Model):
    """
    Tags system for categorization
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class PostTag(models.Model):
    """
    Many-to-Many relation for Post <-> Tags
    """
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_tags")
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, related_name="tag_posts")

    class Meta:
        unique_together = ("post", "tag")
