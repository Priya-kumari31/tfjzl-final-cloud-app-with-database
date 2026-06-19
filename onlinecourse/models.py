from django.db import models
from django.contrib.auth.models import User


class Instructor(models.Model):
    name = models.CharField(max_length=200)


class Learner(models.Model):
    name = models.CharField(max_length=200)


class Course(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    total_enrollment = models.IntegerField(default=0)


class Lesson(models.Model):
    title = models.CharField(max_length=200)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()


# ✅ REQUIRED MODEL 1
class Question(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    question_text = models.TextField()
    grade = models.IntegerField(default=1)

    def is_get_score(self, selected_ids):
        correct_ids = list(
            self.choice_set.filter(is_correct=True).values_list('id', flat=True)
        )
        return set(correct_ids).issubset(set(selected_ids))


# ✅ REQUIRED MODEL 2
class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=100)
    is_correct = models.BooleanField(default=False)


# ✅ REQUIRED MODEL 3
class Enrollment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    mode = models.CharField(max_length=30, default='honor')


# ✅ REQUIRED MODEL 4
class Submission(models.Model):
    enrollment = models.ForeignKey(Enrollment, on_delete=models.CASCADE)
    choices = models.ManyToManyField(Choice)