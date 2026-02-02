# ToDo List Multi-Class Planned Design Recipe

## 1. Describe the Problem

As a user
So that I can keep track of things I need to do
I want to add a new todo to my todo list.

As a user
So that I know what still needs to be done
I want to see a list of all incomplete todos.

As a user
So that I can see what I have already finished
I want to see a list of all completed todos

As a user
So that I can mark work as finished
I want to mark a todo as complete.

As a user
So that I can quickly finish everything when I stop working
I want to mark all todos as complete at once.

As a user
So that I can represent a task I need to do
I want to create a todo with a task description that starts as incomplete.

As a user
So that todos reflect real work to be done
I want new todos to be incomplete by default.

## 2. Design the Class System

_Consider diagramming out the classes and their relationships. Take care to
focus on the details you see as important, not everything. The diagram below
uses asciiflow.com but you could also use excalidraw.com, draw.io, or miro.com_

```
┌──────────────────────────────────┐
│ TodoList                         │
│                                  │
│ - todos                          │
│                                  │
│ - add(todo)                      │
│   => nothing                     │
│                                  │
│ - incomplete()                   │
│   => [Todo, Todo, ...]           │
│                                  │
│ - complete()                     │
│   => [Todo, Todo, ...]           │
│                                  │
│ - give_up()                      │
│   => nothing                     │
└───────────────┬──────────────────┘
                │
                │ owns a list of
                ▼
┌────────────────────────────────┐
│ Todo(task)                     │
│                                │
│ - task                         │
│ - complete                     │
│                                │
│ - mark_complete()              │
│   => nothing                   │
└────────────────────────────────┘

```

_Also design the interface of each class in more detail._

```python
class MusicLibrary:
    # User-facing properties:
    #   tracks: list of instances of Track

    def __init__(self):
        pass # No code here yet

    def add(self, track):
        # Parameters:
        #   track: an instance of Track
        # Side-effects:
        #   Adds the track to the tracks property of the self object
        pass # No code here yet

    def search_by_title(self, keyword):
        # Parameters:
        #   keyword: string
        # Returns:
        #   A list of the Track objects that have titles that include the keyword
        pass # No code here yet


class Track:
    # User-facing properties:
    #   title: string
    #   artist: string

    def __init__(self, title, artist):
        # Parameters:
        #   title: string
        #   artist: string
        # Side-effects:
        #   Sets the title and artist properties
        pass # No code here yet

    def format(self):
        # Returns:
        #   A string of the form "TITLE by ARTIST"
        pass # No code here yet

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
# EXAMPLE

"""
Given a library
When we add two tracks
We see those tracks reflected in the tracks list
"""
library = MusicLibrary()
track_1 = Track("Carte Blanche", "Veracocha")
track_2 = Track("Synaesthesia", "The Thrillseekers")
library.add(track_1)
library.add(track_2)
library.tracks # => [track_1, track_2]
```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
# EXAMPLE

"""
Given a track with a title and an artist
We see the title reflected in the title property
"""
track = Track("Carte Blanche", "Veracocha")
track.title # => "Carte Blanche"
```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
