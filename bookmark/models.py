from django.db import models
from django.urls import reverse

# Create your models here.
class Bookmark(models.Model):
    site_name = models.CharField(max_length=100)
    url = models.URLField('Site URL')
    # 모델 안에 있는 클래스 변수 = field
    # site_name과 url 2개의 필드를 만들어서 데이터베이스에 해당 2가지 정보를 저장 가능

    def __str__(self):
        # 객체를 출력할 때 나타날 값
        return "이름 : " + self.site_name + ", 주소 : " + self.url

    def get_absolute_url(self):
        return reverse('detail', args=[str(self.id)])
    # get_absolute_url 메서드는 장고에서 사용하는 메서드
    # 보통 객체의 상세 화면 주소(detail)를 반환하게 만듦
    # reverse 메서드는 URL 패턴의 이름과 추가 인자를 전달받아 URL을 생성하는 메서드!!