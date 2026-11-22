# missing_deps.py
from qgis.core import Qgis


class MissingDepsPlugin:
    def __init__(self, iface, missing):
        self.iface = iface
        self.missing = missing

    def initGui(self):
        pkgs = " ".join(self.missing)
        self.iface.messageBar().pushMessage(
            "form_profiler",
            f"Fehlende Python-Pakete: {', '.join(self.missing)}. "
            f"Bitte in der OSGeo4W Shell installieren: "
            f"python -m pip install {pkgs}",
            level=Qgis.MessageLevel.Warning,
            duration=0,   # bleibt stehen, bis der Nutzer sie schließt
        )

    def unload(self):
        pass