# qa_python
## conftest.py
    В фикстуры вынесены:
        1) Создание экземпляра класса TestBooksCollector
        2) Генерация спика тестовых книг list_of_test_books

## test.py
    Файл с тестовым классом TestBooksCollector. 
    Релизованны тесты:
        1) test_add_new_book_add_two_books - Проверка добавления книг.
        2) test_add_new_book_add_same_book_twice - Нельзя добавить одну и ту же книгу дважды.
        3) test_set_book_rating_book_is_not_exist - Нельзя выставить рейтинг книге, которой нет в списке.
        4) test_set_book_rating_less_than_one - Нельзя выставить рейтинг меньше 1.
        5) test_set_book_rating_more_than_ten - Нельзя выставить рейтинг больше 10.
        6) test_get_book_rating_book_is_not_exist - У не добавленной книги нет рейтинга.
        7) test_get_books_with_specific_rating_get_books_with_rating_two - Получение списка книг с рейтингом 2
        8) test_get_books_with_specific_rating_no_book_with_rating_four - Нет книг с рейтингом 4
        9) test_add_book_in_favorites_add_new_book - Добавление книги в избранное.
        10) test_add_book_in_favorites_book_is_not_in_books_rating - Нельзя добавить книгу в избранное, если её нет в словаре books_rating.
        11) test_delete_book_from_favorites_delete_book - Проверка удаления книги из избранного.