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


#I apologize to programmers everywhere for the following two functions. I realize they are bad, I tried to make them better, I could not.

#replace Spanish words in text with placeholder emoji denoting case and number with the index in the list of Spanish words
def spanish_detect(text):
    for word in esp_words:
        list_index = esp_words.index(word)
        lower_pattern = re.compile('(?<=[- ])%s(?=[- .,?:!;])' %word.lower())
        text = re.sub(lower_pattern, '😀%s' %list_index, text)
        
        capitalize_pattern = re.compile('(?<=[- ])%s(?=[- .,?:!;])' %word.capitalize())
        text = re.sub(capitalize_pattern, '🦕%s' %list_index, text)
        
        upper_pattern = re.compile('(?<=[- ])%s(?=[- .,?:!;])' %word.upper())
        text = re.sub(upper_pattern, '🐃%s' %list_index, text)
    return text

#add Spanish words back, unchanged by orthographical changes to the text.
def spanish_addback(text):
    emoji_list = ['😀', '🦕', '🐃']
    for emoji in emoji_list:
        addback_pattern = re.compile('%s\d+' %emoji)
        match_list = re.findall(addback_pattern, text)
        for match in match_list:
            index_for_match = re.sub('[😀🦕🐃](?=\d+)', '', match)
            match_index = int(index_for_match)
            word = esp_words[match_index]
            if emoji == '😀':
                text = text.replace(match, word)
            elif emoji == '🦕':
                text = text.replace(match, word.capitalize())
            elif emoji == '🐃':
                text = text.replace(match, word.upper())
    return text
    
#replace diacriticized characters with non-diacriticized counterpart
def replace_diacritics(text):
    for diacritic in diacritics:
        text = text.replace(diacritic, diacritics[diacritic])
    return text
    
#replace variations of irrealis plural suffix with <zceh>
def sehreplace(text):
    seh_pattern = re.compile('(?<![- .,?:!;sz])[cs]e[hj]?(?=[- .,?:!;])')
    text = re.sub(seh_pattern, 'zceh', text)
    seh_pattern = re.compile('(?<![- .,?:!;SZsz])[CScs]e[hj]?(?=[- .,?:!;])')
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
    ll_pattern = re.compile('(?<![tT])li(?=[- .,?:!;])')
    text = re.sub(ll_pattern, 'lli', text)
    ll_pattern = re.compile('(?<![tT])LI(?=[- .,?:!;])')
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
    text = text.replace('W', 'Hu')
    text = text.replace('w', 'hu')
    return text
    
def ureplace(text):
    u_pattern = re.compile('(?<![qc])u(?=[aeioAEIO])')
    text = re.sub(u_pattern, 'hu', text)
    u_pattern = re.compile('(?<![qc])U(?=[aeioAEIO])')
    text = re.sub(u_pattern, 'Hu', text)
    coda_u_pattern = re.compile('(?<![qhcQHC])u')
    text = re.sub(coda_u_pattern, 'uh', text)
    return text