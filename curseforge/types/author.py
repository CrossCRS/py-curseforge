class Author:
    def __init__(self, json_data):
        self.id = int(json_data['id'])
        self.user_id = int(json_data['userId'])
        self.twitch_id = int(json_data['twitchId'])
        self.name = json_data['name']
        self.project_title_id = int(json_data['projectTitleId']) if json_data['projectTitleId'] else None
        self.project_title_title = json_data['projectTitleTitle']
        self.url = json_data['url']