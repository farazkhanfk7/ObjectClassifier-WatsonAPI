import os
class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "you-will-never-guess"
    UPLOAD_FOLDER = "image-file"
    CSRF_ENABLED = True
    DEBUG = False
    
    # Enter your API Key and Custom Classifier ID below
    API_KEY = "kzOhqK0bfqTtEeJbYGmw0b_I_dHBoLaUYO3RWsRVj_ji"
    CLASSIFIER_ID = "DefaultCustomModel_1161430422"
