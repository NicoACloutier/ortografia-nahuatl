def main():

    import switchfunctions as sf
    import re
    
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
    
    #normalize some edge cases, etc
    text = text.replace('uh', 'h')
    text = text.replace('itta', 'ita')
    text = text.replace('huallah', 'hualah')
    
    #add spanish words back from list, one at a time
    text = sf.spanish_addback(text, esp_list)
    
    #write the text in the output file
    with open(output_file, 'w', encoding='utf8') as f:
        f.write(text[1:]) #for some reason the first character repeats itself, [1:] is to prevent that
        
    print('\nTerminado')
    
if __name__ == '__main__':
    main()
