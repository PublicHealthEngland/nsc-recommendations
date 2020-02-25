from django.contrib import messages
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.views import generic

from nsc.organisation.models import Organisation

from .forms import ContactForm
from .models import Contact


class ContactAdd(generic.CreateView):
    model = Contact
    form_class = ContactForm

    def get_success_url(self):
        msg = _("%s was added successfully" % self.object.name)
        messages.info(self.request, msg)
        return reverse(
            "organisation:detail", kwargs={"pk": self.object.organisation.pk}
        )

    def get_initial(self):
        initial = super().get_initial()

        if self.request.method == "GET":
            initial["organisation"] = Organisation.objects.get(pk=self.kwargs["org_pk"])

        return initial

    def get_context_data(self, **kwargs):
        organisation = Organisation.objects.get(pk=self.kwargs["org_pk"])
        return super().get_context_data(organisation=organisation, **kwargs)


class ContactEdit(generic.UpdateView):
    model = Contact
    form_class = ContactForm

    def get_context_data(self, **kwargs):
        organisation = self.object.organisation
        return super().get_context_data(organisation=organisation, **kwargs)

    def get_success_url(self):
        msg = _("%s was updated successfully" % self.object.name)
        messages.info(self.request, msg)
        return reverse(
            "organisation:detail", kwargs={"pk": self.object.organisation.pk}
        )


class ContactDelete(generic.DeleteView):
    model = Contact

    def get_success_url(self):
        msg = _("%s was deleted successfully" % self.object.name)
        messages.info(self.request, msg)
        return reverse(
            "organisation:detail", kwargs={"pk": self.object.organisation.pk}
        )