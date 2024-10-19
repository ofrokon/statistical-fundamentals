# Statistical Fundamentals for Data Scientists

This repository contains Python scripts demonstrating key statistical concepts crucial for data science. It accompanies the Medium post "Statistical Fundamentals for Data Scientists".

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Visualizations](#visualizations)
4. [Topics Covered](#topics-covered)
5. [Contributing](#contributing)
6. [License](#license)

## Installation

To run these scripts, you need Python 3.6 or later. Follow these steps to set up your environment:

1. Clone this repository:
   ```
   git clone https://github.com/ofrokon/statistical-fundamentals.git
   cd statistical-fundamentals
   ```

2. (Optional) Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

To generate all visualizations, run:

```
python create_visualizations.py
```

This will create PNG files for each visualization in the current directory.

## Visualizations

This script generates the following visualizations:

1. `descriptive_stats.png`: Illustrates basic descriptive statistics of a dataset.
2. `normal_distribution.png`: Shows the probability density function of a standard normal distribution.
3. `hypothesis_test.png`: Demonstrates a two-sample t-test with boxplots.
4. `correlation.png`: Visualizes the correlation between two variables with a scatter plot.
5. `linear_regression.png`: Illustrates a simple linear regression model.

## Topics Covered

- Descriptive Statistics
- Probability Distributions
- Hypothesis Testing
- Correlation and Regression
- Introduction to Bayesian Statistics

Each topic is explained in the accompanying Medium post with Python code examples.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request with your suggested changes.

## License

This project is open source and available under the [MIT License](LICENSE).

---

For a detailed explanation of these statistical concepts and their application in data science, check out the accompanying Medium post: [Statistical Fundamentals for Data Scientists](https://medium.com/yourusername/statistical-fundamentals-for-data-scientists)

For questions or feedback, please open an issue in this repository.
