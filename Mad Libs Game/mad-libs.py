def mad_libs():
    print("🌟 Welcome to the Thoughtful Mad Libs Game! 🌟\n")

    # User inputs
    name = input("Enter a name: ")
    profession = input("Enter a profession: ")
    place = input("Enter a place: ")
    goal = input("Enter a life goal: ")
    obstacle = input("Enter a challenge (e.g., fear, failure, doubt): ")
    mentor = input("Enter a name of a mentor or inspiration: ")

    # Story template
    story = f"""
    {name} always dreamed of becoming a {profession}.  
    Every day, they worked hard and pushed themselves to improve.  
    One day, in {place}, {name} faced their biggest challenge: {obstacle}.  
    It was a moment of doubt, but they remembered the advice of {mentor}:  
    "Success comes to those who never give up."  
    With determination, {name} overcame {obstacle} and finally achieved their goal of {goal}.  
    Their journey was tough, but their perseverance made them an inspiration for many.
    """

    print("\n🌟 Here is your inspiring Mad Libs story: 🌟\n")
    print(story)

# Run the game
mad_libs()