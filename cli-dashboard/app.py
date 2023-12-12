from Spotify_df import Spotify_df
from rich import print
from rich.layout import Layout
from rich.panel import Panel
from rich.console import Console
from rich.text import Text
from rich.table import Table
from rich.live import Live
from rich.box import Box
from rich.tree import Tree

import os
import termplotlib as tpl
import plotext as plt
import termcharts as tc


spotify_df = Spotify_df()
console = Console(height=55)
layout = Layout(name='root')
popular_songs = Table(title="Top most popular songs of the least popular genres", show_header=True, header_style="bold white on green", expand=True, title_style='bold white on green')
top_popular_artists = Table(title="Top most popular artists", show_header=True, header_style="bold white on green", expand=True, title_style='bold white on green')
top_popular_eminem_songs_tree = Tree(" ")
top_popular_kayne_songs_tree = Tree(" ")


genres, avg_popularities = spotify_df.most_popular_genre(5)
_, count = spotify_df.distribution_of_explicit_songs()
artists, track_name, popularity, track_genre = spotify_df.top_popular_songs_of_less_popular_genre(8)
popular_artists, artists_avg_popularity = spotify_df.top_artist_by_popularity(10)
eminem_track_name, eminem_track_genre = spotify_df.top_popular_songs_by_artist('Eminem',5)
f_cent_track_name, f_cent_track_genre = spotify_df.top_popular_songs_by_artist('50 Cent',5)


for song_name, genre in zip(eminem_track_name, eminem_track_genre):
    top_popular_eminem_songs_tree.add(f"[bold]{song_name}[/bold] ({genre})")

for song_name, genre in zip(f_cent_track_name, f_cent_track_genre):
    top_popular_kayne_songs_tree.add(f"[bold]{song_name}[/bold] ({genre})")
    
    

count = count.__reversed__()

pie_chart_data = dict(zip(['Not explicit', 'Explicit'], count))

os.system('clear')


plt.simple_bar(genres, avg_popularities, width=console.width, title='Top 5 most popular genre')
pie_chart = tc.pie(pie_chart_data, title=' ', rich=True)

layout.split(
    Layout(name='header', size=3),
    Layout(name='main'),
    Layout(name='lower_main')
)
layout['main'].split_row(
    Layout(name="left"),
    Layout(name="right")
)
layout['lower_main'].split_column(
    Layout(name='lupper'),
    Layout(name='llower')
)
layout['right'].split_column(
    Layout(name='rupper'),
    Layout(name='rlower')
)


top_popular_artists.add_column('Artist')
top_popular_artists.add_column('Average popularity')
for artist, a_popularity in zip(popular_artists, artists_avg_popularity):
    top_popular_artists.add_row(f'{artist}', f'{a_popularity}')

popular_songs.add_column('Artist')
popular_songs.add_column('Track name')
popular_songs.add_column('Popularity')
popular_songs.add_column('Track genre')

for artist, name, popularity, genre in zip(artists, track_name, popularity, track_genre):
    popular_songs.add_row(f'{artist}', f'{name}', f'{popularity}', f'{genre}')

layout['header'].update(Panel(Text('Spotify dataframe dashboard', justify='center'), title='Spotify Analysis', style='bold white on green'))
layout['rupper'].update(Panel(top_popular_eminem_songs_tree, title='Top most popular Emimen songs', style='bold white on green'))
layout['rlower'].update(Panel(top_popular_kayne_songs_tree, title='Top most popular 50 cent songs', style='bold white on green'))
layout['left'].update(Panel(pie_chart, title='Explict vs not explicit songs', style='bold white on green'))
layout['lupper'].update(popular_songs)
layout['llower'].update(top_popular_artists)



console.print(layout)
plt.show()

print('ok')