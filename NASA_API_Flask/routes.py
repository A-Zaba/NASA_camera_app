from NASA_API_Flask import app, forms
from flask import request, render_template


@app.route('/')
@app.route('/search', methods=["GET", "POST"])
def search():
    # Access user input via Flask request
    search_form = forms.Mars_camera(request.form)
    # If any camera was selected by the user, render the pictures from said camera on the page,
    # if no camera was selected, but the url was still accessed, simply return the initial "choose a camera" form.
    if request.method == "POST":
        camera = request.form['camera']
        mars_pics = forms.get_pictures_from_Mars(camera)
        return render_template("mars_results.html", result=mars_pics, camera=camera, form=search_form)
    return render_template("mars_search.html", form=search_form)
