from django.db import models
from django.contrib.auth.models import User
from PIL import Image   # pillow library used here to resize image while uploading in profile pic
# Create your models here.

class profile(models.Model):
	user=models.OneToOneField(User,on_delete=models.CASCADE)
	image=models.ImageField(default='profile_pic/person.jpg',upload_to='profile_pic')
	email=models.TextField()      #email=models.CharField(max_length=80)
	city=models.TextField()	 #city=models.CharField(max_length=40)

	def __str__(self):
		return f'{self.user.username} Profile'

	def save(self, *args, **kwargs):        # for resizing image,  save() is default  method from parent class
		super().save(*args, **kwargs)
		img = Image.open(self.image.path)
		if img.height>300 or img.width>300:
			output_size=(300,300)    # size that we want for all images
			img.thumbnail(output_size)
			img.save(self.image.path)


