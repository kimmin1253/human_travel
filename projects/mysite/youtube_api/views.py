from django.shortcuts import render
from youtube_api.models import YouTubeVideo

def video_list(request):
    """
    저장된 동영상 리스트를 불러와 HTML로 렌더링.
    """
    videos = YouTubeVideo.objects.filter(captions__isnull=False)  # ✅ 자막이 있는 것만 필터링

    return render(request, "video_list.html", {"videos": videos})  # ✅ 변경된 경로 반영