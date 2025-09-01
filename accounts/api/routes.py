from ninja import NinjaAPI

from ..views import router as accounts_router

router = NinjaAPI()

router.add_router("/accounts", accounts_router)

