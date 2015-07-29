class UserInfo():

    def __init__(self, connection):
        self.conn = connection
    def whoami(self):
        return self.conn.get('user/whoami')

class BlockVolume():

    def __init__(self, connection):
        self.conn = connection

    def get_volumes_bulk(self):
        json_data = self.conn.get('block/volumes/bulk')
        return json_data['id']

    def get_volume(self, volume_id):
        return self.conn.get('block/volumes/{0}'.format(volume_id))

class BlockSnapshot ():

    def __init__(self, connection):
        self.conn = connection