import sys

# Path to the footer template file
footer_template_path = "templates/docs/shared/_footer.html"

# Read the content of the footer template
try:
    with open(footer_template_path, "r") as file:
        footer_content = file.read()
except FileNotFoundError:
    print(f"Error: Footer template file not found at {footer_template_path}")
    sys.exit(1)

# Check for the incorrect text
if "Ubuntu and Canonical are registered trademarks." in footer_content:
    print("Bug detected: Incorrect footer text found.")
    sys.exit(1)

# Check for the correct text
if "Ubuntu and Canonical Ubuntu are registered trademarks." not in footer_content:
    print("Bug detected: Correct footer text not found.")
    sys.exit(1)

# If the correct text is present and the incorrect text is absent, the bug is fixed
print("Footer text is correct.")
sys.exit(0)