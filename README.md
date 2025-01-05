# Social Media Automation

This project automates posting to Twitter, Facebook, and Instagram using their respective APIs. The main goal of this project is to provide an easy-to-use script to post text, images, and videos to these social media platforms.

### Features:
- **Twitter**: Post text, images, and videos to Twitter using the Tweepy API.
- **Facebook**: Post text, images, and videos to Facebook using the Graph API.
- **Instagram**: Post images and videos to Instagram using Instaloader (non-official API).

---

## Getting Started

### Prerequisites

You will need the following to run this project:

- Python 3.x
- API credentials for Twitter, Facebook, and Instagram
  
install necessary dependencies:
tweepy for interacting with Twitter's API
facebook-sdk for Facebook's Graph API
instaloader for Instagram media upload


Configuration
You need to set up API credentials for each platform:

1. Twitter Setup:
Create a Twitter Developer account at Twitter Developer Portal.
Generate your API keys (consumer_key, consumer_secret, access_token, access_token_secret).
Replace the placeholders in the code with your credentials.
2. Facebook Setup:
Go to the Facebook Developer Portal.
Create a new app and get a long-lived access token for Facebook Graph API.
Replace fb_access_token in the code with your Facebook API token.
3. Instagram Setup:
Instagram requires you to have an Instagram Developer account and a Business account for posting.
For this project, you can use Instaloader (an unofficial API) for uploading images and videos.
Replace the Instagram credentials (insta_username, insta_password) in the code.
Usage
Once you've set up the credentials, you can use the script to post content.

Example:
To post to Twitter:

python
Copy code
text = "This is a test post!"
image_path = "path_to_image.jpg"  # or video_path = "path_to_video.mp4"

# Post to Twitter with text and an image
post_to_twitter(text, image_path=image_path)
To post to Facebook:

python
Copy code
# Post to Facebook with text and an image
post_to_facebook(text, image_path=image_path)
To post to Instagram:

python
Copy code
# Post to Instagram with text and an image
post_to_instagram(text, image_path=image_path)
You can pass text, image_path, or video_path depending on your needs.


