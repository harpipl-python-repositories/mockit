from abc import ABC, abstractmethod
from azure.servicebus import ServiceBusReceivedMessage


class AbstractQueueHandler(ABC):
    @abstractmethod
    async def handle_message(self, message: ServiceBusReceivedMessage):
        pass
