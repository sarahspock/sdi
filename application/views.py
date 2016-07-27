import abc
from flask.views import View
from flask import render_template


class BaseView(View):
    __metaclass__ = abc.ABCMeta

    def dispatch_request(self, **args):
        """
        This is called when the view is called.
        :return: The template.
        """
        self.args = args
        return self.display_template()

    def context(self):
        """
        :return: Data to pass into the template, in the form of a dictionary.
        """
        return {}

    def display_template(self):
        """
        :return: The final template.
        """
        print str(self.context())
        return render_template(self.template_location(), **self.context())

    @abc.abstractmethod
    def template_location(self):
        """
        :return: String. The location of the template we are using to display this view.
        """
        raise NotImplementedError()