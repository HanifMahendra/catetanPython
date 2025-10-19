#slicing = create substring by extracting elements from another string
#          indexing[] or slice ()
#          [start:stop:step] if using "indexing" if else using "slice" then [start,stop,step]

name = "hanif awiyoso"

first_name =  name[:3]      # [0:3]
last_name = name[4:]        # [4:end]
funky_name = name[0::2]      # [0:end:2] NOTE: jadi fungsi dari step itu ngelewatin "2 angka didepannya"
reversed_name = name[::-1]  # [0:end:-1]

print(reversed_name)

website1 = "http://google.com"
website2 = "http://wikipedia.com"

slice = slice(7,-4) #the function of negative is so when you change the web url,
                    # the stop will always stay on the ".com (just more effective)"

print(website1[slice])
print(website2[slice])