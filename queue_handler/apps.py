from django.apps import AppConfig
import threading


class QueueHandlerConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'queue_handler'

    def ready(self):
        from . import listeners

        handler = listeners.OcnTicketNewQueueHandler()
        handler = listeners.OcnTicketExtractQueueHandler()