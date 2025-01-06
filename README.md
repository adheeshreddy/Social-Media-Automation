# Social Media Automation

This project automates posting to Twitter, Facebook, and Instagram using their respective APIs. The main goal of this project is to provide an easy-to-use script to post text, images, and videos to these social media platforms.

### Features:
- **Twitter**: Post text, images, and videos to Twitter using the Tweepy API.
- **Facebook**: Post text, images, and videos to Facebook using the Graph API.
- **Instagram**: Post images and videos to Instagram using Instaloader (non-official API).

# outputs :

twitter test account link : [Follow me on X](https://x.com/adhitestaccount)

![Screenshot (1228)](https://github.com/user-attachments/assets/07677273-3e7c-4214-b816-f1a3723b6da4)

![Screenshot (1229)](https://github.com/user-attachments/assets/56f36b80-8b51-4145-956c-354f76fa0d9b)

![Screenshot (1230)](https://github.com/user-attachments/assets/bfcba2f5-9ffb-48c0-94f1-c8005eefa2cb)

Instagram test account outputs :

![Screenshot (1222)](https://github.com/user-attachments/assets/fb5e3d5e-ca91-4e2f-af86-fbb5d4f813e7)

![Screenshot (1223)](https://github.com/user-attachments/assets/a100c861-10da-4a8a-80ee-4557a7e95c14)

Facebook test account page outputs :

facebook test page link : [Facebook test page](https://www.facebook.com/profile.php?id=61571816631005)


![Screenshot (1243)](https://github.com/user-attachments/assets/3c296353-c3ad-4a84-8a3a-ba408ae14ac3)

![Screenshot (1245)](https://github.com/user-attachments/assets/bedea32d-5b01-4b67-9785-e23174c69b02)

![Screenshot (1246)](https://github.com/user-attachments/assets/e8d1b26f-9f43-497f-978d-0bc2b7ee5c78)


## Getting Started

### Prerequisites

You will need the following to run this project:

- Python 3.x
- API credentials for Twitter, Facebook, and Instagram
  
install necessary dependencies:
tweepy for interacting with Twitter's API ,
facebook-sdk for Facebook's Graph API ,
instaloader for Instagram media upload .

Configuration
You need to set up API credentials for each platform:

1. Twitter Setup:
Create a Twitter Developer account at Twitter Developer Portal.
Generate your API keys (consumer_key, consumer_secret, access_token, access_token_secret).
Replace the placeholders in the code with your credentials.

get all the keys in portal like this:
![image](https://github.com/user-attachments/assets/f1801c8c-265e-45da-838c-b198b8dc24af)

reference video to get keys:
[Watch this video](https://www.youtube.com/watch?v=QdJx942mfFc)

3. Facebook Setup:
Go to the Facebook Developer Portal.
Create a new app and get a long-lived access token for Facebook Graph API.
Replace fb_access_token in the code with your Facebook API token.

![Screenshot (1241)](https://github.com/user-attachments/assets/8bcac5d1-b2f3-4872-92f0-f0bd234c895c)

tutorial to get access token : [Watch the Video on YouTube](https://www.youtube.com/watch?v=nPOgLZuuURs)


5. Instagram Setup:
Instagram requires you to have an Instagram Developer account and a Business account for posting.
For this project, you can use Instaloader (an unofficial API) for uploading images and videos.
Replace the Instagram credentials (insta_username, insta_password) in the code.


Once you've set up the credentials, you can use the script to post content.

Example:
To post to Twitter:
text = "This is a test post!"
image_path = "path_to_image.jpg"  # or video_path = "path_to_video.mp4"

# Post to Twitter with text and an image
post_to_twitter(text, image_path=image_path)

# Post to Facebook with text and an image
post_to_facebook(text, image_path=image_path)

# Post to Instagram with text and an image
post_to_instagram(text, image_path=image_path)

You can pass text, image_path, or video_path depending on your needs.

# Limit rates :

-> for Twitter API :

![Screenshot 2025-01-07 023717](https://github.com/user-attachments/assets/792d9d38-16d9-4bfc-abe8-c0f0c156a878)

-> for Facebook Graph API :

![Screenshot 2025-01-07 023837](https://github.com/user-attachments/assets/8ddab6a3-a62a-4c9c-8b42-073823e968ec)




