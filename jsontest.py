import json

data = {}
data['Records'] = []

def write_json(data_to_write):
    with open('data.json', 'w') as out_file:
        json.dump(data_to_write, out_file)

colors = "red, orange, yellow, green, teal, blue, purple, pink, white, gray, black, brown"
colorlist = colors.split(', ') #lists are often copied from places, split() is very useful here

times = "past-24-hours, past-7-days"
formats = "jpg, gif, png, bmp" #, svg, webp, ico"
formatlist = formats.split(', ')
#check if sizes can take less than, <
sizes = "large, medium" #, icon, >400*300, >640*480, >800*600, >1024*768, >2MP, >4MP, >6MP, >8MP, >10MP, >12MP, >15MP, >20MP, >40MP, >70MP"
sizelist = sizes.split(', ')
dictionary = "waveform curve, sine curve, amplitude modulation, sound wave, wave graph"
dictionarylist = dictionary.split(', ')

#need to loop over times, formats, colors, sizes; generate 12x2x4x2+ = 192+ entries, ~ 67200 images
'''
data['Records'].append({
            "keywords": dictionarylist[1],
            "limit": 1000,
            "color": colorlist[1],
            "print_urls": True
            "times": "past-7-days",
            "formats": formatlist[1],
            "sizes": sizeslist[1],
})
'''
for x in colorlist:
    for y in formatlist:
        for z in sizelist:
            for a in dictionarylist:
                data['Records'].append({
                    "keywords": a,
                    "limit": 1000,
                    "color": x,
                    "print_urls": True,
                    "times": "past-7-days",
                    "format": y,
                    "sizes": z,
                    "chromedriver": "/usr/bin/chromedriver"
                })


write_json(data)

