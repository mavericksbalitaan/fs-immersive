const express = require('express')
const app = express()

app.use(express.json())

const { connectToDB } = require('./db')

const Book = require('../src/models/books')

const port = 3000

connectToDB();

app.get("/books", async (req, res) => {
  const books = await Book.find()
  res.send(books)
})

app.post("/books", async (req, res) => {
  const { title, author } = req.body;

  const newBook = new Book({
    title: title, author: author
  })


  try {
    await newBook.save()
    res.send(newBook)
  } catch (error) {
    console.log(error)
  }
})

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`)
})
