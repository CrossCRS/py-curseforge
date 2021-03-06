import urllib.request
import json

from .types import Mod, ModFile, ModFileType

class CurseForge:
    def __init__(self):
        self.api_url = 'https://addons-ecs.forgesvc.net/api/v2/addon/'

    def get_mod_files(self, id):
        files = []

        res = urllib.request.urlopen(self.api_url + str(id) + '/files')
        res_body = res.read()
        j = json.loads(res_body.decode('utf-8'))

        for mod_file in j:
            f = ModFile(mod_file)
            files.append(f)

        return files

    def get_mod(self, id):
        """Returns a Mod object of a mod with specified id

        Parameters
        ----------
        id : int
            CurseForge Project Id
        
        Raises
        ------
        ValueError
            If no mod for specified Project Id is found
        """
        try:
            files = self.get_mod_files(id)

            res = urllib.request.urlopen(self.api_url + str(id))
            res_body = res.read()
            j = json.loads(res_body.decode('utf-8'))

            mod = Mod(j, files)
            return mod
        except urllib.error.HTTPError as e:
            if e.code == 404:
                raise ValueError('No mod for specified Project Id found')
            else:
                raise