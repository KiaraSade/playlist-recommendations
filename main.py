# main.py

def recommend_playlist():
    print("Welcome to the Playlist Recommendations app!")
    genre = input("Enter your favorite music genre: ")
    mood = input("Enter your current mood: ")
    
    print(f"\nRecommended Playlist for {genre} music and {mood} mood:")
    
    if genre.lower() == 'pop' and mood.lower() == 'happy':
        print("1. Pop Hits 2022")
        print("2. Happy Vibes")
    elif genre.lower() == 'rock' and mood.lower() == 'calm':
        print("1. Acoustic Rock Favorites")
        print("2. Rock Ballads")
    else:
        print("Sorry, no specific playlist recommendation available. Explore and enjoy!")

# Test the program
recommend_playlist()
