import requests
import json
import pytest
import os
# from dotenv import load_dotenv
# load_dotenv()

apiKey = os.environ.get('apiKey')
baseUrl = 'https://api.musixmatch.com/ws/1.1/'
top10MxArtistChartGET= 'chart.artists.get?page=1&page_size=10&country=mx'
top3MxArtistChartGET= 'chart.artists.get?page=1&page_size=3&country=mx'
artistsAlbumsGET='artist.albums.get?artist_id='

class TestClass:    

    def test_getTop10ArtistsMx(self):
        response = requests.get(f"{baseUrl}{top10MxArtistChartGET}&apikey={apiKey}")
        response.json()['message']['body']['artist_list']
        array = response.json()['message']['body']['artist_list']
        print()
        print("====================TOP 10 ARTISTS====================")
        for artist in array:
            print (artist['artist']['artist_name'])
        assert(response.status_code==200)

    def test_getInformationOfTop3Mx(self):
        print("===============INFO ABOUT TOP 3 ARTISTS===============")
        response = requests.get(f"{baseUrl}{top3MxArtistChartGET}&apikey={apiKey}")
        # dataArtists = json.loads(response.content.decode('utf8'))
        top3Artists = response.json()['message']['body']['artist_list']
        for artist in top3Artists:
            print(artist["artist"]["artist_name"],json.dumps(artist["artist"], indent=4))
        assert(response.status_code==200)

    def test_getAlbumFromLast5ArtistsFromTop10(self):
        print("======ALBUMS OF THE LAST 5 ARTISTS FROM THE TOP 10======")
        response = requests.get(f"{baseUrl}{top10MxArtistChartGET}&apikey={apiKey}")
        array = response.json()['message']['body']['artist_list']
        last3Array = array[5::]
        responseAlbums = None
        for artist in last3Array:
            print(f"Artista: {artist['artist']['artist_name']}")
            responseAlbums = requests.get(f"{baseUrl}{artistsAlbumsGET}{artist['artist']['artist_id']}&apikey={apiKey}")
            for album in responseAlbums.json()['message']['body']['album_list']:
                print (album['album']['album_name'])
            print("----------------------")
        assert(response.status_code==200 and responseAlbums.status_code==200)

