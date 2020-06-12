=====
Usage
=====


Use it in your views:

.. code-block:: python

    from next_url_mixin import NextUrlMixin

    class MyView(NextUrlMixin, UpdateView):

        # If you are overriding form_valid(), don't forgot to return the super value with the redirect to the new url
        def form_valid(self, *args, **kwargs):
            return_value = super().form_valid(*args, **kwargs)
            return return_value
