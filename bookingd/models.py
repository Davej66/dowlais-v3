from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

SERVICE_CHOICESD = (
    ("Urinary tract infection", "Urinary tract infection"),
    ("Emergency Contraception", "Emergency Contraception"),
    ("Skin conditions", "Skin conditions"),
    ("Ear Health", "Ear Health"),
    ("Sore throat test & treat", "Sore throat test & treat"),
    ("Flu Vaccination", "Flu Vaccination"),
    )
    
TIME_CHOICESD = (
    ("9 AM", "9 AM"),
    ("9:30 AM", "9:30 AM"),
    ("10 AM", "10 AM"),
    ("10:30 APM", "10:30 AM"),
    ("11 AM", "11 AM"),
    ("11:30 AM", "11:30 AM"),
    ("12 PM", "12 PM"),
    ("12:30 PM", "12:30 PM"),
    ("1 PM", "1 PM"),
    ("1:30 PM", "1:30 PM"),
    ("2 PM", "2 PM"),
    ("2:30 PM", "2:30 PM"),
    ("3 PM", "3 PM"),
    ("3:30 PM", "3:30 PM"),
    ("4 PM", "4 PM"),
    ("4:30 PM", "4:30 PM"),
    ("5 PM", "5 PM"),
    ("5:30 PM", "5:30 PM"),
    ("6 PM", "6 PM"),
)

class Appointmentd(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    service = models.CharField(max_length=50, choices=SERVICE_CHOICESD, default="Doctor care")
    day = models.DateField(default=datetime.now)
    time = models.CharField(max_length=10, choices=TIME_CHOICESD, default="M")
    time_ordered = models.DateTimeField(default=datetime.now, blank=True)
    def __str__(self):
        return f"{self.user.username} | day: {self.day} | time: {self.time}"


