from django.urls import path
from .views import AddEmployeeView,AddAssetView,\
   DelegateToView,WhenGiveAndReturnView,ConditionGiveAndReturnView,\
   UserLoginView,UserRegistrationView



urlpatterns = [
   path('signup',UserRegistrationView.as_view()),
   path('login',UserLoginView.as_view()),
   path('add-employee/',AddEmployeeView.as_view()),
   path('add-asset/',AddAssetView.as_view()),
   path('delegate-to/',DelegateToView.as_view()),
   path('see-when/<int:pk>/',WhenGiveAndReturnView.as_view()),
   path('condition/<int:pk>/',ConditionGiveAndReturnView.as_view()),
    
]