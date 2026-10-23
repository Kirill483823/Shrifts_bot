import fancify_text
ORIGINAL = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
ORIGINAL_RU = f"{ORIGINAL}АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклмнопрстуфхцчшщъыьэюя"

# --- Латиница (ровно 52 символа) ---

script_regular_dict = (
    "𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵"
    "𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏"
)

def script_regular(text: str) -> str:
    table = str.maketrans(ORIGINAL, script_regular_dict)
    return text.translate(table)

runic_dict = (
    "ᚨᛒᚲᛞᛖᚠᚷᚺᛁᛃᚴᛚᛗᚾᛟᛈᛩᚱᛋᛏᚢᚡᚹᛪᛦᛉ"
    "ᚨᛒᚲᛞᛖᚠᚷᚺᛁᛃᚴᛚᛗᚾᛟᛈᛩᚱᛋᛏᚢᚡᚹᛪᛦᛉ"
)[:52]  # ровно 52

def runic(text: str) -> str:
    table = str.maketrans(ORIGINAL, runic_dict)
    return f"{text.translate(table)}"

antic_dict = (
    "ꋬꃳꉔ꒯ꏂꊰꍌꀿ꒐꒻ꀘ꒒ꈴꈤꄲꃀꆰꋪꇙ꓄꒤꒦ꅐꉧꌦꁴ"
    "ꋬꃳꉔ꒯ꏂꊰꍌꀿ꒐꒻ꀘ꒒ꈴꈤꄲꃀꆰꋪꇙ꓄꒤꒦ꅐꉧꌦꁴ"
)[:52]

def antic(text: str) -> str:
    table = str.maketrans(ORIGINAL, antic_dict)
    return text.translate(table)


# --- Латиница + кириллица (ровно 118 символов) ---

handwritten_dict = ("ᥲbᥴᦔᥱ𐔥ⳋhιjkᥣⲙᥒ𐔖ρqr᥉tᥙ᥎ᥕ᥊𐔤zᥲbᥴᦔᥱ𐔥ⳋhιjkᥣⲙᥒ𐔖ρqr᥉tᥙ᥎ᥕ᥊𐔤zᥲⳝ"\
"ⲃ𐔏ⲇᥱᥱⲿⳅυύⲕ᥈ⲙⲏ𐔖ᥒρᥴⲧ𐔤ⲫⲭцɥɯպ𐔊ыьⲉюяᥲⳝⲃ𐔏ⲇᥱᥱⲿⳅυύⲕ᥈ⲙⲏ𐔖ᥒρᥴⲧ𐔤ⲫⲭцɥɯպ𐔊ыьⲉюя"
)[:118]

def handwritten(text: str) -> str:
    table = str.maketrans(ORIGINAL_RU, handwritten_dict)
    return f"🇷🇺{text.translate(table)}"

# --- Остальные стили: ровно 52 или 118, без «лишнего» ---

asian_dict =("卂乃匚ᗪ乇千Ꮆ卄丨丁片乚爪几口尸Ɋ尺丂十凵ᐯ山乂ㄚ乙卂乃匚ᗪ乇千Ꮆ卄丨丁片乚爪几口尸Ɋ尺丂十凵ᐯ山乂ㄚ乙卂乃ᐯᎶᗪ乇乇乙卄乙丨ㄚ片乚爪几口尸尺丂十凵千卄匚匚卄丂卄丂匚卄ㄚ乇ㄚ凵ㄚ卂卂"\
    "乃ᐯᎶᗪ乇乇乙卄乙丨ㄚ片乚爪几口尸尺丂十凵千卄匚匚卄丂卄丂匚卄ㄚ乇ㄚ凵ㄚ卂")[:118]

def asian(text: str) -> str:
    table = str.maketrans(ORIGINAL_RU, asian_dict)
    return text.translate(table)

aphiopy = (
    "ልፔፎናሏይይሦንሀህኸበጠዘዐከየርፐነዋጰህሃሠሡፘፊሪጓሬጸ"
    "ልፔፎናሏይይሦንሀህኸበጠዘዐከየርፐነዋጰህሃሠሡፘፊሪጓሬጸ"
)[:118]

