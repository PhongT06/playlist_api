

class PlaylistManager:
    def __init__(self):
        self.playlists = {}
        self.songs = {}
        self.user_preferences = {}

    ### creating a new playlist ###

    def create_playlist(self, name, description=""):
        playlist_id = len(self.playlists) + 1
        self.playlists[playlist_id] = {'name': name, 'description': description, 'songs': []}
        return playlist_id
    
    ### getting details of a playlist ###

    def get_playlist(self, playlist_id):
        if playlist_id in self.playlists:
            return self.playlists[playlist_id]
        else:
            return None
        
    ### updating a playlist ###    

    def update_playlist(self, playlist_id, name=None, description=None):
        if playlist_id in self.playlists:
            if name:
                self.playlists[playlist_id]['name'] = name
            if description:
                self.playlists[playlist_id]['description'] = description
        else:
            return None
            
    ### deleting a playlist ###

    def delete_playlist(self, playlist_id):
        if playlist_id in self.playlists:
            del self.playlists[playlist_id] 
        else:
            return None  

    ### adding a song to playlist ###

    def add_song_to_playlist(self, playlist_id, song_id):
        if playlist_id in self.playlists and song_id in self.songs:
            self.playlists[playlist_id]['songs'].append(song_id)
        else:
            return None

    ### removing a song from playlist ###

    def remove_song_from_playlist(self, playlist_id, song_id):
        if playlist_id in self.playlists and song_id in self.songs:
            self.playlists[playlist_id]['songs'].remove(song_id)
        else:
            return None

    ### searching for a song ###

    def search_song(self, query):
        results = []
        for song_id, song_details in self.songs.items():
            if query.lower() in song_details['title'].lower() or query.lower() in song_details['artist'].lower():
                results.append(song_details)
        return results
    
    # ### set user preferences ###

    # def set_user_preferences(self, user_id, preferences):
    #     self.user_preferences[user_id] = preferences

    # ### get user preferences ###

    # def get_user_preferences(self, user_id):
    #     return self.user_preferences.get(user_id, None)

