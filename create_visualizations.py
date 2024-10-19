import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
from sklearn.linear_model import LinearRegression

def save_plot(fig, filename):
    plt.show()
    fig.savefig(filename, dpi=300, bbox_inches='tight')
    plt.close(fig)

# 1. Descriptive Statistics
def plot_descriptive_stats():
    data = [2, 4, 4, 4, 5, 5, 7, 9]
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.bar(range(len(data)), sorted(data))
    ax.axhline(np.mean(data), color='r', linestyle='dashed', linewidth=2, label='Mean')
    ax.axhline(np.median(data), color='g', linestyle='dashed', linewidth=2, label='Median')
    ax.set_title("Descriptive Statistics")
    ax.set_xlabel("Index")
    ax.set_ylabel("Value")
    ax.legend()
    
    stats_text = f"""
    Mean: {np.mean(data):.2f}
    Median: {np.median(data):.2f}
    Mode: {max(set(data), key=data.count)}
    Range: {np.ptp(data)}
    Variance: {np.var(data):.2f}
    Standard Deviation: {np.std(data):.2f}
    """
    ax.text(0.05, 0.95, stats_text, transform=ax.transAxes, fontsize=10, verticalalignment='top')
    
    save_plot(fig, 'descriptive_stats.png')

# 2. Normal Distribution
def plot_normal_distribution():
    x = np.linspace(-5, 5, 100)
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.plot(x, stats.norm.pdf(x, 0, 1))
    ax.set_title("Standard Normal Distribution")
    ax.set_xlabel("x")
    ax.set_ylabel("Probability Density")
    save_plot(fig, 'normal_distribution.png')

# 3. Hypothesis Testing
def plot_hypothesis_test():
    group1 = [5, 7, 5, 3, 5, 3, 3, 9]
    group2 = [8, 1, 4, 6, 6, 4, 1, 2]
    
    t_statistic, p_value = stats.ttest_ind(group1, group2)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    ax.boxplot([group1, group2])
    ax.set_xticklabels(['Group 1', 'Group 2'])
    ax.set_title("Two-Sample T-Test")
    ax.text(0.05, 0.95, f"T-statistic: {t_statistic:.2f}\nP-value: {p_value:.4f}", 
            transform=ax.transAxes, fontsize=10, verticalalignment='top')
    save_plot(fig, 'hypothesis_test.png')

# 4. Correlation
def plot_correlation():
    np.random.seed(0)
    x = np.random.randn(100)
    y = 2*x + np.random.randn(100)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=x, y=y, ax=ax)
    ax.set_title(f"Correlation: {np.corrcoef(x, y)[0, 1]:.2f}")
    save_plot(fig, 'correlation.png')

# 5. Linear Regression
def plot_linear_regression():
    np.random.seed(0)
    x = np.random.randn(100)
    y = 2*x + np.random.randn(100)
    X = x.reshape(-1, 1)
    model = LinearRegression().fit(X, y)
    
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(x=x, y=y, ax=ax)
    ax.plot(x, model.predict(X), color='red')
    ax.set_title(f"Linear Regression (R² = {model.score(X, y):.2f})")
    save_plot(fig, 'linear_regression.png')

if __name__ == "__main__":
    plot_descriptive_stats()
    plot_normal_distribution()
    plot_hypothesis_test()
    plot_correlation()
    plot_linear_regression()
    print("All visualizations have been saved as PNG files.")