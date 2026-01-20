from dataclasses import dataclass

@dataclass
class Track:
    id: int
    album_id : int
    genre_id: int


    def __str__(self):
        return self.id

    def __hash__(self):
        return hash(self.id)