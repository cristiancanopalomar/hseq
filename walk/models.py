# -*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from rename import rename_file
from .tasks import email_commitments
from django.utils.translation import ugettext_lazy as _


class Findings(models.Model):
    description = models.CharField(
        max_length=50,
    )

    class Meta:
        unique_together = ('description',)
        verbose_name = u'Finding'
        verbose_name_plural = u'Findings'

    def __unicode__(self):
        return unicode(self.description)


class Walks(models.Model):
    available_companies = (
        (
            'C-OI',
            'cam, operación integral'),
        (
            'M-OI',
            'micol, operación integral'
        ),
        (
            'W-OI',
            'WSP, operación integral'
        ),
    )
    number_walk = models.CharField(
        max_length=15,
        primary_key=True,
        unique=True,
        help_text='number of walk',
    )
    creation_walks = models.DateTimeField(
        _('creation date'),
        auto_now_add=True,
        help_text='item creation date',
    )
    company = models.CharField(
        max_length=4,
        choices=available_companies,
    )
    activity = models.CharField(
        max_length=50,
    )
    place = models.PositiveIntegerField()
    accomplished = models.CharField(
        _('accomplished by'),
        max_length=20,
    )
    responsible = models.CharField(
        _('responsible of activity'),
        max_length=20,
    )
    good_practices = models.TextField()
    findings = models.ManyToManyField(
        Findings,
        help_text='characterization of the findings',
    )
    comments_findings = models.TextField(
        help_text='comments of findings',
    )
    feedback_comments = models.TextField(
        help_text='feedback and comments',
    )
    image_1 = models.ImageField(
        upload_to=rename_file(
            'upload/hseq/walk/walks/',
        ),
    )
    image_2 = models.ImageField(
        upload_to=rename_file(
            'upload/hseq/walk/walks/',
        ),
        blank=True,
    )
    image_3 = models.ImageField(
        upload_to=rename_file(
            'upload/hseq/walk/walks/',
        ),
        blank=True,
    )
    accompaniment = models.CharField(
        max_length=25,
        blank=True,
    )
    registered = models.ForeignKey(
        User,
        help_text='registrado by user'
    )

    class Meta:
        unique_together = ('number_walk', 'creation_walks', 'registered',)
        verbose_name = u'Walk'
        verbose_name_plural = u'Walks'

    def __unicode__(self):
        return unicode(self.number_walk)


class Commitments(models.Model):
    number_walk = models.ForeignKey(
        Walks,
    )
    description = models.CharField(
        max_length=150,
    )
    date = models.DateTimeField(
        auto_now_add=True,
    )
    user_name = models.CharField(
        max_length=25,
    )
    closing = models.BooleanField(
        default=False,
    )

    class Meta:
        unique_together = ('number_walk', 'description', 'user_name',)
        verbose_name = u'Commitment'
        verbose_name_plural = u'Commitments'

    def __unicode__(self):
        return unicode(self.number_walk)

# signals
@receiver(post_save, sender=Commitments)
def signals_commitments(sender, instance, created, **kwargs):
    if created:
        fm_em = Walks.objects.all().values_list(
            'registered__email',
            flat=True,
        ).filter(
            number_walk=instance.number_walk,
        )
        to_em = User.objects.all().values_list(
            'email',
            flat=True,
        ).filter(
            user_name=instance.user_name,
        )
        nb_wl = instance.number_walk
        ds_wl = instance.description
        email_commitments.delay(fm_em, to_em, nb_wl, ds_wl)


class Supports(models.Model):
    commitments = models.ForeignKey(
        Commitments,
    )
    support = models.ImageField(
        upload_to=rename_file(
            'upload/hseq/walk/supports/',
        ),
    )
    date = models.DateTimeField(
        auto_now_add=True,
    )
    description = models.TextField()

    class Meta:
        verbose_name = u'Support'
        verbose_name_plural = u'Supports'

    def __unicode__(self):
        return unicode(self.commitments)

# signals
@receiver(post_save, sender=Supports)
def signals_supports(sender, instance, created, **kwargs):
    if created:
        Commitments.objects.all().filter(
            id=instance.commitments,
        ).update(
            closing=True,
        )
