class Mod:
    def __init__(self, json_data, files):
        self.id = json_data['id']
        self.name = json_data['name']
        self.slug = json_data['slug']
        self.summary = json_data['summary']
        self.date_modified = json_data['dateModified']
        self.date_created = json_data['dateCreated']
        self.date_released = json_data['dateReleased']
        self.files = files
        self.default_file_id = json_data['defaultFileId']
        self.website_url = json_data['websiteUrl']
        self.game_id = json_data['gameId']
        self.game_slug = json_data['gameSlug']
        self.game_name = json_data['gameName']
        self.download_count = json_data['downloadCount']
        self.is_featured = json_data['isFeatured']
        self.popularity_score = json_data['popularityScore']
        self.game_popularity_rank = json_data['gamePopularityRank']
        self.primary_language = json_data['primaryLanguage']
        self.is_available = json_data['isAvailable']
        self.is_experimental = json_data['isExperiemental'] # Not a typo
        self.files_by_game_version = {}

        for f in json_data['gameVersionLatestFiles']:
            self.files_by_game_version[f['gameVersion']] = int(f['projectFileId'])

    def get_file_by_id(self, file_id):
        """Returns a ModFile object of a file with specified file_id

        Parameters
        ----------
        file_id : int
            The file id

        Raises
        ------
        ValueError
            If no file with specified file_id is found
        """
        for f in self.files:
            if f.id == int(file_id):
                return f
        else:
            raise ValueError('No file for specified file_id')

    def get_file_by_game_version(self, game_version):
        """Returns a ModFile object of a latest file
        that supports specified game_version

        Parameters
        ----------
        game_version : string
            Game version string

        Raises
        ------
        ValueError
            If no file for specified game version is found
        """
        if game_version in self.files_by_game_version:
            return self.get_file_by_id(self.files_by_game_version[game_version])
        else:
            raise ValueError('No file for specified game version')

    def get_default_file(self):
        """Returns a ModFile object for the default file"""
        return self.get_file_by_id(self.default_file_id)

    def get_supported_game_versions(self):
        """Returns a list of mod's supported game versions"""
        return list(self.files_by_game_version.keys())