class Mod:
    def __init__(self, id, name, slug, files, defaultFileId, filesByGameVersion):
        self.id = id
        self.name = name
        self.slug = slug
        self.files = files
        self.defaultFileId = defaultFileId
        self.filesByGameVersion = filesByGameVersion

    def get_file_by_id(self, fileId):
        """Returns a ModFile object of a file with specified fileId

        Parameters
        ----------
        fileId : int
            The file id

        Raises
        ------
        ValueError
            If no file with specified fileId is found
        """
        for f in self.files:
            if f.id == int(fileId):
                return f
        else:
            raise ValueError('No file for specified fileId')

    def get_file_by_game_version(self, gameVersion):
        """Returns a ModFile object of a latest file
        that supports specified gameVersion

        Parameters
        ----------
        gameVersion : string
            Game version string

        Raises
        ------
        ValueError
            If no file for specified game version is found
        """
        if gameVersion in self.filesByGameVersion:
            return self.get_file_by_id(self.filesByGameVersion[gameVersion])
        else:
            raise ValueError('No file for specified game version')

    def get_default_file(self):
        """Returns a ModFile object for the default file"""
        return self.get_file_by_id(self.defaultFileId)

    def get_supported_game_versions(self):
        """Returns a list of mod's supported game versions"""
        return list(self.filesByGameVersion.keys())