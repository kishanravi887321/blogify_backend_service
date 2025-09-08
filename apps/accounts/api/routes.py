from ninja import NinjaAPI

from ..views import router as accounts_router

router = NinjaAPI(version="1.0.0", title="Blogify Accounts API")

router.add_router("", accounts_router)

