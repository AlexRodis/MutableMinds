from blog import app, db
from blog.models import (User, Post,
                        Tag, Category)

@app.shell_context_processor
def make_shell_context():
    return {'db':db, 'User':User,\
        'Post':Post, 'Category':Category,\
            'Tag':Tag}

if __name__ == '__main__':
    app.run(debug=True)
