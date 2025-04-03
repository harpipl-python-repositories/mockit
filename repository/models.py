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


class Application(models.Model):
    logical_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    name = models.CharField(unique=True, max_length=100)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['project', 'name'], name='unique_project_name')
        ]


class Resource(models.Model):
    logical_id = models.UUIDField(unique=True, default=uuid.uuid4, editable=False)
    application = models.ForeignKey(Application, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    uri = models.CharField(max_length=255)

    def __str__(self):
        return self.name
    
    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['application', 'name'], name='unique_application_name')
        ]
