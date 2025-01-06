import requests

# Your Access Token and Page ID
access_token = 'EAAPyrCXa78EBOZCQn8hSWsoEXkTeVfo2GystnWKZAeSCPdHXGC0ZBAEmjQsTUMtxezOyrT1alxpnmpSnIy5bFIlZBW7IzJj2kEEOKZCg8tTqwEedS6Rl6aXa6hklIjzruFJ2TC0Fam1R9q2orvigWhKuXKxjm12AQ9vC9hSyj3ZCdp1spJodZCGmZBzzOYDrUuxsxk7CQJGzaA9NYpd2Qiu3CPum'
page_id = '559607547229238'

# Post Text
def post_text(message):
    url = f'https://graph.facebook.com/{page_id}/feed'
    params = {'message': message, 'access_token': access_token}
    response = requests.post(url, params=params)
    if response.status_code == 200:
        print("Text posted successfully!")
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Post Image
def post_image(image_path, message):
    url = f'https://graph.facebook.com/{page_id}/photos'
    files = {'file': open(image_path, 'rb')}
    params = {'access_token': access_token, 'message': message}
    response = requests.post(url, files=files, data=params)
    if response.status_code == 200:
        print("Image uploaded successfully!")
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Post Video
def post_video(video_path, description):
    url = f'https://graph.facebook.com/{page_id}/videos'
    files = {'file': open(video_path, 'rb')}
    params = {'access_token': access_token, 'description': description}
    response = requests.post(url, files=files, data=params)
    if response.status_code == 200:
        print("Video uploaded successfully!")
    else:
        print(f"Error: {response.status_code}, {response.text}")

# Call all functions to post
post_text('Hello, this is 2nd test post!')
# post_image('signitives.jpg', 'This is an image post')
# post_video('hello.mp4', 'This is a test video post')

# this is the page link : https://www.facebook.com/profile.php?id=61571816631005
