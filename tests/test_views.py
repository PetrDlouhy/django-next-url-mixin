#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-next-url-mixin
------------

Tests for `django-next-url-mixin` models module.
"""

from django import forms
from django.http import HttpResponseRedirect
from django.test import RequestFactory
from django.test import TestCase
from django.views.generic.edit import FormView

from next_url_mixin.mixin import NextUrlMixin


class NextView(NextUrlMixin, FormView):
    form_class = forms.Form
    template_name = 'foo.html'
    success_url = '/success'


class TestNext_url_mixin(TestCase):

    def setUp(self):
        self.request_factory = RequestFactory()

    def test_next_url_redirect(self):
        t = NextView()
        request = self.request_factory.post('/foo?next=bar')
        t.request = request
        response = t.dispatch(request)
        expected_response = HttpResponseRedirect('bar')
        self.assertEquals(response.status_code, expected_response.status_code)
        self.assertEquals(response.url, expected_response.url)

    def test_next_url_forbidden(self):
        t = NextView()
        request = self.request_factory.post('/foo?next=http://bar.com')
        t.request = request
        response = t.dispatch(request)
        expected_response = HttpResponseRedirect('/success')
        self.assertEquals(response.status_code, expected_response.status_code)
        self.assertEquals(response.url, expected_response.url)

    def test_no_next_url(self):
        t = NextView()
        request = self.request_factory.post('/foo')
        t.request = request
        response = t.dispatch(request)
        expected_response = HttpResponseRedirect('/success')
        self.assertEquals(response.status_code, expected_response.status_code)
        self.assertEquals(response.url, expected_response.url)

    def test_next_url_local(self):
        t = NextView()
        request = self.request_factory.post('/foo?next=http://testserver/baz')
        t.request = request
        response = t.dispatch(request)
        expected_response = HttpResponseRedirect('http://testserver/baz')
        self.assertEquals(response.status_code, expected_response.status_code)
        self.assertEquals(response.url, expected_response.url)
