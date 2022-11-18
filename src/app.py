import os
from src.config import create_app
from src.view import MetaDataView
from sqlalchemy import MetaData

# Create the Flask app, preparing the DB connection and starting an application context
app = create_app(__name__)

app.add_url_rule(
    "/api/meta-data",
    view_func=MetaDataView.as_view("meta_data_api"),
    methods=["GET"],
)

def main():
    print(MetaData())
    app.run(debug=True, port=8081)

if __name__ == "__main__":
    main()