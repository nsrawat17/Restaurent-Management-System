def take_feedback():
    rating = float(input("Rate us 1 to 5 "))
    review = input("Your Feedback : ")

    with open("feedback.txt","a") as file :
        file.write(f"Rating : {rating}, Feedback: {review}\n")


    print("Thanks  for your feedback ")