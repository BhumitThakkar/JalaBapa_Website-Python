from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import *
# Create your views here.

class PublicationsView(generic.ListView):
    template_name = "publications/publications.html"
    context_object_name = "all_publications"

    def get_queryset(self):
        return Publications.objects.all()


# def publications(request):
#     all_files = Publications.objects.all()
#     uploaded_file_names = []
#     for obj in all_files:
#         uploaded_file_names.append(str(obj.file_name()))
#         context = {
#         'uploaded_file_names': uploaded_file_names
#         }
#     return render(request, 'publications/publications.html', context)


class PublicationsDetailView(generic.DetailView):
    model = Publications
    template_name = "publications/details.html"

# def pdfs(request, file_name):
#
#     file_full_path = 'media/pdfs/' + file_name
#     with open(file_full_path, 'r') as pdf:
#         data = pdf.read()
#         response = HttpResponse(data, content_type='application/pdf')
#         response['Content-Disposition'] = "attachment; filename='"+file_name+"'"
#         return response
