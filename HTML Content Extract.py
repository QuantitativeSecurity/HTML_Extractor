from bs4 import BeautifulSoup

html_content = """
<html>
  <head>
    <title>Example Page</title>
  </head>
  <body>
    <h1>Welcome to my example page</h1>
    <p class="content">Here is some example content</p>
    <ul id="my-list">
      <li>Item 1</li>
      <li>Item 2</li>
      <li>Item 3</li>
    </ul>
  </body>
</html>
"""

soup = BeautifulSoup(html_content, "html.parser")

# Extract the title of the page
title = soup.find("title").text
print("Page title:", title)

# Extract the text of the first paragraph with class "content"
content = soup.find("p", class_="content").text
print("Content:", content)

# Extract the list items
list_items = [item.text for item in soup.find("ul", id="my-list").find_all("li")]
print("List items:", list_items)
