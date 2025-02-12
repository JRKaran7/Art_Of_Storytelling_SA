# Subject Name: The Art of Storytelling with Data
## Social Media Trends and Global Health Insights Analysis using Tableau
## Scenario 1: Exploring the World of YouTube Influencers-A Deep Dive into Content Trends, Engagement and Viewer Preferences

Student ID: 1000130 <br>
Karan Amol Rajankar </br>
Delhi Public School Bangalore North </br>
Email ID: karan.rajankar07@gmail.com </br>

### Introduction
"Content is King." — Bill Gates (1996) (Evans, 2017)<br> 
This iconic quote from Bill Gates emphasizes that high-quality content is the driving force behind digital success. In the world of YouTube influencers, engaging content shapes audience preferences, builds loyalty, and fuels growth. </br> <br>
This README file provides a structured approach to analyzing YouTube influencer data using Tableau. It explores content trends, engagement metrics, and regional impacts to uncover key success factors. By understanding viewer behavior and influencer performance, brands can refine their marketing strategies and collaborate effectively with high-impact creators. <br> <br>

### Define the Purpose and Understand the Audience
#### Purpose
**1. Identify High-Engagement Content Categories:** <br>
Analyzing which content categories attract the most followers and engagement helps brands align their marketing strategies. By categorizing influencers based on their niche, we can uncover which genres—such as entertainment, education, or gaming—generate the highest audience interaction and sustained viewer interest. <br> <br>
**2. Analyze Viewer Loyalty and Influencer Growth Trends:** <br>
Examining follower growth over time reveals insights into audience loyalty. By comparing channel age, video output, and engagement trends, we can determine whether older channels maintain steady growth or if newer influencers gain rapid traction, helping brands identify the best partnerships for long-term influencer marketing success. <br> <br>
**3. Explore Geographic Trends in Influencer Reach and Engagement:** <br>
Understanding how audience engagement varies by region allows brands to optimize campaigns for specific markets. By mapping follower distributions and analyzing country-based engagement levels, businesses can identify high-potential regions, ensuring that marketing efforts align with areas where influencer content generates the most impact. <br> <br>
**4. Assess the Impact of Branding Elements on Follower Counts:** <br>
Profile aesthetics and content presentation influence audience perception. By evaluating descriptions, video titles, and profile visuals, we can identify patterns that contribute to influencer success. This helps brands and creators refine their online presence to attract more followers and maintain higher engagement rates. <br> <br>

#### Audience
**1. Data-Driven Marketing for Brands & Advertisers:** <br>
Influencer Insights Pvt. Ltd. collaborates with brands and advertisers to refine their marketing strategies using data analytics. They require insights into content performance, audience engagement, and influencer growth to ensure optimal ROI on influencer partnerships. <br> <br>
**2. Optimizing Influencer Selection & Campaigns:** <br>
The company seeks to identify the most impactful influencers based on content trends, follower engagement, and geographic reach. Understanding these factors helps them match brands with influencers who align with their target audience and marketing objectives. <br> <br>
**3. Enhancing Audience Understanding for Better Engagement:** <br>
By analyzing viewer preferences, content categories, and regional impact, the company helps brands create tailored campaigns. Their goal is to leverage high-engagement content trends to drive brand awareness, conversions, and audience loyalty. <br> <br>

### Existing Analysis
The below link provides a report of big data analysis on YouTube with Tableau. It gives a basic understanding of the approach and the methodology that we need to follow when we perform our analysis about influencer reach and engagement on YouTube. <br>

