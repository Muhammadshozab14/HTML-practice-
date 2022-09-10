a = print("Sci-Fi", "\nMystery", "\nPhilosophy","\nPhilosophy-Psychology","Psychology","\nNovels")
Books = input("Enter Your Book Type: ")

def bookCategory(Books):
    if Books == "Sci-Fi":
        print("The Ultimate Hitchhiker's Guide to the Galaxy by Douglas Adams (4.38 – 257,751)",
              "\nFrankenstein by Mary Shelleys",
              "\nThe Hunger Games Trilogy",
              "\nHoughton Mifflin Harcourt 1984")
    elif Books == "Mystery": 
        print("\nThe Silent Patient by Alex Michaelides",
              "\nThe Postman Always Rings Twice is often by James M.Cain ",
              "\nIn Cold Blood by Truman Capot",
              "\nAnatomy of a Murder by Robert Traver")
    elif Books == "Philosophy":
        print("\nA History of Western Philosophy by Bertrand Russels",
              "\nMan’s Search for Meaning by Viktor Frankl",
              "\nBeyond Good And Evil by Nietzsche",
              "\nThe Book of Healing – Avicenna")
    elif Books == "Philosophy-Psychology":
        print("Philosophy of Psychology: An Introduction by Kengo Miyazono and Lisa Bortolotti",
             "\nQuiet: The Power of Introverts in a World That Can't Stop Talking by Susan Cain",
             "\nExamined Life: How We Lose and Find Ourselves by Stephen Grosz",
             "\nMan's Search for Meaning by Viktor Frankl")
    elif Books == "Psychology":
        print("Thinking, Fast and Slow by Daniel Kahneman",
        "\nMistakes Were Made by Carol Tavris and Elliot Aronson",
        "\nInfluence: Science and Practice by Robert Cialdini",
        "\nPredictably Irrational by Dan Ariely")
    elif Books == "Novels":
        print("Harry Potter and the Philosopher's Stoneby Rowling J.K."
        "\nHarry Potter and the Order of the Phoenix by Rowling, J.K.",
        "\nHarry Potter and the Deathly Hallowsby Rowling J.K.",
        "\nDa Vinci Code by Brown, Dan")


bookCategory(Books)
