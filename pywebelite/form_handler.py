class FormHandler:
    def validate_form(self, form_data):
        name = form_data.get('name', '').strip()
        email = form_data.get('email', '').strip()

        if not name or len(name) < 3:
            return False, "Name must be at least 3 characters long."

        if not email or '@' not in email or '.' not in email:
            return False, "Invalid email address."
        return True, "Form submitted successfully!"
