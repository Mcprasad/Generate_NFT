def generate(input_filename, output_directory, mutations, output_width, output_height):

    #import all the necessary images 
    from PIL import Image, ImageEnhance
    import random

    #open the image from the filename
    img = Image.open(input_filename).convert("RGBA")

    #resize the image to a standard size
    img = img.resize((output_width,output_height))

    #split image into multiple channels - RGB
    var = Image.Image.split(img)

    #create multiple variations of mutations:
    i = 0
    for i in range(mutations):
        
        #pick random layers
        layer1 = random.randint(0,3)
        layer2 = random.randint(0,3)
        layer3 = random.randint(0,3)
        layer4 = random.randint(0,3)

        #create a unique image with the combination of layers
        new_img = Image.merge('RGBA', (var[layer1], var[layer2] ,var[layer3], var[layer4]))

        #create a random background image 
        red_channel = random.randint(0,255)
        blue_channel = random.randint(0,255)
        green_channel = random.randint(0,255)
        alpha_channel = random.randint(0,255)

        back_img = Image.new('RGBA',(output_width,output_height),(red_channel,blue_channel,green_channel, alpha_channel))

        #load the newly create image & paste the background image and the newly created image together 
        blend_img = Image.blend(back_img,new_img, random.uniform(0.6, 1)).convert("RGB")

        #improve the quality of the image
        #enhance the color
        blend_img = ImageEnhance.Color(blend_img).enhance(random.uniform(1,3))

        #enhance the contrast 
        blend_img = ImageEnhance.Contrast(blend_img).enhance(random.uniform(1,3))

        #enhance the contrast 
        blend_img = ImageEnhance.Brightness(blend_img).enhance(random.uniform(1,3))

        #enhance the contrast 
        blend_img = ImageEnhance.Sharpness(blend_img).enhance(random.uniform(1,3))
       
        #save the image to the specified dirctory 
        blend_img.save(output_directory+str(i)+".jpeg", format="jpeg")

        #increment the mutation counter
        i += 1 
