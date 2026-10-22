import fancify_text

ORIGINAL = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

script_regular_dict= "𝒜ℬ𝒞𝒟ℰℱ𝒢ℋℐ𝒥𝒦ℒℳ𝒩𝒪𝒫𝒬ℛ𝒮𝒯𝒰𝒱𝒲𝒳𝒴𝒵𝒶𝒷𝒸𝒹ℯ𝒻ℊ𝒽𝒾𝒿𝓀𝓁𝓂𝓃ℴ𝓅𝓆𝓇𝓈𝓉𝓊𝓋𝓌𝓍𝓎𝓏"
def script_regular(text: str):
    table = str.maketrans(ORIGINAL, script_regular_dict)
    return text.translate(table)

runic_dict = "ᚨᛒᚲᛞᛖᚠᚷᚺᛁᛃᚴᛚᛗᚾᛟᛈᛩᚱᛋᛏᚢᚡᚹᛪᛦᛉᚨᛒᚲᛞᛖᚠᚷᚺᛁᛃᚴᛚᛗᚾᛟᛈᛩᚱᛋᛏᚢᚡᚹᛪᛦᛉ"
def runic(text: str):
    table = str.maketrans(ORIGINAL, runic_dict)
    return text.translate(table)


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
    "double_struck": fancify_text.doubleStruck,
    "blue": fancify_text.blue,
    "smallCaps": fancify_text.smallCaps,
}

shrifts_dict_page2 = {
    "curly": fancify_text.curly,
    "reversed_": fancify_text.reversed_,
    "upsideDown": fancify_text.upsideDown,
    "boxed": fancify_text.boxed,
    "circled": fancify_text.circled,
    "squared": fancify_text.squared,
    "superscript": fancify_text.superscript,
    "wiry": fancify_text.wiry,
    "parenthesized": fancify_text.parenthesized,
    "heavyCircled": fancify_text.heavyCircled,
    "currency": fancify_text.currency,
    "cool": fancify_text.cool,
    "magic": fancify_text.magic,
    "script_regular": script_regular,
    "runic": runic,
}
