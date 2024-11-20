import time

def main():

    while(1):
        print("Enter search type - Title, Genre, Year - or exit:")
        searchType = input()

        if(searchType == "exit"):
            return

        print("Enter your search:")
        searchInput = input()

        #write into the file
        with open("search.txt", "w") as search:
            search.write("input\n")
            if(searchType.lower() == "title"):
                search.write("t\n")
            elif(searchType.lower() == "genre"):
                search.write("g\n")
            elif(searchType.lower() == "year"):
                search.write("y\n")
            search.write(searchInput)
        
        #waits for and gets the results from the microsserivce
        while(1):
            key = ""
            #reads first line in file and checks if it says output
            with open("search.txt", "r") as search:
                key = search.readline().strip()
            
                #only processes if first line is output, meaning microservice has ran
                if(key == "output"):
                    movieList = []
                    
                    line = search.readline().strip()

                    while (line != ""):            
                        parts = line.split(",")

                        movieList.append({
                            "title":  parts[0],
                            "genre": parts[1],
                            "rating": parts[2],
                            "year": parts[3]
                        })
                        
                        line = search.readline().strip()
                    
                    print("Results")
                    for movie in movieList:
                        print(movie["title"] + " " + movie["genre"] + " " + movie["rating"] + " " + movie["year"] + "\n")
                    
                    break
        


            
            
                

    
     

 






main()