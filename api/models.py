from django.db import models

class Language(models.Model):
    name=models.CharField(max_length=50)
    paradigm=models.CharField(max_length=80)

    def __str__(self):
        return f"<Language {self.name}>"
