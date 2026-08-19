movies = {
    "the shawshank redemption": 12.99,
    "the godfather": 14.99,
    "the dark knight": 13.99,
    "inception": 11.99,
    "interstellar": 15.99,
    "avengers: endgame": 16.99,
    "titanic": 10.99,
    "the matrix": 12.49,
    "forrest gump": 11.49,
    "gladiator": 13.49,
    "jurassic park": 10.49,
    "the lion king": 9.99,
    "frozen": 8.99,
    "spider-man: no way home": 17.99,
    "top gun: maverick": 16.49,
    "oppenheimer": 18.99,
    "barbie": 15.49,
    "the avengers": 13.99,
    "iron man": 11.99,
    "black panther": 14.49,
    "coco": 9.49,
    "toy story": 8.49,
    "finding nemo": 8.99,
    "shrek": 9.99,
    "harry potter and the sorcerer's stone": 12.99
}



def show_movie_list():
      for i, (item, price) in enumerate(movies.items()):
            print(f"{i}.{item} - ${price} ")

def Book_movie(customer,booking,total):
      if customer in movies:
          tickets=int(input(f"how many tickets do u want for {customer}: "))
          price=movies[customer]
          cost=price*tickets
          total+=cost
          booking = booking + [{"movie": customer, "tickets": tickets, "cost": cost}]
      else:
          print("movie is not available in our cheap ass theatre")

      return booking,total

def show_reciept(booking,total):
      print("reciept:-")
      for i in booking:
            print(f"{i['movie']} - {i['tickets']} tickets - ${i['cost']}")
      print(f"Your total cost was ${total}")
      
def run_movie_theatre():
      show_movie_list()
      booking=[]
      total=0
      while True:
            customer=input("what motherF@@@@ing movies do ya want: ").lower()

            booking, total = Book_movie(customer, booking, total)

            
            yn=input("wanna book a another movie (y)es or (n)o: ")
            if yn =="y":
                  continue
            elif yn == "n":
                  show_reciept(booking,total)
                  break
            else:
                  print("invalid option unemployed piece of shit")

run_movie_theatre()

      



