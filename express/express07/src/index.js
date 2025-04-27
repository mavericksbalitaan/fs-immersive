const express = require('express')
const app = express()
const port = 3000
app.use(express.json())

app.get("/", (req, res) => {
  res.send("Hello")
})

// array
const playlists = [
  {
    "id": 1,
    "title": "Chill Vibes",
    "description": "Relaxing tunes to help you unwind after a long day.",
    "creator": "User123",
    "songs": [
      {
        "songId": "s1",
        "title": "Sunset Lover",
        "artist": "Petit Biscuit",
        "duration": 216
      },
      {
        "songId": "s2",
        "title": "Weightless",
        "artist": "Marconi Union",
        "duration": 512
      },
    ]
  },
  {
    "id": 2,
    "title": "Workout Beats",
    "description": "High-energy tracks to keep you pumped during your workout.",
    "creator": "FitnessFanatic",
    "songs": []
  },
  {
    "id": 3,
    "title": "Road Trip Anthems",
    "description": "The ultimate playlist for your next adventure on the road.",
    "creator": "TravelerJane",
    "songs": []
  },
]

app.get("/playlists", (req, res) => {
  res.send(playlists)
})

app.get("/playlists/:id", (req, res) => {
  const { id } = req.params
  const selectedplaylist = playlists.find((item) => item.id == id)
  res.send(selectedplaylist)
})

app.post("/playlists", (req, res) => {
  const { id, title, description, creator } = req.body
  const newplaylist = {
    id, title, description, creator
  }

  playlists.push(newplaylist)
  res.send(newplaylist)
})

app.put("/playlists/:id", (req, res) => {
  const { id } = req.params
  const { title, description, creator } = req.body

  const selectedplaylist = playlists.find((item) => item.id == id)

  selectedplaylist.title = title
  selectedplaylist.description = description
  selectedplaylist.creator = creator

  res.send(selectedplaylist)
})


app.delete("/playlists/:id", (req, res) => {
  const { id } = req.params
  const deletedplaylist = playlists.find((item) => item.id == id);
  console.log(deletedplaylist)

  playlists.splice(playlists.indexOf(deletedplaylist), 1);
  res.send(deletedplaylist)
})

app.get("/playlists/:id/songs", (req, res) => {
  const { id } = req.params
  const selectedplaylist = playlists.find((item) => item.id == id)
  res.send(selectedplaylist.songs)
})

app.post("/playlists/:id/songs", (req, res) => {
  const { id } = req.params;
  const selectedplaylist = playlists.find((item) => item.id == id)

  const { songId, title, artist, duration } = req.body

  const newsong = {
    songId, title, artist, duration
  }

  selectedplaylist.songs.push(newsong)

  res.send(selectedplaylist.songs)
})

app.delete("/playlists/:id/songs/:songId", (req, res) => {
  const { id, songId } = req.params;
  const selectedplaylist = playlists.find((item) => item.id == id)

  const songs = selectedplaylist.songs;

  const deletedSong = songs.find((item) => item.songId == songId)

  songs.splice(songs.indexOf(deletedSong), 1);

  res.send(selectedplaylist.songs)
})

app.listen(port, () => {
  console.log(`Server running at http://127.0.0.1:${port}`)
})

