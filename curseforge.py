#!/usr/bin/env python3
import urllib.request
import json
import enum

API_URL = 'https://addons-ecs.forgesvc.net/api/v2/addon/'

class ModFileType(enum.Enum):
   Release = 1
   Beta = 2
   Alpha = 3

class ModFile:
    def __init__(self, id, name, date, length, releaseType, downloadUrl, gameVersions):
        self.id = id
        self.name = name
        self.date = date
        self.length = length
        self.releaseType = ModFileType(releaseType)
        self.downloadUrl = downloadUrl
        self.gameVersions = gameVersions

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

def get_mod_files(id):
    files = []

    res = urllib.request.urlopen(API_URL + str(id) + '/files')
    res_body = res.read()
    j = json.loads(res_body.decode('utf-8'))

    for modFile in j:
        f = ModFile(int(modFile['id']), modFile['fileName'], modFile['fileDate'], modFile['fileLength'], modFile['releaseType'], modFile['downloadUrl'], modFile['gameVersion'])
        files.append(f)

    return files

def get_mod(id):
    """Returns a Mod object of a mod with specified id

    Parameters
    ----------
    id : int
        CurseForge Project Id
    """
    files = get_mod_files(id)

    res = urllib.request.urlopen(API_URL + str(id))
    res_body = res.read()
    j = json.loads(res_body.decode('utf-8'))

    fgv = {}
    for f in j['gameVersionLatestFiles']:
        fgv[f['gameVersion']] = int(f['projectFileId'])

    mod = Mod(int(j['id']), j['name'], j['slug'], files, j['defaultFileId'], fgv)
    return mod