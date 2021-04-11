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
        self.is_alternate = json_data['isAlternate']
        self.alternate_file_id = json_data['alternateFileId']
        self.server_pack_file_id = json_data['serverPackFileId']
        self.is_available = json_data['isAvailable']
        self.game_versions = json_data['gameVersion']