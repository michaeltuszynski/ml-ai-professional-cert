# Mini-Lesson 18.2: Setting Up Your Coding Environment and Installing NLTK

The NLTK library is a suite that contains libraries and programs for statistical language processing. Among the most potent NLP libraries, it consists of packages to help machines understand human language and respond appropriately. This mini-lesson covers the installation of NLTK for Python ≥ 3.7 environments.

> **Note:** NLTK requires Python version 3.7, 3.8, 3.9, 3.10, or 3.11.

## Mac/Unix
Use the following steps to install and test NLTK on Mac/Unix:

1. To install NLTK, run the following line of code from the terminal:
   ```bash
   pip install --user -U nltk
   ```

2. To (optionally) install NumPy, run the following line of code:
   ```bash
   pip install --user -U numpy
   ```

3. Test the NLTK installation by going to the Python prompt and then importing the library:
   ```python
   import nltk
   ```

**Note:** For issues with "ntlk" or "numpy" installation or version compatibility issues, please refer to the official documentation to identify compatible versions for your system configurations:

- [NTLK official library](https://www.nltk.org/)
- [NumPy official library](https://numpy.org/)

## Windows
Use the following steps to install and test NLTK on Windows:

1. To install NLTK, run the following line of code from the command prompt:
   ```bash
   pip install nltk
   ```

2. To test the install, run the following code from the command prompt:
   ```python
   import nltk
   ```

## Anaconda
There are three ways to install NLTK in Anaconda. You only need to perform one of these:

1. Install NLTK using a Jupyter Notebook by opening a blank Jupyter Notebook and running the following code:
   ```python
   pip install nltk
   ```

2. Install NLTK using the prompt by running the following code:
   ```bash
   pip install nltk
   ```

3. Install NLTK through the Anaconda Navigator using the following steps:
   - Select the environments tab (on the left)
   - Select "Not installed" in the filter at the top
   - Use the search box to search for NLTK
   - Select NLTK
   - Select the "Apply" button

   To test the install, open a blank Jupyter Notebook and try to install NLTK again (`pip install nltk`). If NLTK installs successfully, the Jupyter Notebook will return "Requirement already satisfied."

## Downloading NLTK
Many components of NLTK will not be present after installation, so you will not be able to use some of NLTK's features. In the Python shell, or a Jupyter Notebook, you can run `ntlk.download()` to select the additional packages you want to install using the user interface. As an alternative, you can use `Python -m nltk.downloader [package name]`. You have some additional options from the command prompt and terminal to download packages:

- Opening the package downloader:
  ```python
  nltk.download()
  ```
- Downloading all available packages:
  ```python
  nltk.download('all')
  ```
- Downloading a specific package:
  ```python
  nltk.download('package-name')
  ```