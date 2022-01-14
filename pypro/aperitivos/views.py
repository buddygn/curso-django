from django.shortcuts import render, get_object_or_404

from pypro.aperitivos.models import Video


def indice(request):
    videos = Video.objects.all().order_by('creation')
    return render(request, 'aperitivos/indice.html', context={'videos': videos})


def video(request, slug):
    video_obj = get_object_or_404(Video, slug=slug)
    return render(request, 'aperitivos/video.html', context={'video': video_obj})
