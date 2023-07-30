from django.http import JsonResponse

from .models import JobPosition


def get_job_positions(request):
    job_positions = JobPosition.objects.all().values()
    return JsonResponse({"job_positions": list(job_positions)})
