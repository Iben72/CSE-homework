with open("life-expectancy.csv") as global_life:
     for line in global_life:
      clean_line = line.strip("global_life")
      parts = clean_line.split(",")
      entity = [0]
      code = [1]
      year = [2]
      lifeexpectancy = [3]