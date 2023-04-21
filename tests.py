class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector, list_of_test_books):

        collector.add_new_book(list_of_test_books[0])
        collector.add_new_book(list_of_test_books[1])

        assert len(collector.get_books_rating()) == 2

    def test_add_new_book_add_same_book_twice(self, collector, list_of_test_books):

        collector.add_new_book(list_of_test_books[0])
        collector.add_new_book(list_of_test_books[0])

        assert len(collector.get_books_rating()) == 1

    def test_set_book_rating_book_is_not_exist(self, collector, list_of_test_books):

        collector.set_book_rating(list_of_test_books[0], 10)

        assert collector.get_book_rating(list_of_test_books[0]) is None

    def test_set_book_rating_less_than_one(self, collector, list_of_test_books):

        collector.add_new_book(list_of_test_books[0])
        collector.set_book_rating(list_of_test_books[0], 0)

        assert collector.get_book_rating(list_of_test_books[0]) == 1

    def test_set_book_rating_more_than_ten(self, collector, list_of_test_books):

        collector.add_new_book(list_of_test_books[0])
        collector.set_book_rating(list_of_test_books[0], 0)

        assert collector.get_book_rating(list_of_test_books[0]) == 1

    def test_get_book_rating_book_is_not_exist(self, collector, list_of_test_books):

        assert collector.get_book_rating(list_of_test_books[0]) is None

    def test_get_books_with_specific_rating_get_books_with_rating_two(self, collector, list_of_test_books):

        collector.add_new_book(list_of_test_books[0])
        collector.set_book_rating(list_of_test_books[0], 3)
        collector.add_new_book(list_of_test_books[1])
        collector.set_book_rating(list_of_test_books[1], 2)
        collector.add_new_book(list_of_test_books[2])
        collector.set_book_rating(list_of_test_books[2], 2)

        assert len(collector.get_books_with_specific_rating(2)) == 2

    def test_get_books_with_specific_rating_no_book_with_rating(self, collector, list_of_test_books):

        collector.add_new_book(list_of_test_books[0])
        collector.set_book_rating(list_of_test_books[0], 3)
        collector.add_new_book(list_of_test_books[1])
        collector.set_book_rating(list_of_test_books[1], 2)

        assert len(collector.get_books_with_specific_rating(4)) == 0

    def test_add_book_in_favorites_add_new_book(self, collector, list_of_test_books):

        collector.add_new_book(list_of_test_books[0])
        collector.add_book_in_favorites(list_of_test_books[0])

        assert list_of_test_books[0] in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_book_is_not_in_books_rating(self, collector, list_of_test_books):

        collector.add_book_in_favorites(list_of_test_books[0])

        assert list_of_test_books[0] not in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites_delete_book(self, collector, list_of_test_books):

        collector.add_new_book(list_of_test_books[0])
        collector.add_book_in_favorites(list_of_test_books[0])
        collector.delete_book_from_favorites(list_of_test_books[0])

        assert list_of_test_books[0] not in collector.get_list_of_favorites_books()
