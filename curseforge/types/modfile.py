from .modfiletype import ModFileType

class ModFile:
    def __init__(self, json_data):
        self.id = int(json_data['id'])
        self.name = json_data['fileName']
        self.date = json_data['fileDate']
        self.length = json_data['fileLength']
        self.release_type = ModFileType(json_data['releaseType'])
        self.download_url = json_data['downloadUrl']
        self.game_versions = json_data['gameVersion']