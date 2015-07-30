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

class BlockSnapshot():

    def __init__(self, connection):
        self.conn = connection

    def get_snapshots_bulk(self):
        json_data = self.conn.get('block/snapshots/bulk')
        return json_data['id']

    def get_snapshot(self, snapshot_id):
        return self.conn.get('block/snapshots/{0}'.format(snapshot_id))

    def deactivate_snapshot(self, snapshot_id):
        return self.conn.post('block/snapshots/{0}/deactivate'.format(snapshot_id))
