#!/usr/bin/env python3
"""
Talabat UAE Orders Data Analysis
Author: Mohamed Abdulhadi
Description: Comprehensive analysis of Talabat UAE order data including trends, patterns, and visualizations
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from datetime import datetime

def load_and_prepare_data(file_path):
    """Load and prepare the dataset for analysis"""
    print("Loading dataset...")
    df = pd.read_csv(file_path)
    
    # Convert datetime column
    df['order_datetime'] = pd.to_datetime(df['order_datetime'])
    df['order_date'] = df['order_datetime'].dt.date
    
    print(f"Dataset loaded: {len(df)} orders from {len(df['order_date'].unique())} days")
    return df

def explore_data(df):
    """Basic data exploration and statistics"""
    print("\n" + "="*50)
    print("DATA EXPLORATION")
    print("="*50)
    
    # Basic info
    print("\nDataset Info:")
    df.info()
    
    # Summary statistics
    print("\nSummary Statistics:")
    print(df.describe())
    
    # Missing values
    print("\nMissing Values:")
    print(df.isnull().sum())
    
    # Data quality checks
    print(f"\nData Quality Checks:")
    print(f"Zero order values: {(df['order_value'] == 0).sum()}")
    print(f"Negative delivery times: {(df['delivery_time_min'] < 0).sum()}")
    print(f"Negative delivery fees: {(df['delivery_fee'] < 0).sum()}")

def analyze_daily_trends(df):
    """Analyze daily order trends"""
    print("\n" + "="*50)
    print("DAILY TRENDS ANALYSIS")
    print("="*50)
    
    # Group by date
    daily_orders = df.groupby('order_date').size().reset_index(name='order_count')
    daily_orders['order_date'] = pd.to_datetime(daily_orders['order_date'])
    
    # Add rolling average
    daily_orders['rolling_avg'] = daily_orders['order_count'].rolling(window=7).mean()
    
    print(f"Total days: {len(daily_orders)}")
    print(f"Average orders per day: {daily_orders['order_count'].mean():.1f}")
    print(f"Max orders in a day: {daily_orders['order_count'].max()}")
    print(f"Min orders in a day: {daily_orders['order_count'].min()}")
    
    # Top busiest days
    print("\nTop 5 busiest days:")
    print(daily_orders.nlargest(5, 'order_count')[['order_date', 'order_count']])
    
    return daily_orders

def analyze_city_trends(df):
    """Analyze order trends by city"""
    print("\n" + "="*50)
    print("CITY TRENDS ANALYSIS")
    print("="*50)
    
    # City statistics
    city_stats = df.groupby('city').size().sort_values(ascending=False)
    print("Total orders by city:")
    print(city_stats)
    
    # Daily trends by city
    city_trends = df.groupby(['order_date', 'city']).size().reset_index(name='order_count')
    city_trends['order_date'] = pd.to_datetime(city_trends['order_date'])
    
    # Average daily orders per city
    avg_daily_city = city_trends.groupby('city')['order_count'].mean().sort_values(ascending=False)
    print("\nAverage daily orders per city:")
    print(avg_daily_city.round(1))
    
    return city_trends

def create_visualizations(daily_orders, city_trends):
    """Create and save visualizations"""
    print("\n" + "="*50)
    print("CREATING VISUALIZATIONS")
    print("="*50)
    
    # Set style
    plt.style.use('default')
    sns.set_palette("husl")
    
    # 1. Daily orders trend with smoothing
    plt.figure(figsize=(14, 6))
    sns.lineplot(data=daily_orders, x='order_date', y='rolling_avg', label='7-Day Rolling Avg', linewidth=2)
    sns.lineplot(data=daily_orders, x='order_date', y='order_count', alpha=0.3, label='Daily Orders')
    plt.title('Talabat UAE - Daily Orders Trend (7-Day Moving Average)', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Number of Orders', fontsize=12)
    plt.legend()
    plt.xticks(rotation=45)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('daily_orders_trend.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ Daily orders trend plot saved")
    
    # 2. City trends comparison
    plt.figure(figsize=(14, 6))
    sns.lineplot(data=city_trends, x='order_date', y='order_count', hue='city', linewidth=1.5)
    plt.title('Talabat UAE - Daily Orders by City', fontsize=16, fontweight='bold')
    plt.xlabel('Date', fontsize=12)
    plt.ylabel('Number of Orders', fontsize=12)
    plt.legend(title='City', bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('city_trends.png', dpi=300, bbox_inches='tight')
    plt.close()
    print("✓ City trends plot saved")

def analyze_business_insights(df):
    """Extract key business insights"""
    print("\n" + "="*50)
    print("BUSINESS INSIGHTS")
    print("="*50)
    
    # Order value analysis
    print("Order Value Analysis:")
    print(f"Average order value: AED {df['order_value'].mean():.2f}")
    print(f"Median order value: AED {df['order_value'].median():.2f}")
    print(f"Total revenue: AED {df['order_value'].sum():,.2f}")
    
    # Delivery analysis
    print(f"\nDelivery Analysis:")
    print(f"Average delivery time: {df['delivery_time_min'].mean():.1f} minutes")
    print(f"Average delivery fee: AED {df['delivery_fee'].mean():.2f}")
    
    # Payment methods
    print(f"\nPayment Methods:")
    payment_dist = df['payment_method'].value_counts()
    for method, count in payment_dist.items():
        print(f"{method}: {count} ({count/len(df)*100:.1f}%)")
    
    # Promo code usage
    promo_usage = df['promo_code_used'].value_counts()
    print(f"\nPromo Code Usage:")
    for usage, count in promo_usage.items():
        print(f"{usage}: {count} ({count/len(df)*100:.1f}%)")
    
    # Restaurant categories
    print(f"\nTop Restaurant Categories:")
    top_categories = df['restaurant_category'].value_counts().head()
    for category, count in top_categories.items():
        print(f"{category}: {count} ({count/len(df)*100:.1f}%)")

def main():
    """Main analysis function"""
    print("TALABAT UAE ORDERS DATA ANALYSIS")
    print("="*50)
    print(f"Analysis started at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    
    # Load data
    df = load_and_prepare_data('talabat_uae_orders_dataset.csv')
    
    # Run analysis
    explore_data(df)
    daily_orders = analyze_daily_trends(df)
    city_trends = analyze_city_trends(df)
    create_visualizations(daily_orders, city_trends)
    analyze_business_insights(df)
    
    print(f"\n" + "="*50)
    print("ANALYSIS COMPLETED")
    print("="*50)
    print("Generated files:")
    print("- daily_orders_trend.png")
    print("- city_trends.png")
    print(f"Analysis completed at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

if __name__ == "__main__":
    main()