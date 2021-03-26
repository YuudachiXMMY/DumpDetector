
import dataset

class MyDB():
    '''
    '''

    def __init__(self, dbName):
        '''
        '''
        try:
            db = dataset.connect('sqlite:///database/%s.db'%dbName)
        except Exception:
            print("ERROR OCCURRED in Connecting Database")

    def createTable(self, tableName, primary_id=None, primary_type=None):
        '''
        '''
        if primary_id is None and primary_type is None:
            self.db.create_table(tableName)
        elif primary_id is None and not primary_type is None:
            self.db.create_table(tableName, primary_type=primary_type)
        elif not primary_id is None and primary_type is None:
            self.db.create_table(tableName, primary_id=primary_id)

    def getTable(self, tableName):
        '''
        '''
        try:
            return self.db[tableName]
        except Exception:
            return None

    def insert(self, table, dataSrc):
        '''
        '''
        table.insert(dataSrc)

    def getAllSrc(self):
        '''
        '''
        return self.db['data_sources'].all()