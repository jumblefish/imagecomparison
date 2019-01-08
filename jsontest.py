import json

data = {}
data['Records'] = []

colors = "red, orange, yellow, green, teal, blue, purple, pink, white, gray, black, brown"
colorlist = colors.split(', ') #lists are often copied from places, split() is very useful here

times = "past-24-hours, past-7-days"
formats = "jpg, gif, png, bmp, svg, webp, ico"
#check if sizes can take less than, <
sizes = "large, medium, icon, >400*300, >640*480, >800*600, >1024*768, >2MP, >4MP, >6MP, >8MP, >10MP, >12MP, >15MP, >20MP, >40MP, >70MP"

#need to loop over times, formats, colors, sizes; generate 12x2x4x2+ = 192+ entries, ~ 67200 images
data['Record'].append({
            "keywords": "apple",
            "limit": 1000,
            "color": colorlist[1],
            "print_urls": True
})
