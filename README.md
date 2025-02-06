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
Analyzing which content categories attract the most followers and engagement helps brands align their marketing strategies. By categorizing influencers based on their niche, we can uncover which genres—such as entertainment, education, or gaming—generate the highest audience interaction and sustained viewer interest. <br> <br>
2. Analyze Viewer Loyalty and Influencer Growth Trends: <br>
Examining follower growth over time reveals insights into audience loyalty. By comparing channel age, video output, and engagement trends, we can determine whether older channels maintain steady growth or if newer influencers gain rapid traction, helping brands identify the best partnerships for long-term influencer marketing success.
3. Explore Geographic Trends in Influencer Reach and Engagement: <br>
Understanding how audience engagement varies by region allows brands to optimize campaigns for specific markets. By mapping follower distributions and analyzing country-based engagement levels, businesses can identify high-potential regions, ensuring that marketing efforts align with areas where influencer content generates the most impact. <br> <br>
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
• Dataset Overview and Initial Inspection <br>
1. Loads the "YouTube 100,000 Influencers" dataset: <br>
2. Prints dataset information and first 5 rows for verification <br> <br> 
![image](https://github.com/user-attachments/assets/b39449f8-6ab6-4154-aafb-7ab17b8ab357) <br> <br>
• Data Cleaning Steps <br>
1. Removes irrelevant columns (profile_url, picture_url, etc.) <br> <br>
2. Handles missing values (fills category_name, country, followers, engagement_rate with defaults) <br> <br>
3. Converts join_date to a proper datetime format for time-based analysis <br> <br>
4. Removes duplicate records to avoid redundant data <br> <br>
5. Ensures followers are numeric (corrects formatting issues) <br> <br>
6. Standardizes category names (title-case formatting for consistency) <br> <br>
• Preparing Data for Tableau <br>
1. Structures data to allow analysis by content categories & location <br> <br>
2. Saves the cleaned dataset as "cleaned_channels.csv" for further analysis <br> <br>
