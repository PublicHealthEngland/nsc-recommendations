from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.http import HttpResponse
from django.urls import include, path

from nsc.review.views import ReviewDashboardView


admin.autodiscover()

urlpatterns = [
    path(r"", ReviewDashboardView.as_view(), name="dashboard"),
    path(r"admin/", admin.site.urls),
    path(r"condition/", include("nsc.condition.urls", namespace="condition")),
    path(r"contact/", include("nsc.contact.urls", namespace="contact")),
    path(r"document/", include("nsc.document.urls", namespace="document")),
    path(r"organisation/", include("nsc.organisation.urls", namespace="organisation")),
    path(r"policy/", include("nsc.policy.urls", namespace="policy")),
    path(r"review/", include("nsc.review.urls", namespace="review")),
    path(r"_health/", lambda request: HttpResponse()),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if "debug_toolbar" in settings.INSTALLED_APPS:
    import debug_toolbar

    urlpatterns += [path(r"__debug__/", include(debug_toolbar.urls))]
