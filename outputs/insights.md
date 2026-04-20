# 🧠 Problem Understanding

## Problem Statement
Revenue has declined by 15% over a recent period, indicating a breakdown in one or more parts of the revenue engine (traffic, conversion, pricing, or retention). The core problem is to identify whether this drop is driven by reduced customer acquisition, lower conversion rates, decreased customer spending, or increased churn—and determine the primary drivers behind the decline.

## Key Metrics
To diagnose the issue, break revenue into its core components:

Revenue = Traffic × Conversion Rate × Average Order Value (AOV)

Track the following:

Traffic / Acquisition
Website/App visits
New vs returning users
Channel-wise traffic (organic, paid, referral, direct)
Conversion Funnel
Conversion rate (visit → purchase)
Drop-off rates at each funnel stage
Monetization
Average Order Value (AOV)
Pricing changes
Discounting levels
Retention / Customer Health
Repeat purchase rate
Churn rate
Customer Lifetime Value (LTV)
External / Business Factors
Seasonality trends
Competitor activity
Market demand shifts

## Assumptions
The 15% drop is recent and not part of normal seasonality
Data tracking and analytics are accurate and consistent
No major one-time events (e.g., outages, policy changes) have already been identified
Business model and pricing structure have not drastically changed (unless being investigated)
Customer behavior patterns are comparable to previous periods unless impacted by external factors


# 📊 Data Insights

## Key Trends
Overall Decline (Jan 1 → Jan 5)
Traffic drops from 1000 → 850 (~15% decline)
Conversion rate drops from 5% → 4.2%
Revenue drops from 5000 → 3570 (~28% decline)
👉 This suggests compounding impact (traffic ↓ + conversion ↓ = sharper revenue decline)
Mid-week Recovery Spike (Jan 4)
Traffic: 1100 (highest)
Conversion: 5.2% (highest)
Revenue: 5720 (highest)
👉 Indicates a temporary positive event (campaign, offer, or weekday effect)
Consistent Drop on Mobile Days
Jan 2, 3, 5 (Mobile-heavy days) show:
Lower traffic
Lower conversion
Lower revenue
👉 Mobile performance is consistently weaker

## Anomalies
Jan 4 Spike
Sudden jump across all metrics
Breaks downward trend
👉 Likely due to:
Marketing campaign
Promotional event
Weekday vs weekday behavior shift
Sharp Revenue Drop vs Traffic Drop
Traffic drops ~15%, but revenue drops ~28%
👉 Indicates conversion rate decline is a major issue, not just traffic

## Segment Insights
1. Device-Level Insights

Desktop:

Jan 1 & Jan 4
Higher conversion rates: 5%+, 5.2%
Higher revenue efficiency

Mobile:

Jan 2, 3, 5
Lower conversion rates: 4.8% → 4.2% (declining)
Drives majority of decline

👉 Insight:
Mobile experience is likely broken or suboptimal (UX issues, slow load, checkout friction)

  2. Time-Based Insights
Early period (Jan 1): Strong baseline
Mid-period (Jan 2–3): Decline begins
Jan 4: Temporary recovery
Jan 5: Drops again

👉 Insight:
This is not random — looks like:

Either campaign ended
Or user quality degraded over time
3. Funnel Insight (Hidden but Important)

Revenue = Traffic × Conversion Rate × Value

Both top of funnel (traffic) and bottom (conversion) are declining
Conversion decline is sharper → bigger lever


# 🔍 Root Cause Analysis

## Root Causes
1. Mobile Experience Degradation
Conversion rate is specifically dropping on mobile
Indicates UX, performance, or usability issues on mobile devices
2. Traffic Quality Decline
Overall traffic is declining over time
Likely shift in acquisition channels bringing lower-intent users
3. Incident or Change on Jan 3
Sharp drop on Jan 3 suggests a one-time trigger event
Could be release, outage, tracking issue, or campaign change
4. Channel / Device Mix Shift
Increasing share of mobile users (who convert worse)
Pulling down overall conversion rate and revenue

## Supporting Reasoning
1. Why Mobile is the Core Problem
You explicitly see: mobile users performing worse than desktop
Combined with: conversion rate dropping on mobile
This strongly signals:
Broken UI elements (forms, checkout, buttons)
Slow page load speeds on mobile
Poor responsive design

👉 Impact: Even if traffic stays constant, revenue drops because fewer users convert.

2. Why Traffic Decline Matters
Traffic is consistently decreasing → top-of-funnel issue
Possible reasons:
Reduced marketing spend
SEO ranking drop
Campaign fatigue

👉 Impact: Fewer users entering funnel → lower total revenue

3. Why Jan 3 is Critical
Sudden drop ≠ natural variation
Usually tied to a specific event:
New product release / bug
Tracking failure (data issue)
Campaign turned off
Site outage or slowdown

👉 This is likely the trigger point that accelerated the decline

4. Why Device Mix is Hurting Overall Performance
If mobile traffic share increased while:
Mobile CVR ↓
Desktop CVR stable

Then:

Overall conversion rate declines even if nothing else changes

👉 This is a composition problem, not just performance
