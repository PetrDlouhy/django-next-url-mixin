from typing import Set

from django.http import HttpResponseRedirect


try:
    from django.utils.http import url_has_allowed_host_and_scheme
except ImportError:  # Django < 3.0
    from django.utils.http import is_safe_url as url_has_allowed_host_and_scheme


class SuccessURLAllowedHostsMixin:
    success_url_allowed_hosts: Set[str] = set()

    def get_success_url_allowed_hosts(self):
        return {self.request.get_host(), *self.success_url_allowed_hosts}


class GetNextPageMixin(SuccessURLAllowedHostsMixin):
    next_url_param_name = "next"

    def get_next_page(self):
        if (
            self.next_url_param_name in self.request.POST
            or self.next_url_param_name in self.request.GET
        ):
            next_url = self.request.POST.get(
                self.next_url_param_name,
                self.request.GET.get(self.next_url_param_name),
            )
            url_is_safe = url_has_allowed_host_and_scheme(
                url=next_url,
                allowed_hosts=self.get_success_url_allowed_hosts(),
                require_https=self.request.is_secure(),
            )
            if url_is_safe:
                return next_url


class NextUrlMixin(GetNextPageMixin):
    def form_valid(self, *args, **kwargs):
        ret_val = super().form_valid(*args, **kwargs)
        next_page = self.get_next_page()
        if next_page:
            return HttpResponseRedirect(next_page)
        return ret_val
