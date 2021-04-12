class Author:
    def __init__(self, json_data):
        self.id = json_data['id']
        self.user_id = json_data['userId']
        self.twitch_id = json_data['twitchId']
        self.name = json_data['name']
        self.project_title_id = json_data['projectTitleId']
        self.project_title_title = json_data['projectTitleTitle']
        self.url = json_data['url']