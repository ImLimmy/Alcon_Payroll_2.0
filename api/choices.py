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
    
class Status(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    APPROVED = 'Approved', 'Approved'
    REJECTED = 'Rejected', 'Rejected'
    CANCELLED = 'Cancelled', 'Cancelled'
    CLOSED = 'Closed', 'Closed'
    
class Leave(models.TextChoices):
    SICK_LEAVE = 'Sick Leave', 'Sick Leave'
    EMERGENCY_LEAVE = 'Emergency Leave', 'Emergency Leave'
    VACATION_LEAVE_WITHOUT_PAY = 'Vacation Leave without Pay', 'Vacation Leave without Pay'
    VACATION_LEAVE_WITH_PAY = 'Vacation Leave with Pay', 'Vacation Leave with Pay'
    MATERNITY_LEAVE = 'Maternity Leave', 'Maternity Leave'
    PATERNITY_LEAVE = 'Paternity Leave', 'Paternity Leave'
    OTHER = 'Other', 'Other'
    
class Career(models.TextChoices):
    PROBATIONARY = 'Probationary', 'Probationary'
    CONTRACTUAL = 'Contractual', 'Contractual'
    END_OF_CONTRACT = 'End of Contract', 'End of Contract'
    REGULAR = 'Regular', 'Regular'
    RESIGNED = 'Resigned', 'Resigned'
    RETIRED = 'Retired', 'Retired'
    TERMINATED = 'Terminated', 'Terminated'
    ABSENT_WITHOUT_LEAVE = 'Absent without Leave', 'Absent without Leave'
    
class Extras(models.TextChoices):
    ACTIVE = 'Active_On', 'ON'
    INACTIVE = 'Inactive_Off', 'OFF'
    