from django.urls import path
from .views import *

urlpatterns = [
    # '' 인수는 북마크앱의 루트 페이지 역할 bookmark/ 로 접속 시 BookmarkListView 뷰 호출
    # 함수형 뷰는 이름만 호출하면 되지만 클래스형 뷰는 뒤에 .as_view() 꼭 붙이기!!
    # 마지막 인자 name은 설정한 이름을 가지고 해당 URL 패턴을 찾을 수 있도록 하는 역할
    path('', BookmarkListView.as_view(), name='list'),
    path('add/', BookmarkCreateView.as_view(), name='add'),
    path('detail/<int:pk>/', BookmarkDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', BookmarkUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BookmarkDeleteView.as_view(), name='delete'),
]

# [<int:pk>] : int 타입의 변수명
# 앞쪽(int)을 '컨버터'라고 부름(클래스 형태) -> 생략하거나 커스텀 컨버터 가능
# 뒤쪽(pk)은 컨버터를 통해 반환받은 값 / 패턴에 일치하는 값의 변수명