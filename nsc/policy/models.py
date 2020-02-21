from datetime import date

from django.db import models
from django.urls import reverse
from django.utils.text import slugify
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.models import TimeStampedModel
from model_utils import Choices
from simple_history.models import HistoricalRecords

from nsc.utils.markdown import convert

from .fields import ChoiceArrayField


class PolicyQuerySet(models.QuerySet):
    def active(self):
        return self.filter(is_active=True)

    def review_due(self):
        year = date.today().year
        return self.filter(next_review__year=year)


class Policy(TimeStampedModel):

    AGE_GROUPS = Choices(
        ("antenatal", _("Antenatal")),
        ("newborn", _("Newborn")),
        ("child", _("Child")),
        ("adult", _("Adult")),
        ("all", _("All ages")),
    )

    name = models.CharField(verbose_name=_("name"), max_length=256)
    slug = models.SlugField(verbose_name=_("slug"), max_length=256, unique=True)

    is_active = models.BooleanField(verbose_name=_("is_active"), default=True)
    is_screened = models.BooleanField(verbose_name=_("is_screened"), default=False)
    last_review = models.DateField(verbose_name=_("last review"), null=True, blank=True)
    next_review = models.DateField(verbose_name=_("next review"), null=True, blank=True)

    ages = ChoiceArrayField(
        models.CharField(
            verbose_name=_("age groups"), choices=AGE_GROUPS, max_length=50
        )
    )

    condition = models.TextField(verbose_name=_("condition"))
    condition_html = models.TextField(verbose_name=_("HTML condition"))

    policy = models.TextField(verbose_name=_("policy"))
    policy_html = models.TextField(verbose_name=_("HTML policy"))

    history = HistoricalRecords()
    objects = PolicyQuerySet.as_manager()

    class Meta:
        ordering = ("name", "pk")
        verbose_name_plural = _("policies")

    def __str__(self):
        return self.name

    def get_public_url(self):
        return reverse("condition:detail", kwargs={"slug": self.slug})

    def get_admin_url(self):
        return reverse("policy:detail", kwargs={"slug": self.slug})

    def get_edit_url(self):
        return reverse("policy:edit", kwargs={"slug": self.slug})

    def recommendation_display(self):
        return _("Recommended") if self.is_screened else _("Not recommended")

    def last_review_display(self):
        return (
            self.last_review.strftime("%b %Y")
            if self.last_review
            else _("This policy has not been reviewed")
        )

    def next_review_display(self):
        today = date.today()
        if self.next_review is None:
            return _("No review has been scheduled")
        if self.next_review < today:
            return _("Overdue")
        else:
            return self.next_review.strftime("%b %Y")

    def ages_display(self):
        return ", ".join(str(Policy.AGE_GROUPS[age]) for age in self.ages)

    def clean(self):
        if not self.slug:
            self.slug = slugify(self.name)
        self.condition_html = convert(self.condition)
        self.policy_html = convert(self.policy)
