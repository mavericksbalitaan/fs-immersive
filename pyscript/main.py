from pyscript import document
from pyscript.web import h2, page

# def sample:
#     body = document.body
#


h1 = document.querySelector("h1")
h1.style.color = "red"

sample = h2()
sample.content = "This is an h2"

page.append(sample)
