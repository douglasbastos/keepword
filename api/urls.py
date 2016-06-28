# coding: utf-8
from rest_framework import routers
# from django.conf.urls import url, include
# from django.contrib import admin
from .views import FeedbackViewSet, WordViewSet
# from django.views.generic import TemplateView

router = routers.DefaultRouter()
router.register(r'feedbacks', FeedbackViewSet)
router.register(r'words', WordViewSet)

urlpatterns = router.urls
# url(r'^', include(router.urls)),
# url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
# url(r'^admin/', admin.site.urls),
# url(r'^next_question/', views.next_question),
# url(r'^base/$', TemplateView.as_view(template_name='result.html'))