def aphiopy_style(text: str) -> str:
    table = str.maketrans(ORIGINAL_RU, aphiopy)
    return f"🇷🇺{text.translate(table)}"

chain = (
    "刄乃匚冂㠪乇彑卄エ丿片し冊力口戶디尺丂匕나ᜠ丗义ソ之刄乃匚冂㠪"
    "乇彑卄エ丿片し冊力口戶디尺丂匕나ᜠ丗义ソ之丹万乃厂冎仨仨水"
    "弓丩以⻓入从什口丌尸仁丁丫中乂㇉나山山⻜⻜|⻜彐扣牙丹万乃"
    "厂冎仨仨水弓丩以⻓入从什口丌尸仁丁丫中乂㇉나山山⻜⻜|⻜彐"
)[:118]

def chain_style(text: str) -> str:
    table = str.maketrans(ORIGINAL_RU, chain)
    return f"🇷🇺{text.translate(table)}"

grecgesky = (
    "ΑΒϹΔΕΦΓΗΙΙΚΛΜΝΟΠΘΡΣΤΥVΩΧΥΖαβϲδεφγηιϳκλμνοπθρστυνωχψζΑБΒΓΔΕ"
    "ЕЖЗИЙΚΛΜΗΟΠΡϹΤΥΦΧЦЧШЩЪЫЬЭЮЯⲁⳝⲃⲅⲇⲉⲉⲿⳅυύⲕⲗⲙⲏⲟⲡⲣⲥⲧⲩⲫⲭⳡ"
    "ɥⲱպъыьⲉюяΑΒϹΔΕΦΓΗΙΙΚΛΜΝΟΠΘΡΣΤΥVΩΧΥΖαβϲδεφγηιϳκλμνοπθρ"
)[:118]

def grecgesky_style(text: str) -> str:
    table = str.maketrans(ORIGINAL_RU, grecgesky)
    return f"🇷🇺{text.translate(table)}"

capital_dict ="ᴀʙᴄᴅᴇꜰɢʜɪᴊᴋʟᴍɴᴏᴘǫʀsᴛᴜᴠᴡxʏᴢᴀбʙᴦдᴇёжзийᴋᴧʍноᴨᴩᴄᴛуɸхцчɯщъыь϶юя"
def capital(text):
    ORIGINAL_CAP = "ABCDEFGHIJKLMNOPQRSTUVWXYZАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
    table = str.maketrans(ORIGINAL_CAP, capital_dict)
    return f"🇷🇺{text.translate(table)}"


shrifts_dict_page1 = { #список функций преобразователей
    "sans_serif": fancify_text.sansSerif,
    "bold": fancify_text.bold,
    "italic": fancify_text.italic,
    "italic_serif": fancify_text.italicSerif,
    "bold_italic": fancify_text.boldItalic,
    "bold_italic_serif": fancify_text.boldItalicSerif,
    "monospace": fancify_text.monospaced,
    "wide": fancify_text.wide,
    "bold_serif": fancify_text.boldSerif,
    "script": fancify_text.script,
    "fraktur": fancify_text.fraktur,
    "bold_fraktur": fancify_text.boldFraktur,
    "doubleStruck": fancify_text.doubleStruck,
    "blue": fancify_text.blue,
    "smallCaps": fancify_text.smallCaps,
    "handwritten": handwritten,
    "script_regular": script_regular,
    "grecgesky_style": grecgesky_style,
    "asian": asian,
    "capital": capital
}

shrifts_dict_page2 = {
    "curly": fancify_text.curly,
    "boxed": fancify_text.boxed,
    "circled": fancify_text.circled,
    "squared": fancify_text.squared,
    "superscript": fancify_text.superscript,
    "parenthesized": fancify_text.parenthesized,
    "heavyCircled": fancify_text.heavyCircled,
    "currency": fancify_text.currency,
    "cool": fancify_text.cool,
    "magic": fancify_text.magic,
    "script_regular": script_regular,
    "runic": runic,
    "antic": antic,
    "reversed_": fancify_text.reversed_,
    "upsideDown": fancify_text.upsideDown,
    "chain_style": chain_style,

}