**Report Link: -** [http://www.jatit.org/volumes/Vol99No22/21Vol99No22.pdf](http://www.jatit.org/volumes/Vol99No22/21Vol99No22.pdf)

### Prepare and Preprocess the Dataset
The "channels.csv" dataset contains valuable insights into YouTube channels, content types, engagement metrics, and viewer demographics. To ensure accurate analysis, the data undergoes a rigorous cleaning process, including removing irrelevant columns, handling missing values, and standardizing key variables like follower counts, video genres, and engagement rates. Additionally, duplicates are eliminated, date formats are corrected, and category names are standardized. Finally, the cleaned dataset is structured for seamless Tableau integration, allowing analysis by content categories, geographic location, and influencer engagement trends. This dataset is saved with the name "cleaned_channels.csv". Both of these datasets are provided in the repository to download and understand the changes. <br> <br>
Here are the steps that I have followed while cleaning and preprocessing the dataset: - <br>
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
2. Saves the cleaned dataset as "cleaned_channels.xlsx" for further analysis (It is saved as an excel file so that Tableau can easily and efficiently extract data) <br> <br>
![image](https://github.com/user-attachments/assets/a0ce48c1-2205-4c2c-8027-7aef7c70b48a)

### Explore and Analyse the Data
In the ever-evolving world of YouTube, understanding what drives engagement is crucial for brands and advertisers looking to collaborate with influencers. This analysis leverages the "YouTube 100,000 Influencers" dataset to uncover insights into content trends, viewer loyalty, geographic impact, and branding strategies that shape influencer success.
#### Identifying Popular Content Categories
One of the key aspects of influencer success lies in the type of content they create. By analyzing category_name and followers, we can determine which content genres attract the most viewers and engagement. Categories such as Vlogs, Tutorials, and Entertainment might dominate, while niche categories could show surprising engagement patterns. This insight helps brands align their marketing efforts with high-performing content types that resonate with audiences. <br> <br>
**Analysis Approach:** <br>
• Group influencers by content category (category_name) <br>
• Measure engagement levels by analyzing total followers in each category <br>
• Visualize follower distribution across content types to spot trends <br>

#### Examining Viewer Loyalty and Engagement
A loyal audience is key to an influencer’s long-term growth and brand collaborations. Understanding how follower growth correlates with channel age provides insights into audience retention and engagement. Using join_date, we calculate channel age and track follower growth over time. This helps determine whether older channels maintain steady growth or if newer ones gain rapid traction. <br> <br>
**Analysis Approach:** <br>
• Calculate channel age (difference between join_date and today’s date) <br>
• Analyze follower growth trends across different age groups <br>
• Compare older vs. newer channels to see which maintain or lose engagement over time <br>

#### Analysing Content Localization and Audience Reach
Influencer engagement can vary significantly based on geographic location. By examining country and followers, we can identify which regions contribute to the highest engagement. Some countries may have high follower counts but lower engagement, while others may have smaller but highly engaged audiences. This insight helps brands target the most active regions for influencer collaborations. <br> <br>
**Analysis Approach:** <br>
• Analyze follower distribution across countries <br>
• Assess engagement trends by region <br>
• Identify high-growth geographic markets for influencer marketing <br>

#### Content Presentation and Brand Development
An influencer’s branding and content presentation play a vital role in audience engagement. Elements such as video descriptions, profile visuals, and branding elements can impact follower counts. By analyzing description, picture_url, and followers, we can determine whether specific branding strategies contribute to higher engagement. This insight helps influencers and brands optimize their content for maximum visibility and audience retention. <br> <br>
**Analysis Approach:** <br>
• Examine description styles and their impact on engagement <br>
• Analyze the role of profile visuals in attracting followers <br>
• Identify successful branding patterns among top influencers <br> <br>

Here is a tabular format of the Analysis, Approach, and Impact: - 
![(Inglés)](https://github.com/user-attachments/assets/a2c84e44-de66-429a-ba4a-fda4d1eabf98) <br>
(Made using [https://www.canva.com/](https://www.canva.com/))

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

### Create a Storyboard in Tableau
#### Organise Data into a Narrative
1. The dashboard is structured in a logical flow, beginning with an overview of influencer content categories, followed by engagement trends, regional impact, and concluding with actionable insights. <br>
2. Each section of the storyboard builds upon the previous one, allowing users to explore data step-by-step, making it easier to identify key patterns and trends.
#### Design for Impact
1. The visual elements are carefully selected to ensure clarity, using intuitive charts, graphs, and filters that allow users to interact with the data seamlessly. <br>
2. The layout prioritizes readability, ensuring that insights are easy to interpret, with a balance of visuals and supporting text for better comprehension.

### Add Context and Annotations
#### Provide Explanations
1. Key insights are annotated to provide explanations, ensuring that users understand how factors like content type and location influence engagement and growth. <br>
2. Additional contextual notes help users navigate complex relationships within the data, making the dashboard more user-friendly and insightful.
#### Branding
1. Company branding, including Influencer Insights Pvt. Ltd. colors and logo, has been integrated to maintain a professional and consistent visual identity. <br>
2. A clean and modern design approach enhances the dashboard’s credibility, ensuring that it aligns with industry standards and expectations.

### Test the Dashboard
#### Usability Testing
At Influencer Insights Pvt Ltd, we prioritize user experience. To ensure our dashboard is intuitive, interactive, and efficient, we conducted extensive usability testing. **Key areas of evaluation include:** <br>
**1. Navigation & Accessibility –** Can users easily find insights? <br>
**2. Interactivity –** Do filters, tooltips, and visual elements function smoothly? <br>
**3. Performance & Speed –** Does the dashboard load efficiently? <br>
**4. Device Compatibility –** Is the experience seamless across mobile and desktop? <br> <br>
To further refine the dashboard, we have launched a survey feedback form. Your responses will help us enhance usability and improve the dashboard’s effectiveness. <br> <br>
**Feedback Survey Link: -** [https://docs.google.com/forms/d/e/1FAIpQLSd2-5pUN5KrnV-NKsSkQ8AKR4rK0hvhhEOlHvxR8RKJtyBcdA/viewform?usp=header](https://docs.google.com/forms/d/e/1FAIpQLSd2-5pUN5KrnV-NKsSkQ8AKR4rK0hvhhEOlHvxR8RKJtyBcdA/viewform?usp=header) <br>
**Responses Link: -** [https://docs.google.com/spreadsheets/d/11c4l-ZiAwqDDyKRdM6-OsPIs5pjT6uv77veRazBth3c/edit?usp=sharing](https://docs.google.com/spreadsheets/d/11c4l-ZiAwqDDyKRdM6-OsPIs5pjT6uv77veRazBth3c/edit?usp=sharing)

#### Check for Accuracy
At Influencer Insights Pvt Ltd, ensuring data accuracy is a top priority. Our dashboard is built to provide reliable insights, helping brands, advertisers, and influencer managers make informed decisions. To maintain high standards of accuracy, we have implemented the following validation measures: <br>

**1. Data Source Verification:** <br>
• We ensure that all data used in the dashboard comes from credible sources. <br>
• The dataset is cross-checked against multiple sources to verify consistency. <br> <br>
**2. Data Cleaning & Processing:** <br>
• Raw data undergoes a rigorous cleaning process to remove duplicate or incomplete entries. <br>
• Outliers and inconsistencies are identified and addressed to prevent misleading insights. <br> <br>
**3. Calculation & Metric Validation:** <br>
• Key metrics such as engagement rates, video counts, and category performance are verified with statistical checks. <br>
• Aggregated values are tested to ensure they align with the expected totals. <br> <br>
**4. Dashboard Functionality Testing:** <br>
• Filters and interactive elements are tested to ensure they accurately reflect data selections. <br>
• Visualizations are reviewed to confirm that they display the correct insights without misrepresenting data. <br> <br>
**5. User Feedback & Continuous Monitoring:** <br>
• We encourage users to report any discrepancies they observe. <br>
• Regular updates are made to keep the dashboard aligned with the latest trends and data. <br> <br>

### Publish and Share the Story
#### Publish The Dashboard
There are multiple ways to publish and share a Tableau dashboard, including Tableau Public, Tableau Server, Tableau Online, embedding in a website, or exporting as an image/PDF. However, I chose Google Sites because it provides a simple, accessible, and shareable platform. <br> <br>
**1. Ease of Access:** No additional login or software is required for viewers. <br>
**2. Seamless Integration:** The dashboard can be embedded directly, allowing interactive insights. <br>
**3. Collaboration:** Enables easy sharing with stakeholders, including brands, advertisers, and influencer managers. <br> <br>
This approach ensures that key marketing insights—such as top-performing content categories, regional engagement trends, and content growth patterns—are easily available to decision-makers for data-driven marketing strategies. <br> <br>

**Sites Link: -** [https://sites.google.com/view/aoswdsa/home](https://sites.google.com/view/aoswdsa/home)

#### Share Insights 
• Entertainment leads in engagement, with over 6 billion followers, making it the dominant content category. <br>
• Education and Comedy also attract large audiences, proving that informative and entertaining content drive substantial growth. <br>
• The U.S. and India are the top influencer markets, highlighting prime regions for brand collaborations. <br>
• Channel trailers and branding elements significantly impact audience engagement, proving the importance of strong first impressions. <br>
• Music dominates as the most-produced content category, surpassing News & Politics, Entertainment, and Gaming, highlighting its widespread influence and continuous demand in digital media. <br>
• Content creation peaked in 2014, reaching its highest number of video uploads, followed by a significant decline, indicating a potential shift in platform trends or content strategies post-2014. <br>
• Entertainment and Music categories have the highest number of trailers, indicating strong promotional efforts in these genres to attract audience engagement.

### Storyboard to Depict my Project Journey
![Daily Energy Transfer Storyboard in Cream Light Blue Clean Style (6)](https://github.com/user-attachments/assets/136c8410-f589-4bfe-9dcd-6d623d373f12) <br> <br>
(Made using [https://www.canva.com/](https://www.canva.com/))

### Conclusion
Working on this project has been an insightful journey for Influencer Insights Pvt Ltd, allowing us to explore the power of data visualization using Tableau. Through the development of this interactive dashboard, we gained hands-on experience in handling large datasets, ensuring accuracy, and creating user-friendly visual representations of influencer trends. From data validation to usability testing, every step reinforced the importance of precision and clarity in analytics. Publishing the dashboard via Google Sites provided an accessible and seamless way to share insights with our audience. To enhance its effectiveness, we have launched a survey feedback form, inviting users to share their experiences and help us refine our work further. This project has strengthened our expertise in data-driven decision-making, and we look forward to implementing more innovations in the future.

### Resources
**1. Logo: -** [https://www.canva.com/](https://www.canva.com/) <br>
**2. Visualizations: -** [https://public.tableau.com/app/discover](https://public.tableau.com/app/discover) <br>
**3. Data Cleaning and Preprocessing: -** Python 

### Bibliography
1. Evans, H. (2017, October 28). “content is king” - essay by Bill Gates 1996. Medium. https://medium.com/@HeathEvans/content-is-king-essay-by-bill-gates-1996-df74552f80d9 
2. YouTube. (n.d.). YouTube. https://www.youtube.com/watch?v=f2LYwLd5oGM
3. Add annotations. Tableau. (n.d.). https://help.tableau.com/current/pro/desktop/en-us/annotations_annotations_add.htm
4. Best practices for effective dashboards. Tableau. (n.d.-b). https://help.tableau.com/current/pro/desktop/en-us/dashboards_best_practices.htm
5. YouTube. (n.d.-a). YouTube. https://www.youtube.com/watch?v=6oFTdbrugUs 
