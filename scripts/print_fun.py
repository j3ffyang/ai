def printstuff(Stuff):

    for i, s in enumerate(Stuff):
        print("Album", i, "Rating is", s)

album_ratings = [10.0, 8.5, 9.5]
printstuff(album_ratings)