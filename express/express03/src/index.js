const express = require('express')
const app = express()

app.use(express.json())

const port = 3000;

const books = [
  {
    id: 1,
    title: "To Kill a Mockingbird",
    author: "Harper Lee"
  },
  {
    id: 2,
    title: "1984",
    author: "George Orwell"
  },
  {
    id: 3,
    title: "The Great Gatsby",
    author: "F. Scott Fitzgerald"
  }
];

// root route
app.get("/", (req, res) => {
  res.send("Hello World")
})

// retrieve a list of all books
app.get("/books", (req, res) => {
  res.send(books)
})

// retrieve details of a specific book
app.get("/books/:id", (req, res) => {
  const { id } = req.params
  const book = books.find((book) => book.id == id)
  res.send(book)
})

// add a new book to the collection
app.post("/books", (req, res) => {
  const { id, title, author } = req.body
  books.push({ id, title, author })

  // return the list of books
  res.send(books)
})

// update details of a book by id
app.put("/books/:id", (req, res) => {
  const { id, title, author } = req.body

  // finding the specific book
  const book = books.find((book) => book.id == id)

  // updating the book
  book.title = title
  book.author = author

  // return the list of books
  res.status(201).send(book)
})

// delete a book by id
app.delete("/books/:id", (req, res) => {
  const { id } = req.params
  // finding the specific book
  const book = books.find((book) => book.id == id)

  // removing the specific book from the collection
  books.splice(books.indexOf(book),1);

  // return the list of books
  res.send(books)
})

app.listen(port, () => {
  console.log("Server is running on http://localhost:3000")
})
