from datetime import date
from metadata import *


class List(object):
    def __init__(self, data):
        self.id = data['id']
        self.name = data['name']
        self.author = data['author']
        self.created = data['created']
        
    def get_created_date(self):
        return date.fromtimestamp(self.created / 1000)


class Detail(List):
    def __init__(self, data):
        import tracks

        super(Detail, self).__init__(data)
        self.tracks = [tracks.List(x) for x in data['tracks']]


class Playlists(MetadataList, MetadataDetail):
    url_base = 'playlists'
    list_class = List
    detail_class = Detail

    def top(self):
        raise NotImplementedError

    def featured(self):
        return self.list('featured')