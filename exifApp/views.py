from django.views.generic import TemplateView

class Home(TemplateView):
    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['file_list'] = self.request.user.user_file.all()
        return context