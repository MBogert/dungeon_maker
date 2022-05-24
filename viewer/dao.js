// TODO Implement Javascript DAO
const {MongoClient, ServerApiVersion} = require("mongodb")

const connection_string = "mongodb+srv://dungeon_master:35PhOJmulXK34kIC@dungeon-maker.hor9x.mongodb.net/?retryWrites=true&w=majority"


const client = new MongoClient(connection_string, { useNewUrlParser: true, useUnifiedTopology: true, serverApi: ServerApiVersion.v1 })
client.connect(err => {
  const collection = client.db("Dungeon-Maker").collection("Dungeon")
  client.close()
})
