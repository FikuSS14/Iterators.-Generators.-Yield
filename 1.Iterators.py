class FlatIterator:
    def __init__(self, multi_list):
        """Определяет атрибут для хранения списка списков"""
        self.multi_list = multi_list

    def __iter__(self):
        """Определяет атрибуты для итерации по списку"""
        self.list_iter = iter(self.multi_list)
        self.nested_list = []
        self.cursor = 0
        return self

    def __next__(self):
        """Определяет и возвращает следующий элемент списка списков"""
        while True:
            if self.cursor >= len(self.nested_list):
                try:
                    self.nested_list = next(self.list_iter)
                    self.cursor = 0
                except StopIteration:
                    raise StopIteration

            if self.cursor < len(self.nested_list):
                item = self.nested_list[self.cursor]
                self.cursor += 1
                return item

            self.cursor += 1


def test_1():
    list_of_lists_1 = [["a", "b", "c"], ["d", "e", "f", "h", False], [1, 2, None]]

    for flat_iterator_item, check_item in zip(
        FlatIterator(list_of_lists_1),
        ["a", "b", "c", "d", "e", "f", "h", False, 1, 2, None],
    ):
        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "h",
        False,
        1,
        2,
        None,
    ]


if __name__ == "__main__":
    test_1()
