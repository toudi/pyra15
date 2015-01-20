from abstractmodel import AbstractModel
from http.client import HTTPConnection
from json import loads
from json import dumps


class RestModel(AbstractModel):
    def __init__(self, *args, **kwargs):
        super(RestModel, self).__init__()
        # self.items_for_sync = set()
        self.conn = HTTPConnection(self.host)
        self.load_items()

    def load_items(self, is_update=False):
        self.conn.request('GET', '/%s' % self.service)
        try:
            self.items = loads(self.conn.getresponse().read().decode('utf-8'))
            if is_update:
                start = self.index(0, 0)
                finish = self.index(self.rowCount(None), 0)
                self.dataChanged.emit(start, finish)
        except ValueError:
            pass
        self.conn.close()

    # def setData(self, index, value, role):
    #     if super(RestModel, self).setData(index, value, role) == True:
    #         self.items_for_sync.add(index.row())
    #     return True

    def sync(self):
        # items = [self.items[row] for row in self.items_for_sync]
        items = self.items
        self.conn.connect()
        self.conn.request('UPDATE', '/%s' % self.service, dumps(items))
        # self.items_for_sync = set()
        self.conn.close()
        self.load_items(is_update=True)

    def removeRows(self, row, count, parent):
        i = 0
        while i < count:
            id = self.items[row]['id']
            self.conn.connect()
            self.conn.request('DELETE', '/%s/%d' % (self.service, id))
            i += 1
        self.conn.close()
        return super(RestModel, self).removeRows(row, count, parent)
