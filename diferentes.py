def main():

    import switchfunctions as sf
    
    #input sentence to be converted
    print('\n')
    filename = input('File: ')
    file = open(filename, 'r', encoding='utf8')
    full_text = file.read()
    file.close()
    
    output_file = input('Output file: ')
    
    full_text, esp_list = sf.spanish_detect(full_text) #remove spanish words
    full_text = sf.replace_diacritics(full_text) #remove diacritics
    lines = full_text.split('\n')
    new_lines = []
    
    for text in lines:
        #if they write glottal stop/fricative as <'> , replace with <h>
        text = text.replace("'", 'h')
    
        #if they write coda-position labio-velar stop with <kw>, replace with <uc>
        text = sf.kwreplace(text)
    
        #if they write plural irrealis suffix as other than <zceh>, replace with <zceh>
        text = sf.sehreplace(text)
    
        #if they write lateral absolutive suffix with <li>, replace with <lli>
        text = sf.llreplace(text)
    
        #if they write alveolar affricate as <ts>, replace with <tz>
        text = text.replace('ts', 'tz')
    
        #if they write alveolar fricative as <s>, replace with <z>/<c>
        text = sf.sreplace(text)

        #if they write velar stop as <k>, replace with <c>/<qu>
        text = sf.kreplace(text)
    
        #if they write glottal fricative with <j>, replace with <h>
        text = text.replace('j', 'h')
    
        #if they write labiovelar approximant with <w>, replace with <hu>/<uh>
        text = sf.wreplace(text)
        text = sf.ureplace(text)
        
        new_lines.append(text)
    
    new_text = ''
    for line in new_lines:
        new_text += '%s\n' %line
    
    new_text = sf.spanish_addback(new_text, esp_list) #add spanish words back
    
    #write the text in the output file
    with open(output_file, 'w', encoding='utf8') as f:
        f.write(new_text)

if __name__ == '__main__':
    main()