HTML Content Parser

This program demonstrates how to use the Beautiful Soup library to parse and extract information from HTML content in Python.
Dependencies

    Python 3.x
    Beautiful Soup 4

You can install Beautiful Soup using pip:

bash

pip install beautifulsoup4

Usage

    Copy the code from the program and save it into a file named parser.py.
    Execute the program by running the following command in your terminal:

bash

python parser.py

Program Overview

The program performs the following steps:

    Importing the Library:
    The Beautiful Soup library is imported to provide the ability to parse HTML content.

    HTML Content:
    An HTML content string is defined which represents a simple HTML page with a title, a paragraph, and a list of items.

    Creating a Soup Object:
    A Beautiful Soup object is created from the HTML content using the built-in HTML parser.

    Extracting the Title:
    The title of the HTML page is extracted by searching for the <title> tag and printing its text content to the console.

    Extracting the Paragraph Content:
    The text content of the first paragraph with a class of "content" is extracted by searching for the <p> tag with the specified class and printing its text content to the console.

    Extracting List Items:
    The text content of the list items is extracted by searching for the <ul> tag with an id of "my-list", finding all nested <li> tags, and printing their text content to the console.

Output

Upon executing the program, you should see the following output in your terminal:

plaintext

Page title: Example Page
Content: Here is some example content
List items: ['Item 1', 'Item 2', 'Item 3']
