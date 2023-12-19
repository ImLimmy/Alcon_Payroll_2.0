from django.db import models

class Gender(models.TextChoices):
    MALE = 'Male', 'Male'
    FEMALE = 'Female', 'Female'
    OTHER = 'Other', 'Other'

class CivilStatus(models.TextChoices):
    SINGLE = 'Single', 'Single'
    MARRIED = 'Married', 'Married'
    DIVORCED = 'Divorced', 'Divorced'
    SEPARATED = 'Separated', 'Separated'
    WIDOW = 'Widow', 'Widow'
    OTHER = 'Other', 'Other'
    
class Suffix(models.TextChoices):
    JR = 'Jr.', 'Jr.'
    SR = 'Sr.', 'Sr.'
    I = 'I', 'I'
    II = 'II', 'II'
    III = 'III', 'III'
    IV = 'IV', 'IV'
    V = 'V', 'V'
    VI = 'VI', 'VI'
    VII = 'VII', 'VII'
    VIII = 'VIII', 'VIII'
    IX = 'IX', 'IX'
    X = 'X', 'X'
    OTHER = 'Other', 'Other'
    
class EducationalAttainment(models.TextChoices):
    ELEMENTARY = 'Elementary', 'Elementary'
    HIGH_SCHOOL = 'High School', 'High School'
    COLLEGE_UNDERGRAD = 'College Undergrad', 'College Undergrad'
    COLLEGE = 'College', 'College'
    MASTERS = 'Masters', 'Masters'
    DOCTORATE = 'Doctorate', 'Doctorate'
    
class LogStatus(models.TextChoices):
    TIME_IN = 'Time In', 'Time In'
    TIME_OUT = 'Time Out', 'Time Out'