import fastapi
from fastapi.middleware.cors import CORSMiddleware
from src.api.endpoints import router as api_endpoint_router
from src.config.manager import settings


def initialize_order_application() -> fastapi.FastAPI:
    app = fastapi.FastAPI(**settings.set_order_app_attributes)  # type: ignore

    # ✅ Root endpoint for browser/homepage
    @app.get("/")
    def root():
        return {"message": "Order Service is Running ✅"}

    # ✅ Health check endpoint
    @app.get("/health")
    def health_check():
        return {"status": "healthy"}

    # Middleware for CORS
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ALLOWED_ORIGINS,
        allow_credentials=settings.IS_ALLOWED_CREDENTIALS,
        allow_methods=settings.ALLOWED_METHODS,
        allow_headers=settings.ALLOWED_HEADERS,
    )

    # API router with prefix from settings
    app.include_router(router=api_endpoint_router, prefix=settings.API_PREFIX)

    return app


app: fastapi.FastAPI = initialize_order_application()
