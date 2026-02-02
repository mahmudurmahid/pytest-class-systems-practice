from lib.todo import Todo

def test_todo_has_a_task():
    todo = Todo("Buy milk")

    assert todo.task == "Buy milk"

def test_todo_starts_incomplete():
    todo = Todo("Buy milk")

    assert todo.complete is False

def test_mark_complete_sets_complete_to_true():
    todo = Todo("Buy milk")

    todo.mark_complete()

    assert todo.complete is True