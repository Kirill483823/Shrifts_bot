from aiogram.fsm.state import State, StatesGroup

#Обработка кнопок переключения сраниц для шрифтов
class States_for_pages(StatesGroup):
    be_on_page1 = State()
    be_on_page2 = State()

class States_for_pages_for_simbols(StatesGroup):
    page_1_for_simbols = State()
    page_2_for_simbols = State()


class States_bot(StatesGroup):
    be_in_main_menu = State()
    wait_send_text = State()
    choosen_shrifts = State()
