def main():

    import switchfunctions as sf
    import re
    
    words = {
    'nochan': '', 
    'xalli': '', 
    'neuctli': '', 
    'calli': '', 
    'tzopilotl': '', 
    'cequin': '', 
    'cahci': '', 
    'ahui': '',
    'matizceh': ''
    }
    
    #ask how to write the above words to collect info on source orthography
    print('¿Cómo se escribe las siguientes palabras en la ortografía en que está escribido el texto ahora?')
    for word in words:
        inputted = input('%s: ' %word).lower()
        words[word] = inputted
    
    #input sentence to be converted
    print('\n')
    filename = input('File: ')
    file = open(filename, 'r', encoding='utf8')
    text = file.read()
    file.close()
    
    output_file = input('Output file: ')
    
    text, esp_list = sf.spanish_detect(text)
    print(esp_list)
    
    #remove vowels with diacritical marks
    text = sf.replace_diacritics(text)
    
    #text = text.lower()
    
    if "'" in words['cahci']:
        text = text.replace("'", 'h')
    
    #if they write <o> with <u>, replace the <u> with <o>
    if 'u' in words['nochan']:
        text = text.replace('u', 'o') 
    
    #if they write coda-position labio-velar stop with <kw>, replace with <uc>
    if 'kw' in words['neuctli']:
        text = sf.kwreplace(text)
    
    #replaces plural irrealis suffix with <zceh>
    if not words['matizceh'].endswith('zceh'):
        text = sf.sehreplace(text)
    
    #replace single-l absolutive suffix <li> with double-l <lli>
    if 'ali' in words['calli']:
        text = sf.llreplace(text)
    
    #if they write alveolar affricate as <ts>, replace with <tz>
    if 'ts' in words['tzopilotl']:
        text = text.replace('ts', 'tz')
    
    #if they write alveolar fricative as <s>, replace with <z>/<c>
    if 's' in words['cequin']:
        text = sf.sreplace(text)

    #if they write <c>/<qu> with <k>, replace <k> with <c>/<qu>,
    #depending on following character
    if 'k' in words['calli']:
        text = sf.kreplace(text)
    
    #if they write <h> with <j>, replace
    if 'j' in words['cahci']:
        text = text.replace('j', 'h')
    
    #if they write <hu>/<uh> with <w>, replace
    if 'w' in words['ahui']:
        text = sf.wreplace(text)
    elif 'aui' in words['ahui']:
        text = sf.ureplace(text)
    
    #add spanish words back from list, one at a time
    text = sf.spanish_addback(text, esp_list)
    
    with open(output_file, 'w', encoding='utf8') as f:
        f.write(text[1:])
    
if __name__ == '__main__':
    main()
