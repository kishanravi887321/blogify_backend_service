from ninja import NinjaAPI
from ..views import router as blog_router

router = NinjaAPI(version="2.0.0", title="Blogify Blog API")

router.add_router("", blog_router)