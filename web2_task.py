
from web1_task import adventure_movie
import pprint
import json

scrapped_data=adventure_movie()
def top_movie(movies):

    years=[]
    for i in movies:
        if i["Year"] not in years:
            years.append(i["Year"])
    movies_dict={i:[] for i in years}
    for i in movies:
        year=i["Year"]
        for update_year in movies_dict:
            # print(update_year,year)
            if (update_year)==(year):
                movies_dict[update_year].append(i)

    with open("top_movie_2.json","w") as file1:
        json.dump(movies_dict,file1,indent=5)
    return movies_dict

top_movie(scrapped_data)




