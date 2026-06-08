pip install` if it's strictly Colab. Let's do:
    ```python
    import sys
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-q", "langgraph", "duckduckgo-search"])
    ```
    This is extremely robust and works everywhere.

    