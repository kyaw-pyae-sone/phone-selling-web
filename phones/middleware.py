# yourapp/middleware.py
class SaveLastPageMiddleware:
    """
    Save the last page URL the user visited (GET request) in session,
    ignoring login/logout/static pages.
    """
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)

        if request.method == "GET" and request.user.is_anonymous:
            path = request.get_full_path()
            # Exclude login/logout/static paths
            if not path.startswith(("/login", "/logout", "/static")):
                request.session["last_page"] = path

        return response
