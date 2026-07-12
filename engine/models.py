from django.db import models


class Story(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class Node(models.Model):
    story = models.ForeignKey(
        Story,
        on_delete=models.CASCADE,
        related_name="nodes"
    )

    title = models.CharField(max_length=200)
    text = models.TextField()

    def __str__(self):
        return self.title

class Choice(models.Model):
    from_node = models.ForeignKey(
        Node,
        on_delete=models.CASCADE,
        related_name="choices"
    )

    text = models.CharField(max_length=200)

    to_node = models.ForeignKey(
        Node,
        on_delete=models.CASCADE,
        related_name="incoming_choices"
    )

    def __str__(self):
        return self.text