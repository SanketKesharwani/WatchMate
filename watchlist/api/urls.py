from django.urls import path,include
# from watchlist.api.views import movie_list,movie_details
from watchlist.api.views import WatchListAV,WatchDetailAV,StreamPlatformAV,StreamPlatformDetailAV,ReviewList,ReviewDetail,ReviewCreate

urlpatterns =[
    path('list/',WatchListAV.as_view(),name='movie-list'),
    path('<int:pk>/',WatchDetailAV.as_view(),name='movie-details'),
    path('stream/',StreamPlatformAV.as_view(),name='stream-platform'),
    path('stream/<int:pk>/',StreamPlatformDetailAV.as_view(),name='stream-platform'),
    path('<int:pk>/review/',ReviewList.as_view(),name='review-list'),
    path('<int:pk>/review-create/',ReviewCreate.as_view(),name='review-create'),
    path('review/<int:pk>/',ReviewDetail.as_view(),name='review-detail'),
]