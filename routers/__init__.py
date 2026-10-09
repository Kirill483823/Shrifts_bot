from routers.StartBot import start_router
from routers.font_processing import processing_router

"""собираем все роутеры папки в кучу"""
def get_routers():
    return [
        start_router,
        processing_router
    ]