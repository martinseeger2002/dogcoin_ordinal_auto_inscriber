def create_html_files(start, end):
    """
    Creates multiple HTML files with titles 'Nerd Stone #x',
    where x is a number in the specified range. Each file is
    named sequentially (e.g., CollectionName.html).
    """
    template = """<!DOCTYPE html>
<html>
<head>
    <title>Collection Name #{}</title>
    <script src="/content/<JS lib inscription ID"></script>
</head>
<body>
    <script src="/content/<your script inscription ID>"></script>
</body>
</html>
"""

    for i in range(start, end + 1):
        file_name = f"CollectionName{str(i).zfill(5)}.html"
        with open(file_name, "w") as file:
            file.write(template.format(i))

# Change the range here for your desired start and end
create_html_files(1, 69)
