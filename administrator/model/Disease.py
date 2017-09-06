from django.db import models

class Disease(models.Model) :
    name = models.CharField(max_length=150)
    type = models.CharField( max_length=150)
    description = models.TextField(max_length=150)

    def __unicode__(self):
        return unicode((self.name, self.type))