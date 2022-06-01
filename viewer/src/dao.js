const {MongoClient, ServerApiVersion} = require("mongodb")
// TODO Figure out how to import sensitive URI info from local
// const {CONNECTION_STRING} = require('./sensitive_info.js')
const client = new MongoClient('')


//# General Operations

function insertDocument(collection, content) {
  client.connect(err => {
    const collection = client.db('Dungeon-Maker').collection(collection)
    return collection.insertOne(content)
  })
}

function getDocument(collection, query = {}) {
    client.connect(err => {
      const collection = client.db('Dungeon-Maker').collection(collection)
      return collection.find(query)
    })
}

function updateDocument(collection, query, newValues = {}) {
    client.connect(err => {
      const collection = client.db('Dungeon-Maker').collection(collection)
      return collection.updateOne(query, newValues)
    })
}

function deleteDocument(collection, query) {
  client.connect(err => {
    const collection = client.db('Dungeon-Maker').collection(collection)
    return collection.deleteOne(query)
  })
}

function getAllDocumentsForCollection(collection) {
  client.connect(err => {
    const collection = client.db('Dungeon-Maker').collection(collection)
    return collection.find({})
  })
}

//# Dungeon
//# {
//#     id: "dungeon-id",
//#     name: "dungeon-name",
//#     map_grid: [[0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1], [0, 1, 0, 0, 0, 1]]
//# }
function getDungeon(query) {
    return getDocument('Dungeon', query)
}

function updateDungeon(query, newValues) {
    return updateDocument('Dungeon', query, newValues)
}

function deleteDungeon(query) {
  return deleteDocument('Dungeon', query)
}

function insertDungeon(content) {
  return insertDocument('Dungeon', content)
}

function getAllDungeons() {
  return getAllDocumentsForCollection('Dungeon')
}

//# Campaign
//# {
//#     id: "campaign-id",
//#     name: "campaign_name",
//#     dungeons: ["dungeon_id_1", "dungeon_id_2","dungeon_id_n",]
//# }

function getCampaign(query) {
    return getDocument('Campaign', query)
}

function updateCampaign(query, newValues) {
    return updateDocument('Campaign', query, newValues)
}

function deleteCampaign(query) {
  return deleteDocument('Campaign', query)
}

function insertCampaign(content) {
  return insertDocument('Campaign', content)
}

function getAllCampaigns() {
  return getAllDocumentsForCollection('Campaign')
}

//# Dungeon_Type
//# {
//#     id: "type-id",
//#     code_alias: "CODE",
//#     build: "build_dungeon_CODE()"
//# }

function getDungeonType(query) {
    return getDocument('Dungeon_Type', query)
}

function updateDungeonType(query, newValues) {
    return updateDocument('Dungeon_Type', query, newValues)
}

function deleteDungeonType(query) {
  return deleteDocument('Dungeon_Type', query)
}

function insertDungeonType(content) {
  return insertDocument('Dungeon_Type', content)
}

function getAllDungeonTypes() {
  return getAllDocumentsForCollection('Dungeon_Type')
}

//# Tile
//# {
//#     id: "tile-id",
//#     name: "tile_name",
//#     code: 999,
//#     src: "filepath-to-src"
//# }

function getTile(query) {
    return getDocument('Tile', query)
}

function updateTile(query, newValues) {
    return updateDocument('Tile', query, newValues)
}

function deleteTile(query) {
  return deleteDocument('Tile', query)
}

function insertTile(content) {
  return insertDocument('Tile', content)
}

function getAllTiles() {
  return getAllDocumentsForCollection('Tile')
}

//# User
//# {
//#     id: "user-id",
//#     username: "username",
//#     password: "password",
//#     campaigns: ["campaign_1", "campaign_2", "campaign_n"],
//#     dungeons: ["dungeon_1", "dungeon_2", "dungeon_3"],
//# }
function getUser(query) {
    return getDocument('User', query)
}

function updateUser(query, newValues) {
    return updateDocument('User', query, newValues)
}

function deleteUser(query) {
  return deleteDocument('User', query)
}

function insertUser(content) {
  return insertDocument('User', content)
}

function getAllUsers() {
  return getAllDocumentsForCollection('User')
}
res = getAllDungeons()
console.log(res)
