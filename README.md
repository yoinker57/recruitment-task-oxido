# Recruitment-task-oxido
# Article to HTML Converter

This program converts a plain text article into HTML format with a specified structure.

## Prerequisites

To use this program, you need to set up an environment variable for your OpenAI API key and install the OpenAI SDK.

### Set up the OpenAI API Key

1. **macOS / Linux**:
   ```bash
   export OPENAI_API_KEY="your_api_key_here"

2. **Windows**:
   ```cmd
   setx OPENAI_API_KEY "your_api_key_here"
### Install the OpenAI SDK:
  ```cmd
   pip install openai
   ```

### Usage
In the zad_artykul.py file, at line 47, there is a reference to artykul.txt. This file should contain the article text that the program will convert to HTML.

#### To run the code, use the following command:
 ```cmd
   python zad_artykul.py
```

This will process the content of artykul.txt and output the resulting HTML.
