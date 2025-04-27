const express = require('express')
const app = express()

app.use(express.json())
const port = 3000;
// initialize a url database object or use an array if you prefer e.g. const urls =[ [shortCode, longURL], [shortCode, longURL], ...]
const urls = {}

// extra route to show what's inside the urls db object
app.get("/", (req, res) => {
  res.send(urls)
})

// function to generate a short code
const shortener = () => {
  const randomCharacters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghiklmnopqrstuvwxyz1234567890"
  const shortCodeLength = 6;
  let shortCode = ""
  for (let i = 0; i < shortCodeLength; i++) {
    // get a random character to add to the shortCode string
    shortCode += randomCharacters.charAt(Math.floor(Math.random() * randomCharacters.length))
  }
  return shortCode
}

// first route needed
app.post("/shorten", (req, res) => {
  const { longURL } = req.body
  // generate a shortCode to use
  const shortenCode = shortener()
  urls[shortenCode] = longURL
  res.send(shortenCode)
})

// second route needed
app.get("/:shortCode", (req, res) => {
  const { shortCode } = req.params
  const longURL = urls[shortCode]
  if (longURL) {
    res.redirect(longURL)
  } else {
    res.send("ShortCode does not exists in URLs")
  }
})

app.listen(port, () => {
  console.log(`Server is running at http://localhost:${port}`)
})
