from django.db import models


class Human(models.Model):
    id = models.IntegerField(primary_key=True)
    surname = models.CharField(max_length=255, blank=True, null=True)
    firstname = models.CharField(max_length=255, blank=True, null=True)
    period = models.IntegerField(blank=True, null=True)
    done = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'human'


class HumanEngagementdate(models.Model):
    id = models.IntegerField(primary_key=True)
    instituteid = models.IntegerField(blank=True, null=True)
    humanid = models.IntegerField(blank=True, null=True)
    dateofengagement = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'human_engagementdate'


class HumanNationaid(models.Model):
    id = models.IntegerField(primary_key=True)
    humanid = models.IntegerField()
    nationalid = models.CharField(max_length=255)

    class Meta:
        managed = False
        db_table = 'human_nationaid'


class HumanNationality(models.Model):
    id = models.IntegerField(primary_key=True)
    humanid = models.IntegerField(blank=True, null=True)
    nationality = models.CharField(max_length=255, blank=True, null=True)
    citizenship = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'human_nationality'


class HumanPersonal(models.Model):
    id = models.IntegerField(primary_key=True)
    gender = models.CharField(max_length=255, blank=True, null=True)
    dob = models.CharField(max_length=255, blank=True, null=True)
    humanid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'human_personal'


class Humancapital(models.Model):
    id = models.IntegerField(primary_key=True)
    ecnumber = models.CharField(max_length=255, blank=True, null=True)
    department = models.CharField(max_length=255, blank=True, null=True)
    isteaching = models.CharField(max_length=255, blank=True, null=True)
    jobtitle = models.CharField(max_length=255, blank=True, null=True)
    humanid = models.IntegerField(blank=True, null=True)
    instituteid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'humancapital'


class Institute(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    type = models.CharField(max_length=255, blank=True, null=True)
    ownership = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'institute'


class Period(models.Model):
    id = models.IntegerField(primary_key=True)
    period = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'period'


class Student(models.Model):
    # Field name made lowercase.
    instituteissueid = models.CharField(
        db_column='instituteIssueId', max_length=255)
    period = models.IntegerField(blank=True, null=True)
    programme = models.CharField(max_length=255, blank=True, null=True)
    mode = models.CharField(max_length=255, blank=True, null=True)
    instituteid = models.IntegerField(blank=True, null=True)
    humanid = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'student'
