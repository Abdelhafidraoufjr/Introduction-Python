import math

class Pagination:

    def __init__(self, items=None, page_size: int = 10):
        if page_size <= 0:
            raise ValueError("page_size must be positive")

        self.items = list(items) if items is not None else []
        self.page_size = page_size
        self.current_idx = 0  # 0‑based page index
        self._update_total_pages()

    def _update_total_pages(self):
        self.total_pages = max(1, math.ceil(len(self.items) / self.page_size))

    def _clamp_current_idx(self):
        self.current_idx = max(0, min(self.current_idx, self.total_pages - 1))


    def get_visible_items(self):
        start = self.current_idx * self.page_size
        end = start + self.page_size
        return self.items[start:end]

    def go_to_page(self, page_num: int):

        if page_num < 1:
            raise ValueError("Page numbers start at 1.")
        self.current_idx = min(page_num - 1, self.total_pages - 1)

    def first_page(self):
        self.current_idx = 0
        return self

    def last_page(self):
        self.current_idx = self.total_pages - 1
        return self

    def next_page(self):
        if self.current_idx < self.total_pages - 1:
            self.current_idx += 1
        return self

    def previous_page(self):
        if self.current_idx > 0:
            self.current_idx -= 1
        return self

    def __str__(self):
        return "\n".join(str(item) for item in self.get_visible_items())

if __name__ == "__main__":
    alphabet_list = list("abcdefghijklmnopqrstuvwxyz")
    p = Pagination(alphabet_list, 4)

    print(p.get_visible_items())

    p.next_page()
    print(p.get_visible_items())

    p.last_page()
    print(p.get_visible_items())

    p.go_to_page(10)
    print(p.current_idx + 1)


    try:
        p.go_to_page(0)
    except ValueError as err:
        print("Caught expected exception:", err)
