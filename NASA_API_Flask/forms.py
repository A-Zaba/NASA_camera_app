from NASA_API_Flask import main_functions
import requests
from flask_wtf import FlaskForm
from wtforms import SelectField


# Create basic class FlaskForm class to then manipulate user input with in routes
class Mars_camera(FlaskForm):
    camera = SelectField('camera', choices=[("FHAZ", "FHAZ"),
                                            ("RHAZ", "RHAZ"),
                                            ("MAST", "MAST"),
                                            ("NAVCAM", "NAVCAM"),
                                            ("CHEMCAM", "CHEMCAM")])


def get_pictures_from_Mars(camera):
    # Build API url for calls
    url = "https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key="
    api_key_dict = main_functions.read_from_file("NASA_API_Flask/JSON_Files/nasa_api_key.json")
    my_api_key = api_key_dict["nasa_key"]
    url2 = url + my_api_key

    # Get json response from API, detailing information about ALL cameras, and save file to system.
    mars_pics = requests.get(url2).json()
    main_functions.save_to_file(mars_pics, "NASA_API_Flask/JSON_Files/mars_pics.json")
    mars_pics = main_functions.read_from_file("NASA_API_Flask/JSON_Files/mars_pics.json")

    # Create empty list and append all images from selected camera to it
    lst = []
    for i in mars_pics["photos"]:
        if i["camera"]["name"] == camera:
            lst.append(i["img_src"])
    return lst
