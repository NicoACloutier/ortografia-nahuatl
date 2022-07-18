import re

esp_word_filename = 'esp_vocabu.txt'
esp_word_file = open(esp_word_filename, 'r', encoding='utf8')
esp_words = esp_word_file.read()
esp_word_file.close()
esp_words = esp_words.split('\n')

high_vowels = ['e', 'i', 'é', 'í', 'E', 'I', 'É', 'Í']
low_vowels = ['a', 'o', 'u', 'á', 'ó', 'ú', 'A', 'O', 'U', 'Á', 'Ó', 'Ú']
vowels = ['a', 'e', 'i', 'o', 'u', 'á', 'é', 'í', 'ó', 'ú', 'A', 'E', 'I', 'O', 'U', 'Á', 'É', 'Í', 'Ó', 'Ú']

diacritics = {
'á': 'a',
'é': 'e',
'í': 'i',
'ó': 'o',
'ú': 'u',
'Á': 'A',
'É': 'E',
'Í': 'I',
'Ó': 'O',
'Ú': 'U',
'ü': 'u',
'Ü': 'U',
'ö': 'a',
'Ö': 'A'
}

#replace Spanish words in text with placeholder emoji, get list of Spanish words/proper nouns in order
def spanish_detect(text):
    esp_pattern = '(?<=[-^ ])('
    for word in esp_words:
        esp_pattern += '%s|' %word
    esp_pattern += '🦕)(?=[- .,?:!;$])'
    esp_pattern = re.compile(esp_pattern, re.I)
    esp_list = re.findall(esp_pattern, text)
    text = re.sub(esp_pattern, '🐃', text)
    return text, esp_list

#add Spanish words back, unchanged by orthographical changes to the text.
def spanish_addback(text, esp_list):
    for word in esp_list:
        text = text.replace('🐃', word, 1)
    return text
    
#replace diacriticized characters with non-diacriticized counterpart
def replace_diacritics(text):
    for diacritic in diacritics:
        text = text.replace(diacritic, diacritics[diacritic])
    return text
    
#replace variations of irrealis plural suffix with <zceh>
def sehreplace(text):
    seh_pattern = re.compile('(?<![-^ .,?:!;sz])[cs]e[hj]?(?=[- .,?:!;]$)')
    text = re.sub(seh_pattern, 'zceh', text)
    seh_pattern = re.compile('(?<![-^ .,?:!;SZsz])[CS]E[HJ]?(?=[- .,?:!;$])')
    text = re.sub(seh_pattern, 'ZCEH', text)
    return text
    
def kwreplace(text):
    coda_pattern = re.compile('kw(?![aeiouAEIOU])')
    text = re.sub(coda_pattern, 'uc', text)
    coda_pattern = re.compile('KW(?![aeiouAEIOU])')
    text = re.sub(coda_pattern, 'UC', text)
    text = text.replace('kw', 'cu')
    text = text.replace('Kw', 'Cu')
    text = text.replace('KW', 'CU')
    return text

def llreplace(text):
    ll_pattern = re.compile('(?<![tTlL])li(?=[-$ .,?:!;])')
    text = re.sub(ll_pattern, 'lli', text)
    ll_pattern = re.compile('(?<![tTlL])LI(?=[-$ .,?:!;])')
    text = re.sub(ll_pattern, 'LLI', text)
    return text
    
def sreplace(text):
    c_pattern = re.compile('s(?=[eiEI])')
    text = re.sub(c_pattern, 'c', text)
    c_pattern = re.compile('S(?=[eiEI])')
    text = re.sub(c_pattern, 'C', text)
    text = text.replace('s', 'z')
    text = text.replace('S', 'Z')
    return text

def kreplace(text):
    kc_pattern = re.compile('k(?=[eiEI])')
    text = re.sub(kc_pattern, 'qu', text)
    kc_pattern = re.compile('K(?=[ei])')
    text = re.sub(kc_pattern, 'Qu', text)
    kc_pattern = re.compile('K(?=[EI])')
    text = re.sub(kc_pattern, 'QU', text)
    text = text.replace('k', 'c')
    text = text.replace('K', 'C')
    return text
        
def wreplace(text):
    w_pattern = re.compile('w(?=[aeioAEIO])')
    text = re.sub(w_pattern, 'hu', text)
    w_pattern = re.compile('W(?=[aeio])')
    text = re.sub(w_pattern, 'Hu', text)
    w_pattern = re.compile('W(?=[AEIO])')
    text = re.sub(w_pattern, 'HU', text)
    coda_w_pattern = re.compile('W(?=[A-Z])')
    text = re.sub(coda_w_pattern, 'UH', text)
    text = text.replace('W', 'UH')
    text = text.replace('w', 'uh')
    return text
    
def ureplace(text):
    u_pattern = re.compile('(?<![qhcQHC])u(?=[aeioAEIO])')
    text = re.sub(u_pattern, 'hu', text)
    u_pattern = re.compile('(?<![qhcQHC])U(?=[aeio])')
    text = re.sub(u_pattern, 'Hu', text)
    u_pattern = re.compile('(?<![qhcQHC])U(?=[AEIO])')
    text = re.sub(u_pattern, 'HU', text)
    coda_u_pattern = re.compile('(?<![qhcQHC])u')
    text = re.sub(coda_u_pattern, 'uh', text)
    coda_u_pattern = re.compile('(?<![qhcQHC])U')
    text = re.sub(coda_u_pattern, 'UH', text)
    return text
