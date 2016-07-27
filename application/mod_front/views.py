import requests
import forms
from application.views import BaseView
from flask import request


class FrontForm(BaseView):

    def dispatch_request(self, **args):
        # need to validate these in the dispatch
        self.args = args
        self.front_form = forms.Front()
        if request.method == 'POST':
            # validates the form
            if self.product_form.validate_on_submit():
                print "validated"
            else:
                print 'not validated '
            return self.display_template()
        else:
            # displays an empty form
            return self.display_template()

    def template_location(self):
        return 'main.html'