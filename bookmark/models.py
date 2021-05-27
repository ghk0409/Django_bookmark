from django.db import models

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    # 모델 안에 있는 클래스 변수 = field
    # site_name과 url 2개의 필드를 만들어서 데이터베이스에 해당 2가지 정보를 저장 가능

    def __str__(self):
        # 객체를 출력할 때 나타날 값
        return "이름 : " + self.site_name + ", 주소 : " + self.url
