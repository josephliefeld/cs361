import time
def writeFile(movieResults):
            with open("search.txt", "w") as search:
                search.write("output\n")
                for movie in movieResults:
                    text = movie["title"] + "," + movie["genre"] + "," + movie["rating"] + "," + movie["year"] + "\n"
                    search.write(str(text))

#will have format
#key
#searchType
#searchInput
def waitSearch():

    while(1):
        key = ""
        searchType = ""
        searchInput = ""

        #get text from textfile search.txt
        with open("search.txt") as search:
            key = search.readline().strip() #tells whether input or output
            searchType = search.readline().strip() #t - title g - genre y - year
            searchInput = search.readline().strip() #what the user typed in

        #if text file is not empty. format of search will be searchType \n searchInput
        if(key == "input"):
            movieList = []

            #get movies from csv file and put into movieList
            with open("moviesearch.csv", "r") as movies:
                
                line = movies.readline().strip()


                #Gets each line from the file and splits it into each category and stores it in movieList
                while (line != ""):            
                    parts = line.split(",")

                    movieList.append({
                        "title":  parts[0],
                        "genre": parts[1],
                        "rating": parts[2],
                        "year": parts[3]
                    })

                    line = movies.readline().strip()
            
            movieResults = []

            if(searchType == "t"):
                for movie in movieList:
                    if (str(movie["title"]).lower() == searchInput.lower()):
                        movieResults.append(movie)
            
            elif(searchType == "g"):
                for movie in movieList:
                    if(str(movie["genre"]).lower() == searchInput.lower()):
                        movieResults.append(movie)
            
            elif(searchType == "y"):
                for movie in movieList:
                    if(str(movie["year"]) == searchInput):
                        movieResults.append(movie)

            writeFile(movieResults)
        
        time.sleep(3)
            
def main():
    waitSearch()


main()
