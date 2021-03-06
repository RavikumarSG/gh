from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(User)
    show_email = models.BooleanField(default=False)
    use_gravatar = models.BooleanField(default=False)
    info = models.TextField(blank=True)
    
    # Professional
    company = models.TextField(blank=True)
    company_url = models.URLField(blank=True)
    job_title = models.TextField(blank=True)
    skills = models.TextField(blank=True)
    interested_in_job_opportunities = models.BooleanField(default=False)
    
    # Social Networks
    bitbucket_url = models.URLField(blank=True)
    dribbble_url = models.URLField(blank=True)
    facebook_url = models.URLField(blank=True)
    github_url = models.URLField(blank=True)
    google_plus_url = models.URLField(blank=True)
    linked_in_url = models.URLField(blank=True)
    stack_overflow_url = models.URLField(blank=True)
    tumblr_url = models.URLField(blank=True)
    twitter_url = models.URLField(blank=True)
    
    # Projects
    project_1_name = models.TextField(blank=True)
    project_1_url = models.URLField(blank=True)
    project_2_name = models.TextField(blank=True)
    project_2_url = models.URLField(blank=True)
    project_3_name = models.TextField(blank=True)
    project_3_url = models.URLField(blank=True)
    project_4_name = models.TextField(blank=True)
    project_4_url = models.URLField(blank=True)
    project_5_name = models.TextField(blank=True)
    project_5_url = models.URLField(blank=True)
    
    # Elsewhere on the Web
    elsewhere_1_name = models.TextField(blank=True)
    elsewhere_1_url = models.URLField(blank=True)
    elsewhere_2_name = models.TextField(blank=True)
    elsewhere_2_url = models.URLField(blank=True)
    elsewhere_3_name = models.TextField(blank=True)
    elsewhere_3_url = models.URLField(blank=True)
    elsewhere_4_name = models.TextField(blank=True)
    elsewhere_4_url = models.URLField(blank=True)
    elsewhere_5_name = models.TextField(blank=True)
    elsewhere_5_url = models.URLField(blank=True)
    
    def __unicode__(self):
        return self.user.username
    
    def get_absolute_url(self):
        return reverse('profile-detail', kwargs={'username': self.user.username})
    
    def get_short_name(self):
        if self.user.first_name:
            return self.user.first_name
        else:
            return self.user.username
    
    def get_full_name(self):
        if self.user.first_name and self.user.last_name:
            return "%s %s" % (self.user.first_name, self.user.last_name)
        elif self.user.first_name:
            return self.user.first_name
        else:
            return self.user.username
    
    def has_projects(self):
        return self.project_1_url or \
               self.project_2_url or \
               self.project_3_url or \
               self.project_4_url or \
               self.project_5_url

    def has_elsewhere(self):
        return self.elsewhere_1_url or \
               self.elsewhere_2_url or \
               self.elsewhere_3_url or \
               self.elsewhere_4_url or \
               self.elsewhere_5_url
