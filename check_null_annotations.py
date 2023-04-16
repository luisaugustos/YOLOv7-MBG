import os

# Specify the directory path where the images and annotations are stored
dir_path = 'video11_frames/'

# Loop through the images in the directory
for filename in os.listdir(dir_path):
    if filename.endswith('.jpg'):  # adjust for your image extension
        annotation_filename = os.path.splitext(filename)[0] + '.txt'
        annotation_file_path = os.path.join(dir_path, annotation_filename)
        if os.path.exists(annotation_file_path) and os.path.getsize(annotation_file_path) == 0:
            os.remove(os.path.join(dir_path, filename))
            os.remove(annotation_file_path)
            print(f"Removed image {filename} and annotation file {annotation_filename}")
