from lib.diary import Diary
from lib.diary_entry import DiaryEntry

def test_diary_counts_words_in_all_entries():
    diary = Diary()
    diary.add(DiaryEntry("title1", "one two"))
    diary.add(DiaryEntry("title2", "three four five"))
    assert diary.count_words() == 5
