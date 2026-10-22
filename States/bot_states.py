from aiogram.fsm.state import State, StatesGroup

class States_for_pages(StatesGroup):
    be_on_page1 = State()
    be_on_page2 = State()

class States_bot(StatesGroup):
    be_in_main_menu = State()
    wait_send_text = State()
    choosen_shrifts = State()
