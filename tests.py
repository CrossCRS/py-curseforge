import unittest

from curseforge import CurseForge
from curseforge.types import Author, Category, Mod, ModFile, ModFileType

MOD_ID_VALID = 32274

class TestCurseforge(unittest.TestCase):

    def setUp(self):
        self.cf = CurseForge()
        self.mod = self.cf.get_mod(MOD_ID_VALID)

    """ Test Mod object """
    def test_valid_mod(self):
        self.assertIsInstance(self.mod, Mod)

    def test_mod_id(self):
        self.assertIs(type(self.mod.id), int)

    def test_mod_name(self):
        self.assertTrue(self.mod.name.strip())
        self.assertTrue(self.mod.slug.strip())

    def test_mod_authors(self):
        self.assertGreaterEqual(len(self.mod.authors), 1)
        self.assertIsInstance(self.mod.authors[0], Author)

    def test_mod_categories(self):
        self.assertGreaterEqual(len(self.mod.categories), 1)
        self.assertIsInstance(self.mod.categories[0], Category)

    def test_mod_files(self):
        self.assertIs(type(self.mod.files), list)

    def test_mod_files_by_game_version(self):
        self.assertIs(type(self.mod.files_by_game_version), dict)
    
    """ Test ModFile object """
    def test_mod_file(self):
        self.assertIsInstance(self.mod.get_default_file(), ModFile)
    
    def test_mod_file_id(self):
        self.assertIs(type(self.mod.get_default_file().id), int)

    def test_mod_file_name(self):
        self.assertTrue(self.mod.get_default_file().name.strip())

    def test_mod_file_download_url(self):
        self.assertTrue(self.mod.get_default_file().download_url.strip())

    def test_mod_file_game_versions(self):
        self.assertIs(type(self.mod.get_default_file().game_versions), list)
        self.assertGreater(len(self.mod.get_default_file().game_versions), 0)

    """ Test exceptions """
    def test_invalid_mod_id(self):
        with self.assertRaises(ValueError):
            self.cf.get_mod(-1)

    def test_invalid_file_id(self):
        with self.assertRaises(ValueError):
            self.mod.get_file_by_id(-1)

    def test_invalid_game_version_for_file(self):
        with self.assertRaises(ValueError):
            self.mod.get_file_by_game_version("1.3.3.7")


if __name__ == '__main__':
    unittest.main()