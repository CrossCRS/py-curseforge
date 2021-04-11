from curseforge import CurseForge

def main():
    cf = CurseForge()
    mod = cf.get_mod(32274) # Get a mod object by project id

    print(mod.name) # Display name
    print(mod.slug) # Slug name
    print(mod.get_supported_game_versions())
    print()

    # Get default file
    print_file(mod.get_default_file())
    # Get latest file for a specified game version
    print_file(mod.get_file_by_game_version("1.7.2"))
    print_file(mod.get_file_by_game_version("1.0.0"))

def print_file(modFile):
    print('Filename: ' + modFile.name)
    print('Date: ' + modFile.date)
    print('Size: ' + format(modFile.length/1024/1024, '.2f') + 'MB')
    print('Release Type: ' + modFile.releaseType.name)
    print('Game Versions: ' + ', '.join(modFile.gameVersions))
    print('URL: ' + modFile.downloadUrl)
    print()

if __name__ == '__main__':
    main()