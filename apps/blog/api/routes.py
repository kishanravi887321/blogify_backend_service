from ninja import NinjaAPI
from ..views import router as blog_router
router = NinjaAPI()

router.add_router("", blog_router)