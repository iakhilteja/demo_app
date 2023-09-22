from django.db import models

class AudioFile(models.Model):
    file = models.FileField(upload_to='audio_files/')
    # transcript = models.TextField(null=True, blank=True)
    # created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.file.name
