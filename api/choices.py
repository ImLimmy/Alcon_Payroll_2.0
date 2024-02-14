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
    NONE = '', ''
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


class TimeStatus(models.TextChoices):
    TIME_IN = 'Time In', 'Time In'
    TIME_OUT = 'Time Out', 'Time Out'
    LATE = 'Late', 'Late'
    FLEXI = 'Flexi', 'Flexi'


class Status(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    APPROVED = 'Approved', 'Approved'
    REJECTED = 'Rejected', 'Rejected'
    CANCELLED = 'Cancelled', 'Cancelled'
    CLOSED = 'Closed', 'Closed'


class Leave(models.TextChoices):
    SICK_LEAVE = 'Sick Leave', 'Sick Leave',
    VACATION_LEAVE = 'Vacation Leave', 'Vacation Leave',
    MATERNITY_LEAVE = 'Maternity Leave', 'Maternity Leave'
    PATERNITY_LEAVE = 'Paternity Leave', 'Paternity Leave'
    HALF_DAY_LEAVE = 'Half Day Leave', 'Half Day Leave'
    UNDERTIME = 'Undertime', 'Undertime'
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
    ACTIVE = 'Active', 'Active'
    INACTIVE = 'Inactive', 'Inactive'
