# Subject Name: The Art of Storytelling with Data
## Social Media Trends and Global Health Insights Analysis using Tableau
## Scenario 1: Exploring the World of YouTube Influencers-A Deep Dive into Content Trends, Engagement and Viewer Preferences

Student ID: 1000130 <br>
Karan Amol Rajankar </br>
Delhi Public School Bangalore North </br>
Email ID: karan.rajankar07@gmail.com </br>

### Introduction
"Content is King." — Bill Gates (1996) <br> 
This iconic quote from Bill Gates emphasizes that high-quality content is the driving force behind digital success. In the world of YouTube influencers, engaging content shapes audience preferences, builds loyalty, and fuels growth. </br> <br>
This README file provides a structured approach to analyzing YouTube influencer data using Tableau. It explores content trends, engagement metrics, and regional impacts to uncover key success factors. By understanding viewer behavior and influencer performance, brands can refine their marketing strategies and collaborate effectively with high-impact creators. <br> <br>

### Define the Purpose and Understand the Audience
#### Purpose
1. Identify High-Engagement Content Categories: <br>
Analyzing which content categories attract the most followers and engagement helps brands align their marketing strategies. By categorizing influencers based on their niche, we can uncover which genres—such as entertainment, education, or gaming—generate the highest audience interaction and sustained viewer interest.
2. Analyze Viewer Loyalty and Influencer Growth Trends: <br>
Examining follower growth over time reveals insights into audience loyalty. By comparing channel age, video output, and engagement trends, we can determine whether older channels maintain steady growth or if newer influencers gain rapid traction, helping brands identify the best partnerships for long-term influencer marketing success.
3. Explore Geographic Trends in Influencer Reach and Engagement: <br>
Understanding how audience engagement varies by region allows brands to optimize campaigns for specific markets. By mapping follower distributions and analyzing country-based engagement levels, businesses can identify high-potential regions, ensuring that marketing efforts align with areas where influencer content generates the most impact. 
4. Assess the Impact of Branding Elements on Follower Counts: <br>
Profile aesthetics and content presentation influence audience perception. By evaluating descriptions, video titles, and profile visuals, we can identify patterns that contribute to influencer success. This helps brands and creators refine their online presence to attract more followers and maintain higher engagement rates. <br> <br>

#### Audience
1. Data-Driven Marketing for Brands & Advertisers: <br>
Influencer Insights Pvt. Ltd. collaborates with brands and advertisers to refine their marketing strategies using data analytics. They require insights into content performance, audience engagement, and influencer growth to ensure optimal ROI on influencer partnerships. <br> <br>
2. Optimizing Influencer Selection & Campaigns:
The company seeks to identify the most impactful influencers based on content trends, follower engagement, and geographic reach. Understanding these factors helps them match brands with influencers who align with their target audience and marketing objectives. <br> <br>
3. Enhancing Audience Understanding for Better Engagement: <br>
By analyzing viewer preferences, content categories, and regional impact, the company helps brands create tailored campaigns. Their goal is to leverage high-engagement content trends to drive brand awareness, conversions, and audience loyalty. <br> <br>

