from django.views.generic import ListView
from ..models import Task


class Tasks(ListView):
    model = Task
    template_name = "tasks/task_list.html"
    context_object_name = "tasks"

    def get_queryset(self):
        data = super().get_queryset()

        status = self.request.GET.get("status")

        if status in Task.Status.values:
            data = data.filter(status=status)

        return data
