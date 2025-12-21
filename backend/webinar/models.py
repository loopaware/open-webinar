from django.db import models

class Setting(models.Model):
    key = models.CharField(max_length=50, unique=True)
    value = models.TextField()
    description = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"{self.key}: {self.value[:50]}"

class Speaker(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    image = models.ImageField(upload_to='speakers/', blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'name']

    def __str__(self):
        return self.name

class AgendaItem(models.Model):
    time = models.CharField(max_length=50) # e.g. "09:00 - 10:00"
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    speaker = models.ForeignKey(Speaker, on_delete=models.SET_NULL, null=True, blank=True, related_name='sessions')
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order', 'time']

    def __str__(self):
        return f"{self.time} - {self.title}"

class Attendee(models.Model):

    name = models.CharField(max_length=100)

    email = models.EmailField(max_length=100)

    company = models.CharField(max_length=100, blank=True, null=True)

    experience = models.CharField(max_length=100, blank=True, null=True)

    date = models.CharField(max_length=50)

    image = models.ImageField(upload_to='attendees/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)



    def __str__(self):

        return self.name
