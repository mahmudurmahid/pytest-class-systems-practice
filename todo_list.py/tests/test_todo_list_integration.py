from lib.todo_list import TodoList
from lib.todo import Todo

def test_adds_todos_to_list():
    todo_list = TodoList()
    todo_1 = Todo("Buy milk")
    todo_2 = Todo("Walk the dog")

    todo_list.add(todo_1)
    todo_list.add(todo_2)

    assert todo_list.todos == [todo_1, todo_2]

def test_incomplete_returns_only_incomplete_todos():
    todo_list = TodoList()
    todo_1 = Todo("Buy milk")
    todo_2 = Todo("Walk the dog")

    todo_list.add(todo_1)
    todo_list.add(todo_2)

    todo_1.mark_complete()

    assert todo_list.incomplete() == [todo_2]

def test_complete_returns_only_completed_todos():
    todo_list = TodoList()
    todo_1 = Todo("Buy milk")
    todo_2 = Todo("Walk the dog")

    todo_list.add(todo_1)
    todo_list.add(todo_2)

    todo_1.mark_complete()

    assert todo_list.complete() == [todo_1]

def test_give_up_marks_all_todos_complete():
    todo_list = TodoList()
    todo_1 = Todo("Buy milk")
    todo_2 = Todo("Walk the dog")

    todo_list.add(todo_1)
    todo_list.add(todo_2)

    todo_list.give_up()

    assert todo_list.complete() == [todo_1, todo_2]
    assert todo_list.incomplete() == []