from qgis.PyQt.QtCore import QSettings, QDir
import os

settings = QSettings()
data_dir = settings.value("dataDirs/dataDir", QDir.homePath() + "/.landuseAnalyst/")
print(f"QSettings dataDirs/dataDir: {data_dir}")

# Also check other relevant keys
print(f"landuse_analyst/debug: {settings.value('landuse_analyst/debug')}")

# Check if directory exists
if os.path.exists(data_dir):
    print(f"Directory exists: {data_dir}")
    print(f"Contents: {os.listdir(data_dir)}")
else:
    print(f"Directory DOES NOT exist: {data_dir}")
