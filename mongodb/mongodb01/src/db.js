const mongoose = require("mongoose")

const uri = "mongodb://localhost:27017/booksDB"

let db;

async function connectToDB() {
  try {
    await mongoose.connect(uri)
    console.log("Connected to database")
  } catch (error) {
    console.log(error)
  }

  return db
}

module.exports = { connectToDB }
