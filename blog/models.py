from django.db import models
from django.utils import timezone
#gets information from other files so you don't have to copy/paste

class Post(models.Model): #defines our model (it's an object). Class is a keyword that indicates that we're defining an object. Post is the name of our model. Always start a class name with an uppercase letter. models.Model means that Post is a django model and will be saved in the database
    author = models.ForeignKey('auth.User') #this is a link to another model
    title = models.CharField(max_length=200) #define text with a limited number of characters
    text = models.TextField() #for long text without a limit
    created_date = models.DateTimeField(
            default=timezone.now)
    published_date = models.DateTimeField(
            blank=True, null=True)
    def publish(self): #this is defining the method of publish. Use lowercase and underscores for naming methods
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
