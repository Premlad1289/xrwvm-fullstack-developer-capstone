from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from djangoapp import views as app_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('djangoapp.urls')),
    
    # Direct Coursera grading endpoints
    path('fetchDealers', app_views.get_dealers, name='fetch_dealers'),
    path('fetchDealers/', app_views.get_dealers, name='fetch_dealers_slash'),
    path('fetchDealers/<str:state>', app_views.get_dealers_by_state, name='fetch_dealers_state'),
    path('fetchDealers/<str:state>/', app_views.get_dealers_by_state, name='fetch_dealers_state_slash'),
    path('fetchDealer/<int:dealer_id>', app_views.get_dealer_by_id, name='fetch_dealer_by_id'),
    path('fetchDealer/<int:dealer_id>/', app_views.get_dealer_by_id, name='fetch_dealer_by_id_slash'),
    path('fetchReviews/dealer/<int:dealer_id>', app_views.get_dealer_reviews, name='fetch_dealer_reviews'),
    path('fetchReviews/dealer/<int:dealer_id>/', app_views.get_dealer_reviews, name='fetch_dealer_reviews_slash'),
    path('djangoapp/get_cars', app_views.get_cars, name='djangoapp_get_cars'),
    path('djangoapp/get_cars/', app_views.get_cars, name='djangoapp_get_cars_slash'),
    path('analyze/<path:text>', app_views.analyze_review_sentiment, name='analyze_text'),
    path('analyze/<path:text>/', app_views.analyze_review_sentiment, name='analyze_text_slash'),
    
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    re_path(r'^(?!admin|api|static|media|fetchDealers|fetchDealer|fetchReviews|djangoapp|analyze).*$', TemplateView.as_view(template_name='index.html')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
