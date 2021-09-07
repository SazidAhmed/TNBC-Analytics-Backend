from django.urls import path

from rest_framework.routers import SimpleRouter
from rest_framework.urlpatterns import format_suffix_patterns

from .views.transaction import TransactionListView
from .views.government import GovernmentViewSet
from .views.treasury import TreasuryViewSet
from .views.scan_chain import ChainScan
from .views.charts import TreasuryChart, GovernmentChart, HomepageChart
from .views.statistics import StatisticsViewSet

router = SimpleRouter(trailing_slash=False)
router.register('transaction', TransactionListView)
router.register('government', GovernmentViewSet)
router.register('treasury', TreasuryViewSet)
router.register('statistics', StatisticsViewSet)

urlpatterns = [
    path('chain-scan', ChainScan.as_view()),
    path('treasury-chart', TreasuryChart.as_view()),
    path('government-chart', GovernmentChart.as_view()),
    path('homepage-chart', HomepageChart.as_view())
]

urlpatterns = format_suffix_patterns(urlpatterns)
