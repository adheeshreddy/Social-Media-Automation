import tweepy # type: ignore
import facebook # type: ignore
import instaloader # type: ignore


# Replace with your actual credentials
# Twitter credentials
# consumer_key = '<CONSUMER_KEY>'
# consumer_secret = '<CONSUMER_SECRET>'
# access_token = '<ACCESS_TOKEN>'
# access_token_secret = '<ACCESS_TOKEN_SECRET>'
# bearer_token = '<BEARER_TOKEN>'
consumer_key = '1vdru0PAYpHJgPz9tg6QHP6vm'
consumer_secret = 's5j4CKKd39vgnkicYwuxcdU7144gbX88KFrAzjGawAH0ULdSPv'
access_token = '1875815433355587584-y8jWVAore1Pf8UTFg314zHF0UviuIR'
access_token_secret = 'pYVgw9b69Wnl8w9jBE3869jU5NFdWQXTYoARhS3NosHK9'
bearer_token = 'AAAAAAAAAAAAAAAAAAAAAN6%2FxwEAAAAAJmtocC7FdjKjZwkyk5Tpmd%2B2t2E%3DFaeaLwErfgLY5CZoXLLpsbDn9QGzx5bVZrvvS70w9PHeRONEQw'

# Instagram credentials
# insta_username = "YOUR_INSTAGRAM_USERNAME"
# insta_password = "YOUR_INSTAGRAM_PASSWORD"

# Instagram Login using Instaloader
# L = instaloader.Instaloader()
# L.login(insta_username, insta_password)

# V1 Twitter API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, wait_on_rate_limit=True)

# V2 Twitter API Authentication
client = tweepy.Client(
    bearer_token,
    consumer_key,
    consumer_secret,
    access_token,
    access_token_secret,
    wait_on_rate_limit=True,
)

# Function to upload media (image/video) to Twitter
def upload_media(filename):
    try:
        media = api.media_upload(filename)
        return media.media_id_string
    except Exception as e:
        print(f"Error uploading media to Twitter: {e}")
        return None

# Function to post to Twitter
def post_to_twitter(text, image_path=None, video_path=None):
    try:
        if image_path:
            image_media_id = upload_media(image_path)
            if image_media_id:
                client.create_tweet(text=text, media_ids=[image_media_id])
                print("Tweeted with Image!")
        elif video_path:
            video_media_id = upload_media(video_path)
            if video_media_id:
                client.create_tweet(text=text, media_ids=[video_media_id])
                print("Tweeted with Video!")
        else:
            client.create_tweet(text=text)
            print("Tweeted with Text!")
    except Exception as e:
        print(f"Error posting to Twitter: {e}")



   

# Function to post to Instagram
def post_to_instagram(text, image_path=None, video_path=None):
    try:
        if image_path:
            post = instaloader.Post.from_media_id(L.context, media_id=image_path)
            L.upload_post(post, caption=text)
        elif video_path:
            post = instaloader.Post.from_media_id(L.context, media_id=video_path)
            L.upload_post(post, caption=text)
        else:
            print("Instagram requires image or video for posting.")

        print("Posted to Instagram successfully!")
    except Exception as e:
        print(f"Error posting to Instagram: {e}")

# Example usage
text = "hi iam taking about signitives "

# Replace with your image or video paths
image_path = "download.jpg"
video_path = "hello.mp4"

# Posting to Twitter, Facebook, and Instagram
post_to_twitter(text)  # or video_path=video_path
# post_to_instagram(text, image_path=image_path)  # or video_path=video_path
