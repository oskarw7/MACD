# MACD Technical Analysis Project

## Overview

This project presents a comprehensive analysis of the MACD (Moving Average Convergence/Divergence) stock market indicator, examining its effectiveness in generating buy and sell signals across different market conditions and financial instruments.

## About MACD

The MACD is one of the most popular and straightforward technical indicators used in financial markets. It analyzes the convergence and divergence of exponential moving averages (EMA) to identify potential trend changes and trading opportunities.

### Key Components
- **MACD Line**: Difference between 12-period and 26-period EMA
- **Signal Line**: 9-period EMA of the MACD line
- **Trading Signals**: Generated when MACD crosses above (buy) or below (sell) the Signal line

## Project Methodology

### Data Sources
The analysis was conducted using two distinct financial instruments with different characteristics:

1. **Ethereum (ETH/USD)**: A highly volatile cryptocurrency experiencing dynamic price changes
2. **Dow Jones Industrial Average (DJI)**: A traditional stock index with stable upward trends

Both instruments were analyzed over the same time period (May 2022 - February 2025) using daily closing prices.

### Analysis Approach
- Implementation of MACD calculations using exponential moving averages
- Visual analysis of buy/sell signals on price charts
- Portfolio simulation comparing MACD strategy vs. buy-and-hold strategy
- Performance evaluation across different market conditions

## Key Findings

### Strengths of MACD
- **Trend Detection**: Effective at identifying trend changes, particularly in stable upward or downward trends
- **Risk Management**: Often provides signals to close positions before major declines
- **Long-term Perspective**: Well-suited for medium to long-term investment strategies
- **Simplicity**: Easy to implement and interpret

### Limitations Identified
- **Signal Delays**: Frequent lag in buy/sell signals, potentially reducing profits or creating losses
- **Horizontal Markets**: Poor performance during sideways/range-bound market conditions
- **False Signals**: Generation of numerous misleading signals, especially in volatile conditions
- **Volume Ignorance**: Does not consider trading volume, which is crucial for short-term trading

### Market-Specific Performance
- **Volatile Assets (ETH)**: Generated many signals but with mixed results; particularly struggled during horizontal trending periods
- **Stable Trends (DJI)**: Performed significantly better with fewer but more accurate signals during consistent upward trends

## Simulation Results

The portfolio simulation revealed important insights:
- More transactions resulted in losses than profits for both instruments
- Despite generating profits, the MACD strategy underperformed a simple buy-and-hold approach
- Performance gap was more pronounced with volatile assets compared to stable trending markets
- Results suggest MACD should not be the only decision-making tool for trading

## Conclusions

### Practical Applications
MACD proves most valuable when:
- Applied to medium and long-term investment strategies
- Used with assets showing stable trending behavior
- Combined with other technical indicators for confirmation
- Applied by investors who understand market context

### Recommended Improvements
To enhance MACD effectiveness, consider incorporating:
- **RSI (Relative Strength Index)**: For measuring trend strength
- **Volume Analysis**: To gauge investor activity levels
- **MACD Histogram**: For additional trend reversal signals
- **Multiple Timeframe Analysis**: To confirm signals across different periods

## Docs
This project includes report written in Polish, see  `report.pdf`.
