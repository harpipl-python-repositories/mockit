from django.db import models
import uuid

class ProjectType(models.TextChoices):
    REST = 'REST', 'REST'
    SOAP = 'SOAP', 'SOAP'


class Project(models.Model):
    logical_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField(null=True)
    type = models.CharField(max_length=20, choices=ProjectType.choices, default=ProjectType.REST)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name', 'type'], name='unique_name_type')
        ]
# Create your models here.
