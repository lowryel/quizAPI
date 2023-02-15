from django.db.models.signals import post_save
from rest_framework.authtoken.models import Token
from django.conf import settings
from django.dispatch import receiver
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=255)
    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")   
    def __str__(self):
        return self.name


class Quizzes(models.Model):
    category = models.ForeignKey(Category, default=1, on_delete=models.DO_NOTHING)
    
    class Meta:
        verbose_name=_("Quiz")
        verbose_name_plural = _("Quizzes")
        ordering = ["id"]
    title = models.CharField(max_length=255, default=_("New Quiz"), verbose_name=_("Quiz Title"))
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Updated(models.Model):
    date_updated = models.DateTimeField(auto_now=True, verbose_name=_("Last Updated"))

    class Meta:
        abstract = True

class Question(Updated):
    class Meta:
        verbose_name = _("Question")
        verbose_name_plural = _("Questions")
        ordering = ["id"]

    SCALE = (
        (0, _("Fundamental")),
        (1, _("Beginner")),
        (2, _("Intermediate")),
        (3, _("Advanced")),
        (4, _("Expert")),
    )
    TYPE = (
        (0, _("Multiple Choice")),
    )
    quiz = models.ForeignKey(Quizzes, related_name='question', on_delete=models.DO_NOTHING)
    technique = models.IntegerField(choices=TYPE, verbose_name=_("Type of Question"), default=1)
    title = models.CharField(max_length=255, verbose_name=_("Title"))
    difficulty = models.IntegerField(choices=SCALE, verbose_name=_("Difficulty"), default=0)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))
    is_active = models.BooleanField(default=False, verbose_name=_("Active Status"))

    def __str__(self):
        return self.title

class Answer(Updated):
    class Meta:
        verbose_name = _("Answer")
        verbose_name_plural = _("Answers")
        ordering = ["id"]
    question = models.ForeignKey(Question, related_name='answer', on_delete=models.DO_NOTHING)
    answer_text = models.CharField(max_length=255, verbose_name=_("Answer Text"))
    is_right = models.BooleanField(default=False)

    def __str__(self):
        return self.answer_text


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    for user in User.objects.all():
        Token.objects.get_or_create(user=user)

