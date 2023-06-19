from django.urls import path

from . import views
from .views import index

urlpatterns = [
    path('', index, name="index"),
    path("like/<int:pohoto_id>/", views.like_fuctionality, name="like"),
    path("share/<int:photo_id>/", views.copy_link_to_clipboard, name='share'),
    path("comment/<int:photo_id>/", views.comment_fuctionality, name="comment")

]