from web1_task import adventure_movie

from web2_task import top_movie
import json
screpped=adventure_movie()
movie_year=top_movie(screpped)


def group_by_decade(movie):
    movie_dec={}
    list1=[]
    for year in movie:
        mod=year%10
        decade=year-mod
        if decade not in list1:
            list1.append(decade)
    list1.sort()
    for i in list1:
        movie_dec[i]=[]
    for i in movie_dec:
        dec=i+9
        for x in movie:
            if x<=dec and x>=i:
                for v in movie[x]:
                    movie_dec[i].append(v)
        with open("top_movie_3.json","w") as f:
            json.dump(movie_dec,f,indent=4)
    return (movie_dec)
print(group_by_decade(movie_year))