from .modfiletype import ModFileType

class ModFile:
    def __init__(self, id, name, date, length, releaseType, downloadUrl, gameVersions):
        self.id = id
        self.name = name
        self.date = date
        self.length = length
        self.releaseType = ModFileType(releaseType)
        self.downloadUrl = downloadUrl
        self.gameVersions = gameVersions