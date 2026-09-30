from cloudinary import uploader


def image_uploader(image, folder: str) -> str | None:
    allowed_types = {"image/jpg", "image/png", "image/webp"}
    if not image or not image.filename:
        return None
    if image.content_type not in allowed_types:
        return None
    try:
        upload = uploader.upload(image, folder=folder)
        return upload['secure_url']
    except Exception as e:
        print(e)
        return None
