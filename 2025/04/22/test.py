import re

def max_matrix(user_list: list):
    m = user_list[0][0]
    for diag in range(1, 8):
        if user_list[diag][diag] > m:
            m = user_list[diag][diag]
    return m

def string_work(user_str: str):
    quanity_words = len(user_str.split())
    new_str = ''
    cons_letters = 'б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ, b, c, d, f, g, h, j, k, l, m, n, p, q, r, s, t, v, w, x, y, z'.split(', ')
    for lett in user_str:
        if lett.lo in cons_letters:
            new_str += lett
    return (quanity_words, new_str)

def phone_num(user_phone: str):
    code = re.findall(r"\d+", user_phone)
    return(code)

print(phone_num("(918)786-54-33"))
