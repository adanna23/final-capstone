from flask import Blueprint, render_template

site = Blueprint('site', __name__, template_folder ='site_templates')

@site.route('/')
def home():
    return render_template('index.html')

@site.route('/profile')
def profile():
    return render_template('profile.html')

@site.route('/contact')
def contact():
    return render_template('contact.html')

@site.route('/about')
def about():
    return render_template('about.html')

@site.route('/architecture')
def architecture():
    return render_template('architecture.html')

@site.route('/art')
def art():
    return render_template('art.html')

@site.route('/nature')
def nature():
    return render_template('nature.html')

@site.route('/people')
def people():
    return render_template('people.html')

@site.route('/portrait')
def portrait():
    return render_template('portrait.html')

@site.route('/blackandwhite')
def blackandwhite():
    return render_template('blackandwhite.html')

@site.route('/services')
def services():
    return render_template('services.html')