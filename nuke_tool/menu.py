"""Menu integration for Nuke."""

try:
    import nuke
except Exception:  # Running outside Nuke
    nuke = None

from .interface import Pixel3DMMPanel


_panel = None


def launch_panel():
    global _panel
    if _panel is None:
        _panel = Pixel3DMMPanel()
    _panel.show()


def add_menu():
    """Add menu entry in Nuke to launch the panel."""
    if nuke is None:
        return
    nuke.menu('Nuke').addCommand('Pixel3DMM/Run Pipeline', launch_panel)
