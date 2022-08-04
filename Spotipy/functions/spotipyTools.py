def get_tracks_id(tracks):
  
  track_ids = []
  
  for item in tracks:
    track_ids.append(item['track']['id'])

  return track_ids

def get_date_added(tracks):
  
  dates_added = []
  
  for item in tracks:
    dates_added.append(item['added_at'])

  return dates_added

def get_playlist_info(user_id, playlist_id, sp):
    results = sp.user_playlist_tracks(user_id, playlist_id)
    
    tracks = get_tracks_id(results['items'])
    dates = get_date_added(results['items'])

    while results['next']:
        results = sp.next(results)
        tracks.extend(get_tracks_id(results['items']))
        dates.extend(get_date_added(results['items']))
    return tracks, dates

def get_all_tracks(user_id, playlist_id, sp):

  play_list = sp.user_playlist_tracks(user_id, playlist_id)

  tracks = []

  for item in play_list['tracks']['items']:
    track = item['track']['id']
    tracks.append(track)
  
  return tracks

def get_track_info(track, sp):
  track_info = sp.track(track)

  name = track_info['name']
  artist_name = track_info['artists'][0]['name']
  artist_url = track_info['artists'][0]['external_urls']['spotify']
  album_name = track_info['album']['name']
  album_date = track_info['album']['release_date']
  album_popularity = track_info['popularity']
  track_duration = track_info['duration_ms']

  track_features = sp.audio_features(track)

  danceability = track_features[0]['danceability']
  energy = track_features[0]['energy']
  instrumentalness = track_features[0]['instrumentalness']
  liveness = track_features[0]['liveness']
  tempo = track_features[0]['tempo']

  track_complete_info = [name, artist_name, album_name, album_date, album_popularity, track_duration, danceability, energy, instrumentalness, liveness, tempo, artist_url]

  return track_complete_info

def get_artist_genre(artists, sp):

  genres = []

  for item in artists:
    genres.append(sp.artist(item)['genres'])

  return genres