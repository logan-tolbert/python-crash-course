def make_album(artist_name, album_title, num_of_tracks=None):
    if num_of_tracks:
        album = {
            "Artist name": artist_name,
            "Album title": album_title,
            "Tracks": num_of_tracks
                   }
        return album
    else:
        album = {
            "Artist name": artist_name,
            "Album title": album_title
            }
        return album

album_info1 = make_album("Have Heart", "The Things We Carry", 11)
album_info2 = make_album("Knocked Loose", "Laugh Tracks", 11)
album_info3 = make_album("Metallica", "Master of Puppets", 8)

print(album_info1)
print(album_info2)
print(album_info3)