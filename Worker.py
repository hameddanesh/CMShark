from PyQt5.QtCore import QObject, pyqtSignal


class Worker(QObject):
    finished = pyqtSignal()
    progress = pyqtSignal(int)

    def __init__(self, sniffer, detectionTable, scanUrl, scanPayload, scanMLM,):
        super().__init__()
        self.sniffer = sniffer
        self.detectionTable = detectionTable
        self.scanUrl = scanUrl
        self.scanPayload = scanPayload
        self.scanMLM = scanMLM

    def run(self):
        """Long-running task."""
        self.sniffer.Sniff(self.detectionTable,
                           self.scanUrl, self.scanPayload, self.scanMLM)
        self.finished.emit()

    def stop(self):
        self._isRunning = False