from math import ceil
from typing import List


class PhotoAlbum:
    PHOTOS_PER_PAGE: int = 4
    DASHES: int = 11 * "-"

    def __init__(self, pages):
        self.pages: int = pages
        self.photos: List[List[str]] = [[] for _ in range(self.pages)]

    @classmethod
    def from_photos_count(cls, photo_count: int):
        pages_count = ceil(photo_count / PhotoAlbum.PHOTOS_PER_PAGE)
        return cls(pages_count)

    def add_photo(self, label: str) -> str:  # [["steak", "mountain", "river"], [], []]
        for page in range(self.pages):
            if len(self.photos[page]) < self.PHOTOS_PER_PAGE:
                slot = len(self.photos[page]) + 1
                self.photos[page].append(label)
                return f"{label} photo added successfully on page {page + 1} slot {slot}"

        return "No more free slots"

    def display(self) -> str:
        result = [
            self.DASHES,
        ]

        for page in self.photos:
            result.append(("[] " * len(page)).rstrip())
            result.append(self.DASHES)

        return "\n".join(result)



album = PhotoAlbum(2)

print(album.add_photo("baby"))
print(album.add_photo("first grade"))
print(album.add_photo("eight grade"))
print(album.add_photo("party with friends"))
print(album.photos)
print(album.add_photo("prom"))
print(album.add_photo("wedding"))

print(album.display())