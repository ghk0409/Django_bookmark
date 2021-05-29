from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from .models import Bookmark
from django.urls import reverse_lazy


class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 5

# CreateView를 상속받아 사용
class BookmarkCreateView(CreateView):
    # model : 어떤 모델을 입력 받을 것인가
    # fields : 어떤 필드들을 입력 받을 것인가
    # success_url : create 완료 후 이동할 페이지 url, 보통 상세 페이지로 이동하지만 여기서는 목록 페이지
    # template_name_suffix : 사용할 템플릿의 접미사만 변경하는 설정값 / bookmark_create 템플릿 파일 사용
    model = Bookmark
    fields = ['site_name', 'url']
    success_url = reverse_lazy('list')
    template_name_suffix = '_create'

class BookmarkDetailView(DetailView):
    model = Bookmark

class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name', 'url']
    template_name_suffix = '_update'

class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')
    # 삭제 후 목록 페이지로 이동