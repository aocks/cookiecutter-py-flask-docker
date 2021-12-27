"""Views for main app.
"""


from flask import render_template


def home():
    """Show top-level home or index.html.
    """
    return render_template('index.html')
