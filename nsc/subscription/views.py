from django.http import Http404
from django.urls import reverse, reverse_lazy
from django.views import generic

from .forms import (
    CreateStakeholderSubscriptionForm,
    CreateSubscriptionForm,
    ManageSubscriptionsForm,
    SubscriptionStart,
)
from .models import StakeholderSubscription, Subscription
from .signer import check_object, get_object_signature


class GetObjectFromTokenMixin:
    def get_object(self, queryset=None):
        obj = super().get_object(queryset=queryset)

        if not check_object(obj, self.kwargs["token"]):
            raise Http404()

        return obj


class SubscriptionLanding(generic.TemplateView):
    template_name = "subscription/subscription_landing.html"


class PublicSubscriptionStart(generic.FormView):
    form_class = SubscriptionStart
    template_name = "subscription/public_subscription_management_form.html"


class PublicSubscriptionManage(GetObjectFromTokenMixin, generic.UpdateView):
    model = Subscription
    form_class = ManageSubscriptionsForm
    template_name = "subscription/public_subscription_management_form.html"

    def get_success_url(self):
        return reverse(
            "subscription:public-complete",
            kwargs={"pk": self.object.pk, "token": get_object_signature(self.object)},
        )


class PublicSubscriptionEmails(generic.UpdateView):
    model = Subscription
    form_class = CreateSubscriptionForm
    template_name = "subscription/public_subscription_email_form.html"

    def get_initial(self):
        return {"policies": self.request.GET.getlist("policies", [])}

    def get_object(self, queryset=None):
        data = self.request.POST or {}

        return Subscription.objects.filter(email=data.get("email", None)).first()

    def get_success_url(self):
        return reverse(
            "subscription:public-complete",
            kwargs={"pk": self.object.pk, "token": get_object_signature(self.object)},
        )


class PublicSubscriptionComplete(GetObjectFromTokenMixin, generic.DetailView):
    model = Subscription
    template_name = "subscription/public_subscription_complete.html"


class StakeholderSubscriptionStart(generic.CreateView):
    model = StakeholderSubscription
    template_name = "subscription/stakeholder_subscription_creation.html"
    form_class = CreateStakeholderSubscriptionForm
    success_url = reverse_lazy("subscription:stakeholder-complete")


class StakeholderSubscriptionComplete(GetObjectFromTokenMixin, generic.DetailView):
    model = Subscription
    template_name = "subscription/stakeholder_subscription_complete.html"