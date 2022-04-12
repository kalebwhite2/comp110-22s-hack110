ids: dict[str, int] = {'freaky_fire_escapes': 0, 'stupid_study_spots':0, 'badass_bathrooms': 0, 'funky_fire_spots': 0, 'crazy_coffee':0}

class Uploaded_Image:
    new_object_id = dict[str, int]
    url = str
    location = str
    description = str

    def __init__(self, new_id: str, url: str, location: str, description: str):
        global ids
        
        self.new_object_id = {}

        for key in ids:
            if key == new_id:
                self.new_object_id[key] = ids[key]
                ids[key] += 1
        
        self.url = url
        self.location = location
        self.description = description



def categorize_images(all_uploads: list[Uploaded_Image], category: str) -> list[Uploaded_Image]:
    return_list: list[Uploaded_Image] = []
    for uploaded_image in all_uploads:
        for key in uploaded_image.new_object_id:
            if key == category:
                return_list.append(uploaded_image)
    return return_list