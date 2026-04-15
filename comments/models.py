from django.db import models
from posts.models import Post
from users.models import User


class Comment(models.Model):
    description = models.TextField()
    created_at = models.DateField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_comments")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comments")

    def __str__(self):
        return f"{self.post}"


class Like(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_likes")

    def __str__(self):
        return f"{self.post}"