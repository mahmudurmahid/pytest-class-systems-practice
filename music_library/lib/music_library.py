class MusicLibrary:
    def __init__(self):
        self.tracks = []

    def add(self, track):
        self.tracks.append(track)

    def search_by_title(self, keyword):
        matches = []

        for song in self.tracks:
            if keyword in song.title:
                matches.append(song)
        return matches