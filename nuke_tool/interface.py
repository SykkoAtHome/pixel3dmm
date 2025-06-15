"""Simple PySide2 interface for running the pipeline."""

try:
    from PySide2 import QtWidgets
except ImportError:  # Nuke 15 may expose PySide6
    from PySide6 import QtWidgets

from .run_pipeline import run_full_pipeline


class Pixel3DMMPanel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Pixel3DMM Pipeline")
        self.setLayout(QtWidgets.QVBoxLayout())

        self.path_edit = QtWidgets.QLineEdit(self)
        browse_btn = QtWidgets.QPushButton("Browse", self)
        run_btn = QtWidgets.QPushButton("Run", self)

        self.layout().addWidget(QtWidgets.QLabel("Video or Image Folder:"))
        self.layout().addWidget(self.path_edit)
        self.layout().addWidget(browse_btn)
        self.layout().addWidget(run_btn)

        browse_btn.clicked.connect(self._browse)
        run_btn.clicked.connect(self._run)

    def _browse(self) -> None:
        path = QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory")
        if path:
            self.path_edit.setText(path)

    def _run(self) -> None:
        path = self.path_edit.text().strip()
        if path:
            run_full_pipeline(path)
