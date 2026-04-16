# u-share_notes_webapp
U-Share Notes is a platform designed to help university students share and discover academic notes with ease. We used the Django web framework to use Python code for the back-end and connect it seamlessly with the front-end. Our group designed this web app for our CIS 376 (Software Engineering II) term project.

## Run Instructions
You can easily view and use the webapp by going to https://lanabu.pythonanywhere.com/. If you want to run the web app locally on your computer, follow the instructions below.

### Step 1: Navigate to project
In a terminal, navigate to the project directory (wherever you downloaded it).

```bash
cd path/to/u-share_notes_webapp
```
  
### Step 2: Install dependencies
Either in a virtual environment (preferred) or just on your local machine, run the following command in the terminal to install all of the necessary dependencies for the project to work:

```bash
python3 -m pip install -r requirements.txt
```

### Step 3: Make database migration
To create a SQLite database on your local machine and connect it to the project, run the following command:

```bash
python3 manage.py migrate
```

### Step 4: Run project
Now that everything is set up for the web application, run it on your local machine with the following command:

```bash
python3 manage.py runserver
```

Go to http://127.0.0.1:8000/ on your web browser (as specified by the output of the above command) to view and interact with the web application.

## Testing
### Test Setup
Before starting, make sure you've navigated to the project directory and installed all of the necessary dependencies by following Steps 1 and 2 of the Run Instructions above.

### Quality Checks
Run the following commands within the project directory to perform the tests:
- ```bash
  python3 manage.py check
  ```
- ```bash
  pytest
  ```
- ```bash
  pytest --cov
  ```

## Sources
### Code Help
- Setting up Django project in VS Code: https://code.visualstudio.com/docs/python/tutorial-django
- Django base template: https://stackoverflow.com/questions/14720464/django-project-base-template
- Linking stylesheet to base template: https://stackoverflow.com/questions/9339226/how-to-load-css-in-django-templates
- Template inheritance: https://unwiredlearning.com/blog/django-template-inheritance
- HTML copyright symbol code: https://www.rapidtables.com/web/html/html-codes/html-code-copyright.html
- Checking if user is logged in within template: https://www.delftstack.com/howto/django/django-check-logged-in-user/
- Short on-click effect for button using CSS "active" attribute: https://www.geeksforgeeks.org/css/how-to-add-onclick-effect-using-css/
- Getting a specific object from a database table: https://pypy-django.github.io/blog/2024/04/26/understanding-django-query-methods-objectsall-vs-get_object_or_404/
- URL pattern tips: https://www.hostinger.com/uk/tutorials/django-url-patterns
- PDF previewer: https://www.w3docs.com/snippets/html/how-to-embed-pdf-in-html.html
- User account functions in Django: https://learndjango.com/tutorials/django-login-and-logout-tutorial
- Serving media files in development mode: https://stackoverflow.com/questions/5517950/django-media-url-and-media-root
- Creating requirements.txt file for continuous integration: https://www.learningaboutelectronics.com/Articles/How-to-create-a-requirements-txt-file-for-a-Django-project.php
- Django searching for objects based on field values: https://learndjango.com/tutorials/django-search-tutorial
- Setting a default value when query result is "none": https://www.w3schools.com/django/ref_filters_default_if_none.php
- Hosting webapp on PythonAnywhere: https://developer.mozilla.org/en-US/docs/Learn_web_development/Extensions/Server-side/Django/Deployment#update_your_application_repository_in_github
- Serving user uploads on hosted website by specifying media URL and directory in static files: https://forum.djangoproject.com/t/media-files-not-found-on-pythonanywhere/21255
- Javascript for-of loop: https://stackoverflow.com/questions/9329446/loop-for-each-over-an-array-in-javascript
- Getting the count of objects of a model: https://stackoverflow.com/questions/5439901/how-to-get-the-count-of-objects-in-a-queryset-django
### Images
- Favicon generator: https://favicon.io/favicon-converter/
- Menu icon: https://fonts.google.com/icons?icon.size=64&icon.color=%23FFFFFF&icon.query=menu&selected=Material+Symbols+Outlined:menu:FILL@0;wght@400;GRAD@0;opsz@48&icon.platform=web
- Profile icon: https://fonts.google.com/icons?icon.size=64&icon.color=%23FFFFFF&icon.query=profile&selected=Material+Symbols+Outlined:account_circle:FILL@0;wght@400;GRAD@0;opsz@48&icon.platform=web
