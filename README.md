# Talabat UAE Orders Data Analysis

A comprehensive data analysis project examining order patterns, trends, and business insights from Talabat UAE delivery data.

## 📊 Project Overview

This project analyzes 10,000 orders from Talabat UAE across 5 major cities over a 6-month period (December 2024 - June 2025). The analysis provides insights into daily ordering patterns, city-wise performance, and key business metrics.

## 🔍 Key Findings

### Daily Order Trends
- **Average daily orders**: 54.9 orders/day
- **Peak day**: June 14, 2025 (77 orders)
- **Order range**: 3-77 orders per day
- **Trend**: Relatively stable with seasonal variations

### City Performance
| City | Total Orders | Avg Daily Orders |
|------|-------------|------------------|
| Ajman | 2,048 | 11.3 |
| Sharjah | 2,041 | 11.2 |
| Abu Dhabi | 1,991 | 11.0 |
| Ras Al Khaimah | 1,968 | 10.9 |
| Dubai | 1,952 | 10.8 |

### Business Metrics
- **Average order value**: AED 73.31
- **Average delivery time**: 30 minutes
- **Average delivery fee**: AED 5.02
- **Data coverage**: 182 days across 5 UAE cities

## 🛠 Technologies Used

- **Python 3.9+**
- **Pandas** - Data manipulation and analysis
- **Matplotlib** - Data visualization
- **Seaborn** - Statistical visualization
- **NumPy** - Numerical operations

## 📁 Project Structure

```
talabat-uae-analysis/
├── README.md                          # Project documentation
├── requirements.txt                   # Python dependencies
├── talabat_analysis.py               # Main analysis script
├── talabat_uae_orders_dataset.csv    # Raw dataset
├── daily_orders_trend.png            # Daily trends visualization
└── city_trends.png                   # City comparison visualization
```

## 🚀 Getting Started

### Prerequisites
- Python 3.9 or higher
- pip package manager

### Installation

1. Clone the repository:
```bash
git clone https://github.com/mohamedibnomer/talabat-uae-analysis.git
cd talabat-uae-analysis
```

2. Install required packages:
```bash
pip install -r requirements.txt
```

3. Run the analysis:
```bash
python talabat_analysis.py
```

## 📈 Visualizations

The project generates the following visualizations:

1. **Daily Orders Trend** - Shows daily order counts with 7-day moving average
2. **City Trends Comparison** - Compares daily performance across all 5 cities

## 🔍 Analysis Features

- **Data Quality Assessment** - Identifies and reports data issues
- **Time Series Analysis** - Daily trends with smoothing
- **Geographic Analysis** - City-wise performance comparison
- **Business Intelligence** - Key metrics and insights
- **Statistical Summary** - Comprehensive data statistics

## 📊 Data Quality Notes

The dataset contains some data quality issues:
- Zero order values (likely promotions/cancellations)
- Negative delivery times (data entry errors)
- Negative delivery fees (promotional discounts)

## 🤝 Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

**Mohamed Abdulhadi**
- Data Analyst & Business Intelligence Specialist
- LinkedIn: [Mohamed Abdulhadi](https://linkedin.com/in/mohamedibnomer)
- Email: mohamed.abdulhadi@example.com

## 🙏 Acknowledgments

- Talabat UAE for the dataset
- Python data science community for excellent libraries
- UAE market for providing interesting delivery patterns

## 📞 Contact

For questions or collaboration opportunities, please reach out via:
- GitHub Issues
- LinkedIn messaging
- Email

---
*Last updated: June 2025*