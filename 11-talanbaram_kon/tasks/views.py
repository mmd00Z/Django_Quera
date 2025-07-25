from django.views.decorators.csrf import csrf_exempt
from .models import Task
from django.http import HttpResponse


@csrf_exempt
def list_create_tasks(request):
    if request.method == 'POST':
        task = request.POST.get('task')
        Task.objects.create(name = task)
        return HttpResponse(f'Task Created: \'{task}\'')

