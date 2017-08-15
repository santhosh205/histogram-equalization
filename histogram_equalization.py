import cv2
name = "images/input.jpg"
bgr = cv2.imread(name)
h = len(bgr)
w = len(bgr[0])
hsv = cv2.cvtColor(bgr, cv2.COLOR_BGR2HSV)
values_count = {}
for row in hsv:
    for pixel in row:
        v = pixel[2]
        if v in values_count:
            values_count[v] = values_count[v] + 1
        else:
            values_count[v] = 1
values_count = list(values_count.items())
values_count = [list(tup) for tup in values_count]
temp = 0
for count in values_count:
    count[1] = count[1] + temp
    temp = count[1]
values_cdf = values_count
cdf_min = min([tup[1] for tup in values_cdf])
new_values = {}
for value_cdf in values_cdf:
    new_value = round(((value_cdf[1]-cdf_min)/(h*w-1))*255)
    new_values[value_cdf[0]] = new_value
new_hsv = hsv
for row in new_hsv:
    for pixel in row:
        v = pixel[2]
        pixel[2] = new_values[v]
new_bgr = cv2.cvtColor(new_hsv, cv2.COLOR_HSV2BGR)
new_name = "images/input_enhanced.jpg"
cv2.imwrite(new_name, new_bgr)
