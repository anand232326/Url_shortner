from django.db import models

class URLMapping(models.Model):
    id = models.BigAutoField(primary_key=True)
    short_key = models.CharField(max_length=10, unique=True, db_index=True)
    long_url = models.URLField(max_length=2048)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.short_key} -> {self.long_url}"