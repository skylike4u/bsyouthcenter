from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


# include를 통해 하위분개 실시
urlpatterns = [
    path("", include("core.urls")),
    path("articles/", include("articles.urls")),
    path("profiles/", include("profiles.urls")),
    path("users/", include("users.urls")),
    path("comments/", include("comments.urls")),
    path("blogs/", include("blogs.urls")),
    path("admin/", admin.site.urls),
]


# 우선 urlpatterns에서 static을 가져와 줌. static의 인자로 settings을 가져와 줌
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT,
    )
# DEBUG가 True라면(프로덕션이 아니라 개발중이라면), urlpatterns += (urlpatterns에 += 하나더 추가할거다)
