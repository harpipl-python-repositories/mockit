from core.services.queue import AbstractQueueHandler
from typing import List, Callable
import asyncio
from azure.servicebus.aio import ServiceBusClient


class QueueListener:
    def __init__(self, connection_string: str, handlers: List[AbstractQueueHandler]):
        self.connection_string = connection_string
        self.handlers = handlers
        self.servicebus_client = ServiceBusClient.from_connection_string(
            conn_str=self.connection_string
        )

    async def receive_messages(self, queue_name: str, handler: Callable):
        async with self.servicebus_client:
            async with self.servicebus_client.get_queue_receiver(
                queue_name=queue_name
            ) as receiver:
                while True:
                    messages = await receiver.receive_messages(
                        max_message_count=10, max_wait_time=1
                    )
                    for message in messages:
                        await handler(message)
                        await receiver.complete_message(message)

    async def start_listening(self):
        tasks = []
        for handler in self.handlers:
            tasks.append(
                self.receive_messages(handler.queue_name, handler.handle_message)
            )
        await asyncio.gather(*tasks)

    def start_listening_sync(self):
        loop = asyncio.new_event_loop()
        asyncio.set_event_loop(loop)
        try:
            loop.run_until_complete(self.start_listening())
        except KeyboardInterrupt:
            print("Keyboard interrupt")
        finally:
            loop.close()
