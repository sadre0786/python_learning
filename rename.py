# import os

# folder_path = r"C:\Users\mrsad\Desktop\Sanatan-react\public\gallery\Spiritual Events 2"
# start_name = 1

# for index,fileName in enumerate(os.listdir(folder_path)):
#     if fileName.endswith(".webp"):
#         new_name = f"{start_name+index}.webp"
#         os.rename(os.path.join(folder_path,fileName), os.path.join(folder_path,new_name))





import os

folder_path = r"C:\Users\mrsad\Desktop\Sanatan-react\public\gallery\Spiritual Events 2"
total_images = 156  # Total images in the folder

# Step 1: Rename files to temporary names to avoid conflicts
for index, fileName in enumerate(os.listdir(folder_path)):
    if fileName.endswith(".webp"):
        temp_name = f"temp_{index}.webp"
        os.rename(os.path.join(folder_path, fileName), os.path.join(folder_path, temp_name))

# Step 2: Rename files to final reverse order names
for index, temp_name in enumerate(os.listdir(folder_path)):
    if temp_name.startswith("temp_") and temp_name.endswith(".webp"):
        final_name = f"{total_images - index}.webp"
        os.rename(os.path.join(folder_path, temp_name), os.path.join(folder_path, final_name))












# import os

# folder_path = r'C:\Users\HP\Downloads\px-conversions'  # Raw string
# start_number = 138  # Starting number for renaming

# for i, filename in enumerate(os.listdir(folder_path)):
#     if filename.endswith('.webp'):
#         new_filename = f"{start_number + i}.webp"  # New name format
#         os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))





# """"""""""""""""""""""""""""""'""""""""""""""""""""New Syntax using enumerate""""""""""""""""""""""""""""""""""""""""""""""""
# fruits = ["Apple","Banana","Mango"]
# for index,fruit in enumerate(fruits):
#     print(index,fruit) 


# $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$oath.join method uses for joining paths$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# file_path = r"C:\\Users\\HP\\Documents"
# file_name = "example.txt"
# os.path.join(file_path,file_name)
