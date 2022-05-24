// TODO Implement Javascript DAO
const {MongoClient, ServerApiVersion} = require("mongodb")

const connection_string = "mongodb+srv://dungeon_master:35PhOJmulXK34kIC@dungeon-maker.hor9x.mongodb.net/?retryWrites=true&w=majority"


const client = new MongoClient(connection_string, { useNewUrlParser: true, useUnifiedTopology: true, serverApi: ServerApiVersion.v1 })
client.connect(err => {
  const collection = client.db("Dungeon-Maker").collection("Dungeon")
  client.close()
})


//# General Operations

//TODO Fix
//function getDatabase() {
//    return orders.find(query)
//    return
//}

function insertDocument(collection, content) {
    return collection.insertOne(content)
}

function getDocument(collection, query = {}) {
    return collection.findOne(query)
}

function updateDocument(collection, query, newValues = {}) {
    return collection.updateOne(query, newValues)
}

function deleteDocument(collection, query) {
    return collection.deleteOne(query)
}

function getAllDocumentsForCollection(collection) {
    return collection.find({})
}

function getCollection(name) {
    return 
}

//# Dungeon
//# {
//#     id: "dungeon-id",
//#     name: "dungeon-name",
//#     map_grid: [[0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1]]
//# }
function getDungeon(query) {
    return getDocument(query)
}

function updateDungeon(query, newValues) {
    return 
}

function deleteDungeon(query, newValues) {
}

function insertDungeon(content) {
}

function getAllDungeons() {
}

//# Campaign
//# {
//#     id: "campaign-id",
//#     name: "campaign_name",
//#     dungeons: ["dungeon_id_1", "dungeon_id_2","dungeon_id_n",]
//# }

def get_campaign(query)

def delete_campaign(query)

def update_campaign(query, newValues)

def insert_campaign(content)

def get_all_campaigns()

//# Dungeon_Type
//# {
//#     id: "type-id",
//#     code_alias: "CODE",
//#     build: "build_dungeon_CODE()"
//# }

def get_dungeon_type(query)


def delete_dungeon_type(query)


def update_dungeon_type(query, newValues)


def insert_dungeon_type(content)

def get_all_dungeon_types()

//# Tile
//# {
//#     id: "tile-id",
//#     name: "tile_name",
//#     code: 999,
//#     src: "filepath-to-src"
//# }

def get_tile(query)


def delete_tile(query)


def update_tile(query, newValues)


def insert_tile(content)

def get_all_tiles()

//# User
//# {
//#     id: "user-id",
//#     username: "username",
//#     password: "password",
//#     campaigns: ["campaign_1", "campaign_2", "campaign_n"],
//#     dungeons: ["dungeon_1", "dungeon_2", "dungeon_3"],
//# }
def insert_user(content)

def update_user(query, newValues)

def delete_user(query)

def get_user(query)

def get_all_users()