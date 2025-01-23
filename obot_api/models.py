from django.db import models
from users.models import UserAccount


class Course(models.Model):
    name = models.CharField(max_length=150)
    desc = models.CharField(max_length=300)
    owner = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Source(models.Model):
    SOURCE_TYPES = [
        ('document', 'Document'),  # text files or pdf files
        ('youtube', 'YouTube URL'),  # youtube url, which is the main focus.
    ]
    course = models.ForeignKey(
        'Course', on_delete=models.CASCADE, related_name='sources')
    source_type = models.CharField(max_length=20, choices=SOURCE_TYPES)
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    youtube_url = models.URLField(null=True, blank=True)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title

    def get_source(self):
        if self.source_type == 'document':
            return self.document
        elif self.source_type == 'youtube':
            return self.youtube_url


class ChatMessage(models.Model):
    MESSAGE_TYPES = [
        ('text', 'Text'),
        ('link', 'Link'),
    ]

    course = models.ForeignKey(
        'Course', on_delete=models.CASCADE, related_name='chat_messages')
    author = models.ForeignKey(UserAccount, on_delete=models.CASCADE)
    message_type = models.CharField(max_length=20, choices=MESSAGE_TYPES)
    text = models.TextField(null=True, blank=True)
    link = models.URLField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.author.username}'s message in {self.notebook.name}"

    def get_message_content(self):
        if self.message_type == 'text':
            return self.text
        elif self.message_type == 'link':
            return self.link
        elif self.message_type == 'image':
            return self.image
