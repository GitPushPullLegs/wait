from .wait import Wait


class BrowserWait(Wait):

    def __init__(self, driver=None, **kwargs):
        """
        Instantiates a new BrowserWait instance.
        :param driver: The selenium driver to use, unnecessary if executing methods from the superclass, Wait.
        :param kwargs: The Wait argument.
        """
        super().__init__(**kwargs)
        self.driver = driver

    def until_angular_loads(self):
        """Returns when an AngularJS page loads completely."""
        return self.until(self._is_angular_loaded)

    def _is_angular_loaded(self):
        """Returns true if there are no pending http requests. Angular lists all network requests in a list."""
        return self.driver.execute_script("""
            return angular.element(document).injector().get('$http').pendingRequests.length === 0
        """)

    def until_file_downloaded(self):
        """Waits for the currently downloading file to finish then returns the file path. Requires a Google Chrome browser."""
        return self.until(self._is_file_downloaded)

    def _is_file_downloaded(self):
        """Checks Google Chrome's downloads page to see if the latest element's state is 'COMPLETE' if so,
        returns the file path. """
        self.driver.get('chrome://downloads')
        return self.driver.execute_script("""
        var items = document.querySelector('downloads-manager')
            .shadowRoot.querySelector('#downloadsList').items;
        var latestDownload = items[0]
        if (latestDownload.state === "COMPLETE")
            return latestDownload.fileURL || latestDownload.file_url || latestDownload.filePath;
        """)
