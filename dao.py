import json
# Get your own secure-url :P
import sensitive_info as info
# TODO
# Implement a python DAO to Mongo

from pymongo import MongoClient


# General Operations

def get_database():
    return MongoClient(info.CONN_STRING).get_database('Dungeon-Maker')


def insert_document(collection, content):
    return get_database()[collection].insert_one(json.loads(content))


def get_document(collection, query={}):
    return get_database()[collection].find_one(query)


def update_document(collection, query, new_values={}):
    return get_database()[collection].update_one(query, new_values)


def delete_document(collection, query):
    return get_database()[collection].delete_one(query)


def get_all_documents_for_collection(collection_name):
    return get_database()[collection_name].find()


# Dungeon
# {
#     id: "dungeon-id",
#     name: "dungeon-name",
#     map_grid: [[0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1]]
# }
def get_dungeon(query):
    return get_document('Dungeon', query)


def update_dungeon(query, new_values):
    return update_document('Dungeon', query, new_values)


def delete_dungeon(query, new_values):
    return delete_document('Dungeon', query)


def insert_dungeon(content):
    return insert_document('Dungeon', content)


def get_all_dungeons():
    return get_all_documents_for_collection('Dungeon')


# Campaign
# {
#     id: "campaign-id",
#     name: "campaign_name",
#     dungeons: ["dungeon_id_1", "dungeon_id_2","dungeon_id_n",]
# }

def get_campaign(query):
    return get_document('Campaign', query)


def delete_campaign(query):
    return delete_document('Campaign', query)


def update_campaign(query, new_values):
    return update_document('Campaign', query, new_values)


def insert_campaign(content):
    return insert_document('Campaign', content)


def get_all_campaigns():
    return get_all_documents_for_collection('Campaign')


# Dungeon_Type
# {
#     id: "type-id",
#     code_alias: "CODE",
#     build: "build_dungeon_CODE()"
# }

def get_dungeon_type(query):
    return get_document('Dungeon_Type', query)


def delete_dungeon_type(query):
    return delete_document('Dungeon_Type', query)


def update_dungeon_type(query, new_values):
    return update_document('Dungeon_Type', query, new_values)


def insert_dungeon_type(content):
    return insert_document('Dungeon_Type', content)


def get_all_dungeon_types():
    return get_all_documents_for_collection('Dungeon_Type')


# Tile
# {
#     id: "tile-id",
#     name: "tile_name",
#     code: 999,
#     src: "filepath-to-src"
# }

def get_tile(query):
    return get_document('Tile', query)


def delete_tile(query):
    return delete_document('Tile', query)


def update_tile(query, new_values):
    return update_document('Tile', query, new_values)


def insert_tile(content):
    return insert_document('Tile', content)


def get_all_tiles():
    return get_all_documents_for_collection('Tile')


# User
# {
#     id: "user-id",
#     username: "username",
#     password: "password",
#     campaigns: ["campaign_1", "campaign_2", "campaign_n"],
#     dungeons: ["dungeon_1", "dungeon_2", "dungeon_3"],
# }
def insert_user(content):
    return insert_document('User', content)


def update_user(query, new_values):
    return update_document('User', query, new_values)


def delete_user(query):
    return delete_document('User', query)


def get_user(query):
    return get_document('User', query)


def get_all_users():
    return get_all_documents_for_collection('User')
