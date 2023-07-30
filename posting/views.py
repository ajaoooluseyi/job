from django.http import JsonResponse

from .models import JobPosition


def get_job_positions(request):
    job_positions = JobPosition.objects.all().values()
    return JsonResponse({"job_positions": list(job_positions)})


def search_job_positions(request):
    if request.method == "GET":
        selected_job = request.GET.get("selected_job", "")
        job_positions = JobPosition.objects.filter(
            title__icontains=selected_job
        ).values()
        return JsonResponse({"job_positions": list(job_positions)})
    else:
        return JsonResponse({"error": "Invalid request method."}, status=400)
