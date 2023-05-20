"""
Provides functionality for the basic COCOMO calculation.
"""

def calc_cocomo():
    """
        Calculates basic COCOMO values based on user input.
    """

    # The basic COCOMO parameters for each category
    param = [(2.4, 1.05, 2.5, 0.38), (3.0, 1.12, 2.5, 0.35), (3.6, 1.20, 2.5, 0.32)]
    size, project = 0, 0 # Initiating variables so that user input can be validated

    print("""
In COCOMO, projects are categorized into three types:
  Organic
  Semidetached
  Embedded

1. Organic: A development project can be treated of the organic type, if the project deals with developing a well-understood application program, the size of the development team is reasonably small, and the team members are experienced in developing similar methods of projects. Examples of this type of projects are simple business systems, simple inventory management systems, and data processing systems.
2. Semidetached: A development project can be treated with semidetached type if the development consists of a mixture of experienced and inexperienced staff. Team members may have finite experience in related systems but may be unfamiliar with some aspects of the order being developed. Example of Semidetached system includes developing a new operating system (OS), a Database Management System (DBMS), and complex inventory management system.
3. Embedded: A development project is treated to be of an embedded type, if the software being developed is strongly coupled to complex hardware, or if the stringent regulations on the operational method exist. For Example: ATM, Air Traffic control.
""")
    while project not in range (1,4):
        try:
            project = int(input("Please make your selection (1-3):"))
        except ValueError:
            print("Please enter an integer value between 1-3.")

    print("""
Please enter the size of the project in KLOC (thousands of lines of code).
For example, for 500,000 lines, enter 500.""")
    while size <= 0:
        try:
            size = int(input("Project size:"))
        except ValueError:
            print("Please enter an integer value greater than 0.")

    p = project - 1 # Minus 1 corresponds to the index of the param list
    a, b, c, d = param[p][0], param[p][1], param[p][2], param[p][3]
    effort = (a * size) ** b
    time = (c * effort) ** d
    people = effort / time

    print(f"""Based on your input, the project will take {round(time, 2)} months to be completed and 
and a total of {round(people, 2)} people are needed.""")
    return
