#coding=utf-8
import unittest

from flask_pymongo import MongoClient

#connection to mongo
mongo = MongoClient()

# get a handle to the budzets database
db = mongo.budzets

class BudzetsImportingTestCases(unittest.TestCase):
    
    def setUp(self):
        pass