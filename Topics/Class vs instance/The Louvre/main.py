class Painting:
    def __init__(self, title, artist, year):
        self.title = title
        self.artist = artist
        self.year = year

        print(f'"{title}" by {artist} ({year}) hangs in the Louvre.')


painting = Painting(input(), input(), input())
