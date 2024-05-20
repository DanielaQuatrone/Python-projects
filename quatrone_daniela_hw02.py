import json

list_of_movie_dict = []

with open('netflix_titles.tsv') as file:
    content = file.read().split('\n')

for movie in content[1:]:
    movies = movie.split('\t')
    movie_dict = {}
    movie_dict['title'] = movies[content[0].split('\t').index('PRIMARYTITLE')]
    movie_dict['directors'] = movies[content[0].split('\t').index('DIRECTOR')].replace(', ', ',').split(',')
    movie_dict['cast'] = movies[content[0].split('\t').index('CAST')].replace(', ', ',').split(',')
    movie_dict['genres'] = movies[content[0].split('\t').index('GENRES')].replace(', ', ',').split(',')
    movie_dict['decade'] = movies[content[0].split('\t').index('STARTYEAR')][:3]+'0'
    for key, value in movie_dict.items():
        if value == ['']:
            movie_dict[key] = []
    list_of_movie_dict.append(movie_dict)  

with open('hw02_output.json', mode='w', encoding='utf-8') as file:
    json.dump(list_of_movie_dict, file, ensure_ascii=False, indent=5)
