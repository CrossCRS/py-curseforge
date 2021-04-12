class Category:
    def __init__(self, json_data):
        self.id = int(json_data['categoryId'])
        self.parent_id = int(json_data['parentId'])
        self.root_id = int(json_data['rootId'])
        self.project_id = int(json_data['projectId'])
        self.avatar_id = int(json_data['avatarId'])
        self.game_id = int(json_data['gameId'])
        self.name = json_data['name']
        self.url = json_data['url']
        self.avatar_url = json_data['avatarUrl']