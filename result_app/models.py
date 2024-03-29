from django.db import models
from django.contrib.auth.models import AbstractUser

class customUser(AbstractUser):
    department=models.CharField(max_length=120)
    city=models.CharField(max_length=120)

    def __str__(self):
        return self.username
    
class SubjectModel(models.Model):
    SubjectName=models.CharField(max_length=120)
    SubjectCode=models.CharField(max_length=120)
    Credit=models.CharField(max_length=120)

    def __str__(self) -> str:
        return self.SubjectName+ " " +self.Credit
    
class studentModel(models.Model):

    StudentName=models.CharField(max_length=120,null=True)
    Age=models.FloatField()
    roll = models.IntegerField(blank=True, null=True)
    Subjects=models.ManyToManyField(SubjectModel)

    def __str__(self) -> str:
        return self.StudentName
    

class MarkModel(models.Model):
    student = models.ForeignKey(studentModel, on_delete=models.CASCADE, related_name='student_marksheet')
    subject = models.ForeignKey(SubjectModel, on_delete=models.CASCADE)
    marks = models.FloatField()

    def __str__(self) -> str:
        return f"{self.student.StudentName} - {self.subject.SubjectName}: {self.marks}"

