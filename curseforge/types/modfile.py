from .modfiletype import ModFileType

class ModFile:
    def __init__(self, json_data):
        self.id = int(json_data['id'])
        self.name = json_data['fileName']
        self.date = json_data['fileDate']
        self.length = json_data['fileLength']
        self.releaseType = ModFileType(json_data['releaseType'])
        self.downloadUrl = json_data['downloadUrl']
        self.gameVersions = json_data['gameVersion']