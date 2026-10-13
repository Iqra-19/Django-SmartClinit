from django.db import models

# Department Model
class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name}"

# Doctor Model
class Doctor(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15, unique = True)
    email = models.EmailField(unique = True)
    
    department = models.ForeignKey(
        Department,
        on_delete = models.PROTECT,
        related_name = "doctors",   # Lets us access a department's doctors using .doctors
    )

    specialization = models.CharField(max_length = 100)
    qualification = models.CharField(max_length = 100)
    experience_years = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

# Availability Model
class DoctorAvailability(models.Model):

    DAYS_OF_WEEK = [
        ("MON", "Monday"),
        ("TUE", "Tuesday"),
        ("WED", "Wednesday"),
        ("THU", "Thursday"),
        ("FRI", "Friday"),
        ("SAT", "Saturday"),
        ("SUN", "Sunday"),
    ]

    doctor = models.ForeignKey(
        Doctor,
        on_delete = models.CASCADE,
        related_name="availabilities"
    )

    day = models.CharField(
        max_length = 3, 
        choices = DAYS_OF_WEEK
    )

    start_time = models.TimeField()
    end_time = models.TimeField()

    def __str__(self):
        return f"{self.doctor} - {self.get_day_display()} ({self.start_time} - {self.end_time})"  # Django provide get_day_display() when a field has choices.