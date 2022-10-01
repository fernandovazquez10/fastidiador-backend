from FastidiadorBackend.utils import CustomRouter
from main.views import StatusDiaViewSet, UserCursoViewSet

app_name = "main"

router = CustomRouter()
router.register(r'status-dia', StatusDiaViewSet)
router.register(r'user-curso', UserCursoViewSet)
