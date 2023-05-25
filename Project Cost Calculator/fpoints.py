"""
Provides functionality for the Function Points calculation.
"""

def calc_fpoints():
    """
        Calculates Function Points values based on user input.
    """

    # STEP 1: Unadjusted Function Point (UFP) calculation
    # Weights for the functional complexities
    fp = [(3, 4, 6), (4, 5, 7), (3, 4, 6), (7, 10, 15), (5, 7, 10)]
    print("""
STEP 1. Please indicate the overall complexity of functions in the project:
1 - Simple      2 - Average     3 - Complex""")
    c = 0
    while c == 0:
        try:
            c = int(input("Please enter your selection (1-3):"))
        except ValueError:
            print("Please enter an integer between 1 and 3.")
    c -= 1 # So that it matches the index number of fp list
    ei, eo, eq, ilf, eif = -1, -1, -1, -1, -1 # Initiating the variables as negative to use them in while loop for input validation
    print("""
STEP 2. Please indicate the number and types of functions used in the applications
included in the project for each of the five categories below (e.g. 0, 15, 120, etc.)
""")
    while not ei >= 0:
        print("1. Number of external inputs (e.g. Input screen and tables):")
        try:
            ei = int(input("Please enter 0 or a positive integer value:"))
        except ValueError:
            print("Invalid input.")
    while not eo >= 0:
        print("2. Number of external outputs (e.g. Output screens and reports):")
        try:
            eo = int(input("Please enter 0 or a positive integer value:"))
        except ValueError:
            print("Invalid input.")
    while not eq >= 0:
        print("3. Number of external inquiries (e.g. Prompts and interrupts):")
        try:
            eq = int(input("Please enter 0 or a positive integer value:"))
        except ValueError:
            print("Invalid input.")
    while not ilf >= 0:
        print("4. Number of internal files (e.g. Databases and directories):")
        try:
            ilf = int(input("Please enter 0 or a positive integer value:"))
        except ValueError:
            print("Invalid input.")
    while not eif >= 0:
        print("5. Number of external interfaces (e.g. Shared databases and shared routines):")
        try:
            eif = int(input("Please enter 0 or a positive integer value:"))
        except ValueError:
            print("Invalid input.")

    # Unadjusted Function Point calculation (-1) corresponds to the index of the value
    ufp = fp[0][c] * ei + fp[1][c] * eo + fp[2][c] * eq + fp[3][c] * ilf + fp[4][c] * eif
    print(f"UFP = {ufp}")

    # STEP 2: Value Adjustment Factor (VAF) calculation
    # Initiating variables so that we can validate the user input later on, setting them to 10 because 0 is a valid value
    q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14 = 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 10
    print("""
STEP 2. Please answer 14 general system characteristic questions below to indicate the overall complexity of the system 
by asigning a value on a scale of 0-5 to each of them.
0 - Not present, or no influence,   1 - Incidental influence,      2 - Moderate influence 
3 - Average influence               4 - Significant influence      5 - Strong influence throughout
    """)
    while not q1 in range(0, 6):
        try:
            q1 = int(input("""
1. Data Communications (Describes the degree to which the application communicates directly with the processor):"""))
        except ValueError:
            print("Please enter a value between 0-5.")
    while not q2 in range(0, 6):
        try:
            q2 = int(input("""
2. Distributed Data Processing (Describes the degree to which the application transfers data among physical components of the
application):"""))
        except ValueError:
            print("Please enter a value between 0-5.")
    while not q3 in range(0, 6):
        try:
            q3 = int(input("""
3. Performance (Describes the degree to which response time and throughput performance considerations influenced the 
application development):"""))
        except ValueError:
            print("Please enter a value between 0-5.")
    while not q4 in range(0, 6):
        try:
            q4 = int(input("""
4. Heavily Used Configuration (Describes the degree to which computer resource restrictions influenced the development 
of the application. Heavily used operational configurations may require special considerations when designing the application):"""))
        except ValueError:
            print("Please enter a value between 0-5.")
    while not q5 in range(0, 6):
        try:
            q5 = int(input("""
5. Transaction Rate (Describes the degree to which the rate of business transactions influenced the development of the application):"""))
        except ValueError:
            print("Please enter a value between 0-5.")
    while not q6 in range(0, 6):
        try:
            q6 = int(input("""
6. On-Line Data Entry (On-line User Interface describes the degree to which data is entered or retrieved through 
interactive transactions. On-line User Interface for data entry, control functions, reports, and queries are provided in the application):"""))
        except ValueError:
            print("Please enter a value between 0-5.")
    while not q7 in range(0, 6):
        try:
            q7 = int(input("""
7. End-User Efficiency (Describes the degree of consideration for human factors and ease of use for the user of the 
application measured. The on-line functions provided emphasize a design for user efficiency):"""))
        except ValueError:
            print("Please enter a value between 0-5.")
    while not q8 in range(0, 6):
            try:
                q8 = int(input("""
8. On-Line Update (Describes the degree to which internal logical files (ILF) are updated on-line. The application 
provides on-line updates for the ILF's):"""))
            except ValueError:
                print("Please enter a value between 0-5.")
    while not q9 in range(0, 6):
            try:
                q9 = int(input("""
9. Complex Processing (Describes the degree to which processing logic influenced the development of the application):"""))
            except ValueError:
                print("Please enter a value between 0-5.")
    while not q10 in range(0, 6):
            try:
                q10 = int(input("""
10. Reusability (Describes the degree to which the application and the code in the application have been specifically 
designed, developed, and supported to be usable in other applications):"""))
            except ValueError:
                print("Please enter a value between 0-5.")
    while not q11 in range(0, 6):
            try:
                q11 = int(input("""
11. Installation Ease: Describes the degree to which conversion from previous environments influenced the development of 
the application. A conversion / installation plan and/or tools were provided and tested during the system test phase):"""))
            except ValueError:
                print("Please enter a value between 0-5.")
    while not q12 in range(0, 6):
            try:
                q12 = int(input("""
12. Operational Ease (Describes the degree to which the application attends to operational aspects, such as start-up, 
back-up, and recovery processes. The application minimizes the need for manual activities, such as tape mounts, paper 
handling, and direct, on-location manual intervention):"""))
            except ValueError:
                print("Please enter a value between 0-5.")
    while not q13 in range(0, 6):
            try:
                q13 = int(input("""
13. Multiple Sites (Describes the degree to which the application has been developed for different hardware and software environments):"""))
            except ValueError:
                print("Please enter a value between 0-5.")
    while not q14 in range(0, 6):
            try:
                q14 = int(input("""
14. Facilitate Change (Describes the degree to which the application has been developed for easy modification of 
processing logic or data structure. Made up of two parts: Flexible Query and Business Data Control Data):"""))
            except ValueError:
                print("Please enter a value between 0-5.")

    qtotal = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9 + q10 + q11 + q12 + q13 + q14
    vaf = 0.65 + qtotal/100

    # STEP 3: Adjusted Function Point (AFP) calculation
    afp = ufp * vaf

    print(f"""
The Adjusted Function Point (AFP) calculated for your project is: {afp}
You can compare this value to that of the other projects.""")

    return