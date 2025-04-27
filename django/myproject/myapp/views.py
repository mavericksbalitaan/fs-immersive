from django.shortcuts import render, HttpResponse

# Create your views here.


def home(request):
    return HttpResponse("Hello World!")


posts = [
    {
        "title": "My First Post",
        "content": "This is the content of my first post. Welcome to my blog!"
    },
    {
        "title": "Learning Django",
        "content": "Django is a powerful web framework for building web applications quickly."
    },
    {
        "title": "Python Tips",
        "content": "Here are some tips for writing clean and efficient Python code."
    },
    {
        "title": "Web Development",
        "content": "Web development involves both frontend and backend technologies."
    },
    {
        "title": "Django Models",
        "content": "Django models are used to define the structure of your database tables."
    }
]


def about(request):
    return render(request, "about.html", {"posts": posts})
