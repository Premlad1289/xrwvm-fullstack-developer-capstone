from django.urls import path
from . import views

urlpatterns = [
    # Authentication endpoints
    path('login/', views.login_user, name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),
    path('user/', views.get_current_user, name='current_user'),
    
    # Dealer endpoints
    path('dealers/', views.get_dealers, name='get_dealers'),
    path('dealers/<int:dealer_id>/', views.get_dealer_by_id, name='get_dealer_by_id'),
    path('dealers/state/<str:state>/', views.get_dealers_by_state, name='get_dealers_by_state'),
    
    # Review endpoints
    path('reviews/dealer/<int:dealer_id>/', views.get_dealer_reviews, name='get_dealer_reviews'),
    path('reviews/', views.post_review, name='post_review'),
    
    # Car endpoints
    path('cars/makes/', views.get_car_makes, name='get_car_makes'),
    path('cars/models/', views.get_car_models, name='get_car_models'),
    path('get_cars', views.get_cars, name='get_cars'),
    path('get_cars/', views.get_cars, name='get_cars_slash'),
    
    # Sentiment analysis endpoint
    path('analyze/', views.analyze_review_sentiment, name='analyze_sentiment'),
    path('analyze/<path:text>', views.analyze_review_sentiment, name='analyze_sentiment_text'),
    path('analyze/<path:text>/', views.analyze_review_sentiment, name='analyze_sentiment_text_slash'),
]
