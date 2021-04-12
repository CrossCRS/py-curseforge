class Category:
    def __init__(self, json_data):
        self.id = json_data['categoryId']
        self.parent_id = json_data['parentId']
        self.root_id = json_data['rootId']
        self.project_id = json_data['projectId']
        self.avatar_id = json_data['avatarId']
        self.game_id = json_data['gameId']
        self.name = json_data['name']
        self.url = json_data['url']
        self.avatar_url = json_data['avatarUrl']