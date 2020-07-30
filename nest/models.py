from django.db import models

class Notices(models.Model):
    subject = models.CharField(max_length=200)
    date = models.DateField(auto_now_add=True, null=True)
    body = models.TextField(null=True, blank=True)
    notice_file = models.FileField(upload_to='uploads/notices_pdf')

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "Notice"
        verbose_name_plural = "Notices"

class Result(models.Model):
    batch = models.CharField(max_length=200)
    exam_year = models.IntegerField()
    result_file = models.FileField(upload_to='uploads/results_pdf')

    def __str__(self):
        return str(self.batch + ' - ' + str(self.exam_year))

class NewsTicker(models.Model):
    title = models.CharField(max_length=200, null=True)
    news = models.ForeignKey(Notices,on_delete=models.CASCADE)

    def __str__(self):
        return str(self.title + ' - ' + self.news.subject)

    class Meta:
        verbose_name = "Important News"
        verbose_name_plural = "Important Newses"