### Prepare and Preprocess the Dataset
The "channels.csv" dataset contains valuable insights into YouTube channels, content types, engagement metrics, and viewer demographics. To ensure accurate analysis, the data undergoes a rigorous cleaning process, including removing irrelevant columns, handling missing values, and standardizing key variables like follower counts, video genres, and engagement rates. Additionally, duplicates are eliminated, date formats are corrected, and category names are standardized. Finally, the cleaned dataset is structured for seamless Tableau integration, allowing analysis by content categories, geographic location, and influencer engagement trends. This dataset is saved with the name "cleaned_channels.csv". Both of these datasets are provided in the repository to download and understand the changes. <br>
Here are the steps that I have followed while cleaning and preprocessing the dataset: - <br> <br>
#### Dataset Overview and Initial Inspection
1. Loads the "YouTube 100,000 Influencers" dataset
2. Prints dataset information and first 5 rows for verification <br> <br>
![image](https://github.com/user-attachments/assets/1715cf76-0459-4434-8a60-e226632c96a6)
#### Data Cleaning Steps
1. Removes irrelevant columns (profile_url, picture_url, etc.) <br> <br>
![image](https://github.com/user-attachments/assets/e1e9796f-d014-41b9-ae0d-df0440b99eed) <br> <br>
2. Handles missing values (fills category_name, country, followers, engagement_rate with defaults) <br> <br>
![image](https://github.com/user-attachments/assets/eac55941-d8ce-47e7-99ee-018eca9ad098) <br> <br>
![image](https://github.com/user-attachments/assets/5f40c98a-bdc0-433f-ad13-fa4d26072b57) <br> <br>
3. Converts join_date to a proper datetime format for time-based analysis <br> <br>
![image](https://github.com/user-attachments/assets/3a9adf88-51f6-48bd-b333-bdb56b5bf118) <br> <br>
4. Ensures followers are numeric (corrects formatting issues) <br> <br>
![image](https://github.com/user-attachments/assets/f23276c5-d6ab-4771-b94a-b8307e2190fc) <br> <br>
5. Standardizes category names (title-case formatting for consistency) <br> <br>
![image](https://github.com/user-attachments/assets/57fe835f-056d-44ff-84cc-e34782092465)
#### Preparing Data for Tableau
1. Structures data to allow analysis by content categories & location
2. Saves the cleaned dataset as "cleaned_channels.csv" for further analysis <br> <br>
![image](https://github.com/user-attachments/assets/38a506f1-375e-4f71-8810-102c1f59d86a)

### Explore and Analyse the Data
In the ever-evolving world of YouTube, understanding what drives engagement is crucial for brands and advertisers looking to collaborate with influencers. This analysis leverages the "YouTube 100,000 Influencers" dataset to uncover insights into content trends, viewer loyalty, geographic impact, and branding strategies that shape influencer success.
#### Identifying Popular Content Categories
One of the key aspects of influencer success lies in the type of content they create. By analyzing category_name and followers, we can determine which content genres attract the most viewers and engagement. Categories such as Vlogs, Tutorials, and Entertainment might dominate, while niche categories could show surprising engagement patterns. This insight helps brands align their marketing efforts with high-performing content types that resonate with audiences. <br> <br>
Analysis Approach: <br>
• Group influencers by content category (category_name) <br>
• Measure engagement levels by analyzing total followers in each category <br>
• Visualize follower distribution across content types to spot trends <br>

#### Examining Viewer Loyalty and Engagement
A loyal audience is key to an influencer’s long-term growth and brand collaborations. Understanding how follower growth correlates with channel age provides insights into audience retention and engagement. Using join_date, we calculate channel age and track follower growth over time. This helps determine whether older channels maintain steady growth or if newer ones gain rapid traction. <br> <br>
Analysis Approach: <br>
• Calculate channel age (difference between join_date and today’s date) <br>
• Analyze follower growth trends across different age groups <br>
• Compare older vs. newer channels to see which maintain or lose engagement over time <br>

#### Analysing Content Localization and Audience Reach
Influencer engagement can vary significantly based on geographic location. By examining country and followers, we can identify which regions contribute to the highest engagement. Some countries may have high follower counts but lower engagement, while others may have smaller but highly engaged audiences. This insight helps brands target the most active regions for influencer collaborations. <br> <br>
Analysis Approach: <br>
• Analyze follower distribution across countries <br>
• Assess engagement trends by region <br>
• Identify high-growth geographic markets for influencer marketing <br>

#### Content Presentation and Brand Development
An influencer’s branding and content presentation play a vital role in audience engagement. Elements such as video descriptions, profile visuals, and branding elements can impact follower counts. By analyzing description, picture_url, and followers, we can determine whether specific branding strategies contribute to higher engagement. This insight helps influencers and brands optimize their content for maximum visibility and audience retention. <br> <br>
Analysis Approach: <br>
• Examine description styles and their impact on engagement <br>
• Analyze the role of profile visuals in attracting followers <br>
• Identify successful branding patterns among top influencers <br> <br>

Here is a tabular format of the Analysis, Approach, and Impact: - 
![(Inglés)](https://github.com/user-attachments/assets/a2c84e44-de66-429a-ba4a-fda4d1eabf98)

### Design the Visuals
To effectively present insights from the YouTube 100,000 Influencers dataset, we will use a range of visualizations that make it easy to understand content trends, engagement patterns, and geographic reach. These visuals will help brands and advertisers optimize their influencer marketing strategies.
#### Choose Visualizations
To ensure clear and actionable insights, the following visualizations will be implemented: <br>
• **Bar Charts:** Display the most popular content categories by follower count and engagement rate to highlight which genres attract the most audience interest. <br>
• **Line Charts (Trend Lines):** Show follower growth over time, segmented by channel age, to identify long-term engagement trends. <br>
• **Geographic Heatmaps:** Illustrate regional distribution of influencers by mapping follower density and engagement levels in different countries. <br>
• **Scatter Plots:** Analyze how branding elements like descriptions, profile visuals, and video titles correlate with follower growth and engagement. <br>
• **Treemaps:** Provide a hierarchical view of influencer categories, allowing users to see which sub-genres contribute most to engagement. <br>
#### Interactive Features
To enhance usability, the dashboard will include: <br>
• **Filters for Region, Content Type, and Engagement Level:** Users can dynamically adjust the view to analyze specific geographic markets, content genres, or engagement patterns. <br>
• **Hover-Over Insights:** Detailed statistics will appear when hovering over chart elements, providing additional metrics such as average watch time, likes, and comments. <br>
• **Comparison Mode:** Users can compare two or more influencers, content types, or regions side by side to identify performance differences. <br>
• **Time-Based Trends:** The dashboard will allow users to analyze how engagement and follower count evolved over months or years, helping brands predict future trends. <br>



#### Story
Main focus is comparing all categories with followers to understand the trend 
