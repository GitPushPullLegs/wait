import time


class Wait:
    def __init__(self, timeout: int = 120, poll_frequency: float = 0.5):
        self.timeout = timeout
        self.poll_frequency = poll_frequency if poll_frequency > 0 else 0.5
        self.__exceptions = []

    def until(self, method, **kwargs):
        """
        Calls the same method at the polling frequency until it returns a value or times out.
        :param method: The method to execute.
        :param kwargs: Any arguments the method takes.
        :return: Whatever the method returns.
        """
        end_time = time.time() + self.timeout

        while True:
            try:
                result = method(**kwargs)
                if result:
                    return result
            except Exception as exc:
                self.__exceptions.append(exc)

            time.sleep(self.poll_frequency)

            if time.time() > end_time:
                break

        raise TimeoutError(f"Wait timed out. Exceptions: {'None' if not self.__exceptions else self.__exceptions}")
