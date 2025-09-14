<p align="center">
  <img src="https://skillicons.dev/icons?i=python" alt="logo python" width="15%">
  <br><br>
  <i>First experiment with Machine Learning basics,<br>
  implementing Linear Regression from scratch with Python.</i>
</p>

---

# 📖 Index
- 📌 [Overview](#-overview)  
- 📥 [Download & Installation](#-download--installation)  
- 📷 [Usage Examples](#-usage-examples)  
- 📄 [License](#-license)  

---

# 📌 Overview

**Linear Regression Project** is a simple implementation of **linear regression** using **Python**, built **from scratch** without libraries like `scikit-learn`.

In this project, the algorithm tries to find the **best-fit line** that describes the relationship between two variables:

* `studytime` → hours of study
* `score` → exam/test score

The process works as follows:

1. The line is defined as **y = m·x + b**, where *m* is the slope and *b* the intercept.
2. The **Mean Squared Error (MSE)** measures how far the predicted values are from the real data points.
3. Using **Gradient Descent**, the values of *m* and *b* are updated step by step to minimize the error.
4. After several iterations, the algorithm converges to the line that best approximates the dataset.

Finally, the program visualizes the results by plotting both the original data points and the regression line📈

---

# 📥 Download & Installation

**⚠️ Python 3.x is required on the machine to run this project.**

1. Download the latest LinearRegression folder (includes all files and the batch file).
2. Make sure Python 3.x is installed and added to your system PATH.
3. Open the folder and double-click run_sentiment_analyzer.bat to start the application.
   
On first run, the batch file will install the required Python packages (from requirements.txt) and download the Hugging Face models (Internet connection required). After that, the app works offline.
Place your dataset as data.csv in the project folder(The CSV must contain at least two columns)

# 📷 Usage Examples
**Example Output (Console)**<br>
<br>![App Screenshot](img/result.png)<br>

**Graphical Output**
<br>![App Screenshot](img/graph.png)<br>

The script will plot:

⚫ Data points (hours of study vs. score)

🔴 Best-fit regression line (calculated via gradient descent)

# 📄 License

Released under the MIT License.
Feel free to use, modify, and share 🚀
