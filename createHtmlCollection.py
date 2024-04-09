def create_html_files(start, end):
    """
    Creates multiple HTML files with titles 'Nerd Stone #x',
    where x is a number in the specified range. Each file is
    named sequentially (e.g., NerdStone00001.html).
    """
    template = """<!DOCTYPE html>
<html>
<head>
    <title>Nerd Stone #{}</title>
    <script src="/content/f8d6d9594ff93cb4190cfa81d877b81b59b0d2acd975685fdd12efd0452bd190i0"></script>
</head>
<body>
    <script src="/content/da759d4d72fbdefb9d0d81c41e2c7a90bca7c9b6b5f0be8d5cba3a9f310dd0bai0"></script>
</body>
</html>
"""

    for i in range(start, end + 1):
        file_name = f"NerdStone{str(i).zfill(5)}.html"
        with open(file_name, "w") as file:
            file.write(template.format(i))

# Change the range here for your desired start and end
create_html_files(1, 10000)
