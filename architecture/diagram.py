class Person():
    first_name = "" #Jens
    last_name = "" #Hansen
    email_address = "" #test@yeet.com
    gender = "" #M/F kun et enkelt bogstav

#Alle classes skal inherite fra personen
class Student():
    student_id = 1
    klasse = ""
    valgfag = ""
    teknikfag = ""

class Teacher():
    staff_id = 1
    subjects_taught = []


class Subject():
    subject_id = 1
    name = ""
    taught_by = "" #henter staff_id
    taught_to = [] #Henter student class
