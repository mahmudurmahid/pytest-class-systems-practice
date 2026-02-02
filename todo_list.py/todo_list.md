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
class TodoList:
    def __init__(self):
        pass

    def add(self, todo):
        # Parameters:
        #   todo: an instance of Todo
        # Returns:
        #   Nothing
        # Side-effects:
        #   Adds the todo to the list of todos
        pass

    def incomplete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are not complete
        pass

    def complete(self):
        # Returns:
        #   A list of Todo instances representing the todos that are complete
        pass

    def give_up(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Marks all todos as complete
        pass


class Todo:
    # Public Properties:
    #   task: a string representing the task to be done
    #   complete: a boolean representing whether the task is complete

    def __init__(self, task):
        # Parameters:
        #   task: a string representing the task to be done
        # Side-effects:
        #   Sets the task property
        #   Sets the complete property to False
        pass

    def mark_complete(self):
        # Returns:
        #   Nothing
        # Side-effects:
        #   Sets the complete property to True
        pass

```

## 3. Create Examples as Integration Tests

_Create examples of the classes being used together in different situations and
combinations that reflect the ways in which the system will be used._

```python
"""
Given an empty todo list
When we add two todos
We see those todos reflected in the list
"""
todo_list = TodoList()
todo_1 = Todo("Buy milk")
todo_2 = Todo("Walk the dog")

todo_list.add(todo_1)
todo_list.add(todo_2)

todo_list.todos  # => [todo_1, todo_2]

"""
Given a todo list with two todos
And one todo is marked complete
When we ask for incomplete todos
We see only the incomplete todo
"""
todo_list = TodoList()
todo_1 = Todo("Buy milk")
todo_2 = Todo("Walk the dog")

todo_list.add(todo_1)
todo_list.add(todo_2)

todo_1.mark_complete()

todo_list.incomplete()  # => [todo_2]

"""
Given a todo list with two todos
And one todo is marked complete
When we ask for complete todos
We see only the completed todo
"""
todo_list = TodoList()
todo_1 = Todo("Buy milk")
todo_2 = Todo("Walk the dog")

todo_list.add(todo_1)
todo_list.add(todo_2)

todo_1.mark_complete()

todo_list.complete()  # => [todo_1]

"""
Given a todo list with multiple incomplete todos
When we give up
All todos are marked as complete
"""
todo_list = TodoList()
todo_1 = Todo("Buy milk")
todo_2 = Todo("Walk the dog")

todo_list.add(todo_1)
todo_list.add(todo_2)

todo_list.give_up()

todo_list.complete()    # => [todo_1, todo_2]
todo_list.incomplete()  # => []

```

## 4. Create Examples as Unit Tests

_Create examples, where appropriate, of the behaviour of each relevant class at
a more granular level of detail._

```python
"""
Given a todo with a task
We see the task reflected in the task property
"""
todo = Todo("Buy milk")

todo.task  # => "Buy milk"

"""
Given a new todo
It is incomplete by default
"""
todo = Todo("Buy milk")

todo.complete  # => False

"""
Given an incomplete todo
When we mark it as complete
The complete property becomes True
"""
todo = Todo("Buy milk")

todo.mark_complete()

todo.complete  # => True

```

_Encode each example as a test. You can add to the above list as you go._

## 5. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green,
refactor to implement the behaviour._
