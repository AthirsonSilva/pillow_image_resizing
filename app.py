import os
from PIL import Image


def main(main_images_folder, new_width=800):
	if not os.path.isdir(main_images_folder):
		raise NotADirectoryError(f'{main_images_folder} does not exist')

	for root, dirs, files in os.walk(main_images_folder):
		for file in files:
			file_full_path = os.path.join(root, file)
			file_name, extension = os.path.splitext(file)

			converted_tag = '_CONVERTED'
			new_file = file_name + converted_tag + extension
			new_file_full_path = os.path.join(root, new_file)

            # if converted_tag in file_full_path:
            #     os.remove(file_full_path)
            # 	continue

            if os.path.isfile(new_file_full_path):
				print(f'File {new_file_full_path} already exists')
				continue

            if converted_tag in file_full_path:
				print('Image already converted')
				continue

            img_pillow = Image.open(file_full_path)

            width, height = img_pillow.size
            new_height = round((new_width * height) / width)
            image_quality = 10

            new_image = img_pillow.resize(
            	(new_width, new_height),
            	Image.LANCZOS
            )

            new_image.save(
            	new_file_full_path,
            	optimize = True,
            	quality = image_quality,
            	exif = img_pillow['exif']
            )

            print(f'{file_full_path} convertido com sucesso!')
            new_image.close()
            img_pillow.close()



if __name__ == '__main__':
    main_images_folder = '/home/athirson/Pictures'
    main(main_images_folder, new_width = 800)