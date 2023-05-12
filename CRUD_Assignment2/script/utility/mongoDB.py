from pymongo import MongoClient

# Creating instance of mongo client
client = MongoClient("mongodb://intern_23:intern%40123@192.168.0.220:2717/interns_b2_23")
database = client['interns_b2_23']
Students = database['Suneel_Rathod']

# In-memory database
database = []


class MongoUtility():
    def __init__(self):
        """"""

    def insert_record(self, records_to_insert):

    # logic of insertion

    def delete_record(self, recirdid):
# ogic
