from azure.servicebus import ServiceBusReceivedMessage

from core.services.queue import AbstractQueueHandler
from core.services.queue.decorators import ServiceBusListener

@ServiceBusListener(queue_name="ocn-ticket-new", connection_string_env_var="SERVICEBUS_CONNECTION_STRING")
class OcnTicketNewQueueHandler(AbstractQueueHandler):
    async def handle_message(self, message: ServiceBusReceivedMessage):
        print(f"Received message from {self.queue_name}: {message}")
        return message

@ServiceBusListener(queue_name="ocn-ticket-extract", connection_string_env_var="SERVICEBUS_CONNECTION_STRING")
class OcnTicketExtractQueueHandler(AbstractQueueHandler):
    async def handle_message(self, message: ServiceBusReceivedMessage):
        print(f"Received message from {self.queue_name}: {message}")
        return message
