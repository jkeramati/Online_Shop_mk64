from django.views.generic import FormView

from home.form import ContactEmailForm


# class ContactEmailFormView(FormView):
#     form_class = ContactEmailForm
#     success_url = 'index'
#     template_name = 'base/_footer.html'
#
#     def get_context_data(self, **kwargs):
#         return super().get_context_data(**kwargs)

def contact_send_email(request):
    # print('contact email form', ContactEmailForm())
    return {
        'mail': ContactEmailForm()
    }
