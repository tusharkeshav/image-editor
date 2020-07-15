#!/usr/bin/env python3
# -*- coding: utf-8 -*-

#coded by 0xp0is0n -_- XD

from PIL import Image
from PIL import ImageFilter
from PIL.ExifTags import TAGS
from banner import header

#save a image
def save(image, image_path, **kwargs):#, result_ext, qualtiy_img ):
    name_noExt = str(image_path.split('.')[0])
    #name_noExt = str(name.split('/))[-1]
    default_ext = str(image_path.split('.')[-1]).lower()
    if default_ext == 'jpg':
        default_ext = 'jpeg'
    print(default_ext)

    if 'ext' in kwargs:
        image.save(name_noExt + "new." + kwargs['ext'], kwargs['ext'])
        print('The image is save as: '+ name_noExt + "new." + kwargs['ext'])
    else:
        image.save(name_noExt + "new."+ default_ext, default_ext)
        print('The image is save as: '+ name_noExt + "new."+ default_ext)
    
'''
    Ext = image_path.split('.')[-1]
    if result_ext == 'png':
        image.save(name_noExt + "new.png", 'PNG')
    elif result_ext == 'jpg':
        image.save(name_noExt + "new.jpg", 'JPG')
    else:
        image.save(name_noExt + "new.jpg", 'JPG' )
 '''       
        
#imafe filters
def image_filter(image, image_path):
    '''It is a Image Filter Function. It apply various filter to Image.
Usage: Enter the serial number of Filter you wanted to apply on Image
For Example: Type 1 for Blur'''
    filter_type = int(input('1. Blur \n2. Edge Enhance \n3. Sharpen \n4. Smooth \n>>>'))
    if filter_type == 1:
        #Blur
        image1 = image.filter(ImageFilter.BLUR)
    elif filter_type == 2:
        #Edge enhance
        image1 = image.filter(ImageFilter.EDGE_ENHANCE)
    elif filter_type == 3:
        #Sharpen
        image1 = image.filter(ImageFilter.SHARPEN)
    elif filter_type == 4:
        #Smooth
        image1 = image.filter(ImageFilter.SMOOTH)
    else:
        print("Sorry, Either Wrong input or filter not supported")
    save(image1, image_path)

#Rotate of image
def rotate(image, image_path):
    '''
It is a Image Rotate Function. It rotate the Image to by a given degree.
Usage: Enter the Degree by which you wanted to Rotate the Image.
For Example: Type 90 to rotate the Image by 90 degree
'''
    degree = int(input("Enter the degree to rotate(E.g 90 to rotate by 90 degree): "))
    image1 = image.rotate(degree)
    save(image1, image_path)
    
    
#Flipping of Image
def flip(image, image_path):
    '''
It is a Image Flip Function. It flip the image to given Flip option.
Currently, It support
-> Flip Left to Right
-> Flip Top to Bottom
-> Image Transpose
Other Rotation can be Performed under Rotation of Image
Usage: Enter the serial number of Flip.
For Example: Type 1 for Flip Left to Right.
'''
    flip_id = int(input("1. Flip Left to right \n2. Flip Top to bottom \n3. Image Transpose \n>>>"))
    if flip_id == 1:
        image1 = image.transpose(Image.FLIP_LEFT_RIGHT)
    elif flip_id == 2:
        image1 = image.transpose(Image.FLIP_TOP_BOTTOM)
    elif flip_id == 3:
        image1 = image.transpose(Image.TRANSPOSE)
    else:
        print("You haven't entered the wrong serial of filter")
    save(image1, image_path)
    
    
#thumbnail code
def thumbnail(image, image_path):
    '''
It is a Thumbnail Function. It convert Image to its Thumbnail of given size.
Alert: If the enter width(or Height) of Image exceed Original Image widht(or Height), this function won't stretch the Image to given size instead It uses the original width of Image.
Usage: Enter the desired Widht and then enter the desired Height.
Info: Currently, it save the Thumbnail Image in PNG format. Generaly, thumbnail are in PNG
'''
    max_width = int(input("Enter the max width: "))
    max_height = int(input("Enter the max height: "))
    image.thumbnail((max_width, max_height))
    save(image, image_path, ext = 'PNG')
    

def exif_info(image, image_path):
    '''
EXIF_INFO provide you the meta-data of Image if availiable. 
Meta-data of Image often contain some Camera, GPS, Exposure etc. information.
It is very useful in obtaining some extra juicy info about Image.
'''
    exif_data = image.getexif()
    #print(exif_data)
    for tag_id in exif_data:
        tag = TAGS.get(tag_id, tag_id)
        data = exif_data.get(tag_id)
        
        if isinstance(data, bytes):
            data = data.decode()
        #for python 3
        print(f"{tag:25}: {data}")
        #for python2
        # s = "{:<25} {:^9}".format(tag,data)
        # print(s)
    
    
    
    
#*********** Main driver Code **********#
#Main driver code
def image_main():
    '''
It is a light weight handy Image editing tool developed mainly for CLI users.
Library used: Pillow
Usage: You have to insert the Path of Image. For Example: /root/Desktop/test.jpg.
Then Enter the serial of the features to be used on Image
You can Type help for any help in any feature.
Features: Right now many features are included - Resizing, Filtering, Rotation, Flipping of Image

'''
    image_path = str(input("Enter the path of image or image name: "))
    #image_path = "test_exif.jpg"
    print(image_path)
    image = Image.open(image_path)
    #image.show()
    name_noExt = str(image_path.split('.')[0])
    Ext = image_path.split('.')[-1]
    print ('1. For Image resizing \n2. For Image format conversion \n3. For reducing the Quality of image(for reducing size) \n4. Apply image filter(E.g Blur, Sharpen etc.) \n5. Create thumbnail of image \n6. Rotate Image by Degree \n7. Get Information about image(Exif data) \n')
    user_choice = int(input('>>>'))
    
    #resizing of image
    if user_choice == 1:
        print('Current image size is: '+ str((image.size)[0]) + ' x ' + str((image.size)[1]))
        width = int(input("Enter width: "))
        height = int(input("Enter height: "))
        new_image = image.resize((width, height))
        new_image.save(name_noExt+"new."+Ext)
        print('The image is save as: '+ name_noExt+"new."+Ext)
    
    #changing image type e.g png to jpg
    elif user_choice == 2:
        img_format = (str(input('Enter the format as png/jpg :'))).lower()
        if img_format == 'png':
            image.save(name_noExt+"new.png", 'PNG')
        elif img_format == 'jpg':
            image.save(name_noExt+"new.jpg", 'jpeg')
        else:
            print('Sorry, Wrong Extension or currently not supported!')
        print('The image is save as: '+ name_noExt+"new.jpg")
            
    #Changing qualuty
    elif user_choice == 3:
        q = int(input("Enter the quality of image on scale of 0-100. Best(95), Good(85): "))
        image.save(name_noExt+"new.jpg", 'jpeg', quality=q)
        print('The image is save as: '+ name_noExt+"new.jpg")
        
        
    #filter image
    elif user_choice == 4:
        image_filter(image, image_path)
        
    #thumbnail of image
    elif user_choice == 5:
        thumbnail(image, image_path)
    
    #rotation of image
    elif user_choice == 6:
        rotate(image, image_path)

    #print Exif data of image
    elif user_choice == 7:
        exif_info(image, image_path)
    
 

#main function
if __name__ == "__main__":
    print(header())
    image_main()
