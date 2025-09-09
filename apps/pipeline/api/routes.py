from ..views  import router as pipeline_router

from   ninja import NinjaAPI

router = NinjaAPI(version="3.0.0", title="Blogify Pipeline API")

router.add_router("/pipeline", pipeline_router)