from django.urls import path
from .views import ServiceListView,ServiceDetailView,ContactsView,BlogsListView,BlogDetailView,ClientTicketView,DeviceGetSerializerView,DeviceListView,EstimateCreateView
urlpatterns = [
    path("service/",ServiceListView.as_view(),name="service"),
    path("service/<slug:slug>/",ServiceDetailView.as_view(),name="service-detail"),
    path("blogs/",BlogsListView.as_view(),name="blogs"),
    path("blog/<slug:slug>/",BlogDetailView.as_view(),name="blog-detail"),
    path("client/<slug:ticket>/",ClientTicketView.as_view(),name="client-ticket"),
    path("contact/",ContactsView.as_view(),name="contact"),
    path('repair/',DeviceGetSerializerView.as_view(),name="repair"),
    path('device/',DeviceListView.as_view(),name="device"),
    path('estimate/',EstimateCreateView.as_view(),name="estimate")
]