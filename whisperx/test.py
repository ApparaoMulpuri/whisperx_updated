import re

def refine_text(self, text):
    print("refine_text")
    print(f"input text: {text}")
    
    # Remove leading and trailing non-ASCII characters
    text = re.sub(r'^[^\x00-\x7F]+|[^\x00-\x7F]+$', '', text)
    
    # Remove multiple spaces
    text = " ".join(text.split())

    for char in ["।", "?", "!", ":", ";"]:
        text = text.replace(char, ".")

    print(f"refined text: {text}")
    return text

def test_refine_text():
    text = "আমি বাংলায় গান গাই। আমি বাংলায় গান গাই।"
    refined_text = refine_text(None, text)
    assert refined_text == "আমি বাংলায় গান গাই. আমি বাংলায় গান গাই."
    print("test_refine_text passed")


if __name__ == "__main__":
    test_refine_text()    
