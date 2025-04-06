from abc import ABC
from azure.servicebus import ServiceBusReceivedMessage


class AbstractQueueHandler(ABC):
    async def handle_message(self, message: ServiceBusReceivedMessage):
        pass
