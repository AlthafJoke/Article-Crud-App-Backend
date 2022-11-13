
from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('articles', views.ArticleViewSet, basename='articles')
router.register('users', views.UserViewSet )



urlpatterns = [
    path('api/', include(router.urls)),
    # path('articles', views.article_list),
    # path('articles/<int:pk>/', views.articles_details)
    # path('articles/', views.ArticleList.as_view()),
    # path('articles/<int:id>/', views.ArticleDetails.as_view()),
    
]