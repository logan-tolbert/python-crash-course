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
    
while True:
    artist = input("Enter artist name: ")
    if artist == "quit":
        break
    album = input("Enter album name: ")
    if album == "quit":
        break
    response = input("Would you like to enter the number of tracks? ")
    if response == "quit":
        break
    if response == "yes":
        tracks = input("Enter number of tracks? ")
        if tracks == "quit":
            break
        print(make_album(artist, album, int(tracks)))
   
    elif response != "yes" or response == 'quit':
        print(make_album(artist, album))
                     
