import os

os.environ[
    "OPENAI_API_KEY"] = "your-key"

def main():
    from openai import OpenAI

    client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
    response = client.images.generate(
        model="dall-e-3",
        prompt="'꽃말의 비밀 정원' 전자상거래 앱의 새해 장미꽃 홍보 포스터, 문구도 포함해서",
        size="1024x1024",
        quality="standard",
        n=1
    )

    img_url = response.data[0].url

    import requests
    image = requests.get(img_url)
    from IPython.display import Image, display

    display(Image(data=image.content))

if __name__ == "__main__":
    main()