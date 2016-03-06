#!/usr/bin/env python

class BlockVolume():

    def __init__(self, connection):
        self.conn = connection

    def get_volumes_bulk(self):
        json_data = self.conn.get('types/Volume/instances')
        return json_data['vtreeId']