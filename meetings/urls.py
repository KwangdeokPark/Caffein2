from django.urls import path

from .views import (
    EveryMeetingListView,
    OfficialMeetingCreateView,
    OfficialMeetingUpdateView,
    OfficialMeetingDeleteView,
    OfficialMeetingDetailView,
    OfficialMeetingListView,
    CoffeeEducationCreateView,
    CoffeeEducationUpdateView,
    CoffeeEducationDeleteView,
    CoffeeEducationListView,
    CoffeeEducationDetailView,
    participate_meeting,
)

app_name = 'meetings'

urlpatterns = [
    path('', EveryMeetingListView.as_view(), name='meetings-list'),
    path('official/create/', OfficialMeetingCreateView.as_view(), name='official-create'),
    path('official/update/<int:pk>/', OfficialMeetingUpdateView.as_view(), name='official-update'),
    path('official/delete/<int:pk>/', OfficialMeetingDeleteView.as_view(), name='official-delete'),
    path('official/', OfficialMeetingListView.as_view(), name='official-list'),
    path('official/<int:pk>/', OfficialMeetingDetailView.as_view(), name='official-detail'),

    path('education/create/', CoffeeEducationCreateView.as_view(), name='education-create'),
    path('education/update/<int:pk>/', CoffeeEducationUpdateView.as_view(), name='education-update'),
    path('education/delete/<int:pk>/', CoffeeEducationDeleteView.as_view(), name='education-delete'),
    path('education/<int:pk>/', CoffeeEducationDetailView.as_view(), name='education-detail'),
    path('education/', CoffeeEducationListView.as_view(), name='education-list'),

    path('participate/<int:pk>/', participate_meeting, name='participate'),

]