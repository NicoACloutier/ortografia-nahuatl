def main():

    import switchfunctions as sf
    import re
    
    #dictionary storing the words in the classical orthography
    #along with how they write it
    words = {
    'nochan': '', 
    'xalli': '', 
    'neuctli': '', 
    'calli': '', 
    'tzopilotl': '', 
    'cequin': '', 
    'cahci': '', 
    'ahui': '',
    'matizceh': '',
    'huallauh': '',
    'itta': ''
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
    
    #remove spanish words from text so they aren't changed
    text, esp_list = sf.spanish_detect(text)
    
    #get rid of diacritics
    text = sf.replace_diacritics(text)
    
    #if they write glottal stop/fricative as <'> , replace with <h>
    if "'" in words['cahci']:
        text = text.replace("'", 'h')
    
    #if they write <o> as <u>, replace with <o>
    if 'u' in words['nochan']:
        text = text.replace('u', 'o') 
    
    #if they write coda-position labio-velar stop with <kw>, replace with <uc>
    if 'kw' in words['neuctli']:
        text = sf.kwreplace(text)
    
    #if they write plural irrealis suffix as other than <zceh>, replace with <zceh>
    if not words['matizceh'].endswith('zceh'):
        text = sf.sehreplace(text)
    
    #if they write lateral absolutive suffix with <li>, replace with <lli>
    if 'ali' in words['calli']:
        text = sf.llreplace(text)
    
    #if they write alveolar affricate as <ts>, replace with <tz>
    if 'ts' in words['tzopilotl']:
        text = text.replace('ts', 'tz')
    
    #if they write alveolar fricative as <s>, replace with <z>/<c>
    if 's' in words['cequin']:
        text = sf.sreplace(text)

    #if they write velar stop as <k>, replace with <c>/<qu>
    if 'k' in words['calli']:
        text = sf.kreplace(text)
    
    #if they write glottal fricative with <j>, replace with <h>
    if 'j' in words['cahci']:
        text = text.replace('j', 'h')
    
    #if they write labiovelar approximant with <w>, replace with <hu>/<uh>
    if 'w' in words['ahui']:
        text = sf.wreplace(text)
    elif 'aui' in words['ahui']:
        text = sf.ureplace(text)
      
    #take care of edge-case double letters
    if words['itta'] == 'ita':
        text = text.replace('ita', 'itta')
    if 'ala' in words['huallauh']:
        text = text.replace('hualah', 'huallah')
        text = text.replace('hualauh', 'huallauh')
    
    #add spanish words back from list, one at a time
    text = sf.spanish_addback(text, esp_list)
    
    #write the text in the output file
    with open(output_file, 'w', encoding='utf8') as f:
        f.write(text[1:]) #for some reason the first character repeats itself, [1:] is to prevent that
        
    print('\nTerminado')
    
if __name__ == '__main__':
    main()
