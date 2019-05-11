from django.urls import path
from . import views

app_name = 'adviseMeApp'

urlpatterns = [
    path('topic/<int:pk>', views.TopicView.as_view(), name='topicview'),
    path('topic/add', views.TopicCreate.as_view(), name='topicCreate'),
    path('topic/<int:pk>/comment', views.CommentCreate.as_view(), name='commentCreate'),

    path('comment/<int:pk>', views.vote, name='vote'),
]
