"""
Functions related to initializing a gradebook 
"""
import json

def create_empty():
    """
    Add functionality, description, doctests, doctypes, paremeters
    """
    ...


def add_students(path: 'str') -> dict:
    """Adding the dictionary, where the key are tuples of students info from the file 


    Args:
        path (str): csv file where to get students names, emails and group

    Returns:
        dict: key: tuple with name, surname, email and group and value is another dict, hovever empty one

    >>> (add_students('names_and_emails.csv'))[('Печененко', 'Ярина', 'pechenenko.pn@ucu.edu.ua', 'ПСА24/Б-1')]
    {}
    """


    with open(path, 'r', encoding='utf-8') as file:
        students = {}
        for line in file.readlines():
            student = line.strip().split(';')
            student[0] = student[0].split(' ')
            student_ = (student[0][0], student[0][1], student[1], student[2])
            students[student_] = {}
        return students



def del_activity(gradebook, activity):
    """
    Add functionality, description, doctests, doctypes.
    """
    ...


def add_activity(gradebook, activity):
    """
    Add functionality, description, doctests, doctypes.
    """
    ...


def add_student(gradebook, student):
    """
    Add functionality, description, doctests, doctypes.
    """
    ...
if __name__=='__main__':
    import doctest
    print(doctest.testmod())