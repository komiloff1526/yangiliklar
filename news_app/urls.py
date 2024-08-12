from django.urls import path
from news_app.views import news_list_view, new_detail_view, contact_view, local_news_view, xorij_news_view,texnalogiya_news_view, sport_news_view, madaniyat_news_view, sport_news_view

urlpatterns = [
    path('', news_list_view, name='news_list'),
    # path('', NewsListView.as_view(), name='news_list'),
    path('contact-us/', contact_view, name='contact_page'),
    path('local/', local_news_view, name='local_news'),
    path('xorij/', xorij_news_view, name='xorij_news'),
    path('sport/', sport_news_view, name='sport_news'),
    path('texnalogiya/', texnalogiya_news_view, name='texnalogiya_news' ),
    path('madaniyat/', madaniyat_news_view, name= 'madaniyat_news'),
    path('<slug>/', new_detail_view, name='news_detail'),
]
