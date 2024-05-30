from main import BooksCollector

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
collector = BooksCollector()  # создаем экземпляр BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self):
        # Проверка добавления двух книг
        collector.add_new_book('Тестовая книга 1')
        collector.add_new_book('Тестовая книга 2')
        assert len(collector.get_books_genre()) == 2

    def test_add_new_book_name_book_more_41_symbols(self):
        # Проверка книги с именем больше 41 символов не добавилась
        collector.add_new_book('Тестовая книга 2Тестовая книга 2Тестовая книга 2Тестовая книга 2')
        assert len(collector.books_genre) == 2

    def test_set_genre_for_book(self):
        # Проверка установки жанра для книги
        collector.set_book_genre('Тестовая книга 1', 'Ужасы')
        assert collector.get_book_genre('Тестовая книга 1') == 'Ужасы'

    def test_get_books_with_specific_genre(self):
        # Проверка получения книг с определенным жанром
        collector.set_book_genre('Тестовая книга 1', 'Ужасы')
        assert collector.get_books_with_specific_genre('Ужасы') == ['Тестовая книга 1']

    def test_get_books_get_dictionary(self):
        # Проверка получения словаря books_genre
        assert collector.get_books_genre() == {'Тестовая книга 1': 'Ужасы', 'Тестовая книга 2': ''}

    def test_get_books_for_children_no_age_rating(self):
        # Проверка получения книг для детей
        collector.add_new_book('Тестовая книга для детей 2')
        collector.set_book_genre('Тестовая книга для детей 2', 'Мультфильмы')
        collector.genre_age_rating = ['Детективы', 'Ужасы']
        assert (collector.get_books_for_children() == ['Тестовая книга для детей 2']
                and len(collector.get_books_for_children()) == 1)

    def test_add_book_in_favorites(self):
        # Проверка добавления книги в Избранное
        collector.add_book_in_favorites('Тестовая книга 1')
        assert 'Тестовая книга 1' in collector.get_list_of_favorites_books()

    def test_add_book_in_favorites_not_add_again(self):
        # Проверка получения списка Избранных книг
        collector.add_book_in_favorites('Тестовая книга 1')
        assert len(collector.get_list_of_favorites_books()) == 1

    def test_delete_book_from_favorites(self):
        # Проверка удаления книги из Избранного
        collector.delete_book_from_favorites('Тестовая книга 1')
        assert 'Тестовая книга 1' not in collector.get_list_of_favorites_books()

