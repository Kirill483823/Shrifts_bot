from routers.StartBot import start_router
from routers.Font_process.font_processing import processing_router
from routers.acception_text import accept_text_router
from routers.Font_process.switch_fonts_pages import font_process_router

"""собираем все роутеры папки в кучу"""
def get_routers():
    return [
        start_router,
        processing_router,
        accept_text_router,
        font_process_router
    ]