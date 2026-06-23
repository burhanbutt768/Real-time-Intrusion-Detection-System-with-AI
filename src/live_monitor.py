from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time


class LogHandler(
    FileSystemEventHandler
):

    def __init__(
        self,
        callback
    ):

        self.callback = callback

        self.last_event = 0

    def on_modified(
        self,
        event
    ):

        if not event.src_path.endswith(
            "auth.log"
        ):
            return

        current = time.time()

        # Prevent duplicate triggers
        if (
            current
            -
            self.last_event
            <
            0.5
        ):
            return

        self.last_event = current

        # Wait until save finishes
        time.sleep(
            0.2
        )

        self.callback()


def monitor_logs(
    filepath,
    callback
):

    observer = Observer()

    handler = LogHandler(
        callback
    )

    observer.schedule(
        handler,
        path="../logs",
        recursive=False
    )

    observer.start()

    print(
        "\n👁 Monitoring logs..."
    )

    try:

        while True:

            time.sleep(
                1
            )

    except KeyboardInterrupt:

        observer.stop()

    observer.join()