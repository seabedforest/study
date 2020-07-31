from django.urls import path
from . import views

urlpatterns = [
    # v1/topics/username
    path('<str:author_id>', views.TopicView.as_view())
]
