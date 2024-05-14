from django.db import models
from django.urls import reverse


# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     author = models.ForeignKey(
#         "auth.User",
#         on_delete=models.CASCADE,
#     )
#     body = models.TextField()

#     def __str__(self):
#         return self.title


class Post(models.Model):
    id = models.AutoField(primary_key=True)  # Thêm khóa chính tự tăng
    name_facebook = models.CharField(max_length=255)
    href_value = models.CharField(max_length=255)
    ptit = models.CharField(max_length=255)
    birth_of_date = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    orientation = models.CharField(max_length=255)
    main_programming_language = models.CharField(max_length=255)
    priority = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)  # Thêm trường created_at

    other_note = models.CharField(max_length=255)

    def __str__(self):
        return self.name_facebook

    def get_absolute_url(self):
        return reverse("home")