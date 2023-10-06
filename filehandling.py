f1 = open('yash.jpg', 'rb')
f2 = open('new_image.jpg', 'wb')

for i in f1:
    f2.write(i)
