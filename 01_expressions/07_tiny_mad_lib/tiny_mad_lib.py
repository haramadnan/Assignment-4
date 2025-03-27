def programming_mad_lib():
    """Yeh function ek programmer ki journey par Mad Libs story generate karega"""

    # User se inputs lena
    name = input("Enter a programmer's name: ")
    language = input("Enter a programming language: ")
    project = input("Enter a project name: ")
    bug = input("Enter a type of bug (e.g., syntax error, infinite loop, segmentation fault): ")
    feeling = input("Enter an emotion (e.g., frustration, excitement, relief): ")
    mentor = input("Enter a famous programmer or mentor's name: ")

    # Story template
    story = f"""
    {name} had always been fascinated by coding. They decided to learn {language} 
    and started working on a project called {project}. Everything seemed exciting 
    until they encountered a {bug}. 

    At first, {name} felt {feeling}. They spent hours debugging, searching Stack Overflow, 
    and even considered giving up. But then, they remembered the advice of {mentor}: 
    "Every bug is a lesson, not a roadblock."

    With renewed determination, {name} kept going, fixing the {bug} and finally 
    completing {project}. That day, they realized that programming is not just about writing code, 
    but about solving problems and never giving up.
    """

    # Output dikhana
    print("\nYour Programming Mad Libs Story:")
    print(story)

# Function call kar ke game start karna
programming_mad_lib()