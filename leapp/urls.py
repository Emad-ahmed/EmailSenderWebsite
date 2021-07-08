from django.urls import path
from leapp.views import HomeView, HistoryView, LoginView, SettingView, SubcriptionView, SignupView, user_logout, showemail

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('history/', HistoryView.as_view(), name='history'),
    path('login/', LoginView.as_view(), name='login'),
    path('settings/', SettingView.as_view(), name='setting'),
    path('subcription/', SubcriptionView.as_view(), name='subcription'),
    path('signup/', SignupView.as_view(), name='signup'),
    path('user_logout/', user_logout, name='user_logout'),
    path('showemail/<int:id>', showemail, name='showemail'),
]
