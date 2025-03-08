from django.db import models
from accounts.models import User
from django.core.validators import FileExtensionValidator


class FutureMessage(models.Model):
    title = models.CharField(max_length=255)
    message = models.TextField()
    delivery_date = models.DateTimeField()
    is_opened = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    reflection_questions = models.TextField(null=True, blank=True)
    mood = models.CharField(max_length=255, null=True, blank=True)
    life_stage = models.CharField(max_length=255, null=True, blank=True)

    def __str__(self):
        return self.title


class BaseMessageMedia(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True
        ordering = ["-uploaded_at"]


class Photo(BaseMessageMedia):
    future_message = models.ForeignKey(
        FutureMessage,
        on_delete=models.CASCADE,
        related_name="photo_set",
        null=True,  #!Remove null while deploying or changing DB
    )
    image = models.ImageField(
        upload_to="future_messages/photos/%Y/%m",
        validators=[FileExtensionValidator(["jpg", "jpeg", "png", "gif"])],
    )


class Video(BaseMessageMedia):
    future_message = models.ForeignKey(
        FutureMessage,
        on_delete=models.CASCADE,
        related_name="video_set",
        null=True,  #!Remove null while deploying or changing DB
    )
    video = models.FileField(
        upload_to="gallery/videos/%Y/%m",
        validators=[FileExtensionValidator(["mp4", "mov", "avi"])],
    )


class LifeGoal(models.Model):
    future_message = models.ForeignKey(FutureMessage, on_delete=models.CASCADE)
    goal = models.TextField()
    achieved = models.BooleanField(default=False)
    reflection = models.TextField()
