from lib.todo_list import TodoList
from lib.todo import Todo

def test_todo_list_starts_with_empty_list():
    todo_list = TodoList()

    assert todo_list.todos == []

def test_add_adds_a_todo_to_the_list():
    todo_list = TodoList()
    todo = Todo("Buy milk")

    todo_list.add(todo)

    assert todo_list.todos == [todo]