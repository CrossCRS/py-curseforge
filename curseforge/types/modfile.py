from .modfiletype import ModFileType

class ModFile:
    def __init__(self, json_data):
        self.id = int(json_data['id'])
        self.name = json_data['fileName']
        self.display_name = json_data['displayName']
        self.date = json_data['fileDate']
        self.length = json_data['fileLength']
        self.release_type = ModFileType(json_data['releaseType'])
        self.download_url = json_data['downloadUrl']
        self.is_alternate = bool(json_data['isAlternate'])
        self.alternate_file_id = int(json_data['alternateFileId']) if json_data['alternateFileId'] else None
        self.server_pack_file_id = int(json_data['serverPackFileId']) if json_data['serverPackFileId'] else None
        self.is_available = bool(json_data['isAvailable'])
        self.game_versions = json_data['gameVersion']