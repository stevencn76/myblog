from common.profile import Profile


class ImageService:
    def get_image_filename_list(self):
        image_path = Profile.get_images_path()

        filename_list = []

        if image_path.exists():
            for item in image_path.iterdir():
                if item.is_file():
                    filename_list.append(item.name)

        return filename_list
