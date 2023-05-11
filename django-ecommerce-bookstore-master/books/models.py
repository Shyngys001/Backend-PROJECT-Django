
from django.db import models
from django.urls import reverse

class Book(models.Model):
    title  = models.CharField(max_length = 200)
    author = models.CharField(max_length = 200)
    description = models.CharField(max_length = 500, default=None)
    price = models.FloatField(null=True, blank=True)
    image_url = models.CharField(max_length = 2083, default="https://avatars.mds.yandex.net/i?id=06568aa568af79365d7c1ee286abfcbc805406c7-9180973-images-thumbs&n=13")
    follow_author = models.CharField(max_length=2083, blank=True)  
    book_available = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Order(models.Model):
	product = models.ForeignKey(Book, max_length=200, null=True, blank=True, on_delete = models.SET_NULL)
	created =  models.DateTimeField(auto_now_add=True) 

	def __str__(self):
		return self.product.title
