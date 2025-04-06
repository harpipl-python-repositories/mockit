from .listeners import QueueListener
import functools
import os
import threading


def ServiceBusListener(queue_name: str = None, connection_string_env_var: str = None):
    def decorator(queue_handler_class):
        if not queue_name:
            raise ValueError("Queue name is required")
        if not connection_string_env_var:
            raise ValueError("Connection string env. var. is required (eg. SERVICEBUS_CONNECTION_STRING)")

        @functools.wraps(queue_handler_class)
        def wrapper(*args, **kwargs):
            handler = queue_handler_class(*args, **kwargs)
            handler.queue_name = queue_name

            connection_string = os.getenv(connection_string_env_var)
            if not connection_string:
                raise ValueError(f"{connection_string_env_var} not set in environment")

            print(f"Starting listener for queue: {handler.queue_name}")
            listener = QueueListener(connection_string, [handler])

            thread = threading.Thread(
                target=listener.start_listening_sync,
                daemon=True,
                name=f"Listener-{handler.queue_name}",
            )
            thread.start()
            print(f"Listener thread started: {thread.name}")

            return handler

        return wrapper

    return decorator
