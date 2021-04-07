import unittest
import curseforge

MOD_ID_VALID = 32274

class TestCurseforge(unittest.TestCase):

    def setUp(self):
        self.mod = curseforge.get_mod(MOD_ID_VALID)

    """ Test Mod object """
    def test_valid_mod(self):
        self.assertIsInstance(self.mod, curseforge.Mod)

    def test_mod_id(self):
        self.assertIs(type(self.mod.id), int)

    def test_mod_name(self):
        self.assertTrue(self.mod.name.strip())
        self.assertTrue(self.mod.slug.strip())

    def test_mod_files(self):
        self.assertIs(type(self.mod.files), list)

    def test_mod_files_by_game_version(self):
        self.assertIs(type(self.mod.filesByGameVersion), dict)
    
    """ Test ModFile object """
    def test_mod_file(self):
        self.assertIsInstance(self.mod.get_default_file(), curseforge.ModFile)
    
    def test_mod_file_id(self):
        self.assertIs(type(self.mod.get_default_file().id), int)

    def test_mod_file_name(self):
        self.assertTrue(self.mod.get_default_file().name.strip())

    def test_mod_file_download_url(self):
        self.assertTrue(self.mod.get_default_file().downloadUrl.strip())

    def test_mod_file_game_versions(self):
        self.assertIs(type(self.mod.get_default_file().gameVersions), list)
        self.assertGreater(len(self.mod.get_default_file().gameVersions), 0)

    """ Test exceptions """
    def test_invalid_mod_id(self):
        with self.assertRaises(ValueError):
            curseforge.get_mod(-1)

    def test_invalid_file_id(self):
        with self.assertRaises(ValueError):
            self.mod.get_file_by_id(-1)

    def test_invalid_game_version_for_file(self):
        with self.assertRaises(ValueError):
            self.mod.get_file_by_game_version("1.3.3.7")


if __name__ == '__main__':
    unittest.main()