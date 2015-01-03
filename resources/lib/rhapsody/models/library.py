class Library(object):
    def __init__(self, api):
        self._api = api

    def artists(self, limit=None, offset=None):
        from rhapsody.models import artists

        return self._api.get_list(artists.List, 'me/library/artists', limit, offset, cache_timeout=None)

    def albums(self, limit=None, offset=None):
        from rhapsody.models import albums

        return self._api.get_list(albums.List, 'me/library/albums', limit, offset, cache_timeout=None)

    def tracks(self, limit=None, offset=None):
        from rhapsody.models import tracks

        return self._api.get_list(tracks.List, 'me/library/tracks', limit, offset, cache_timeout=None)

    def recent_artists(self, limit=None, offset=None):
        from rhapsody.models import artists

        return self._api.get_list(artists.List, 'me/recent/artists', limit, offset, cache_timeout=None)

    def recent_tracks(self, limit=None, offset=None):
        from rhapsody.models import tracks

        return self._api.get_list(tracks.List, 'me/listens', limit, offset, cache_timeout=None)

    def playlists(self, limit=None, offset=None):
        from rhapsody.models import playlists

        return self._api.get_list(playlists.List, 'me/playlists', limit, offset, cache_timeout=None)

    def playlist(self, playlist_id):
        from rhapsody.models import playlists

        return self._api.get_detail(playlists.Detail, 'me/playlists', playlist_id, cache_timeout=None)

    def favorites(self, limit=None, offset=None):
        from rhapsody.models import tracks

        return self._api.get_list(tracks.Detail, 'me/favorites', limit, offset, cache_timeout=None)