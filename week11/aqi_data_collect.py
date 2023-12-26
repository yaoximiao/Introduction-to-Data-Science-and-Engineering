import requests
import json


def get_followings_repos(token):
    headers = {
        'Authorization': f'token {token}',
        'Accept': 'application/vnd.github.v3+json'
    }

    # 获取当前登录用户的用户名
    user_response = requests.get('https://api.github.com/user', headers=headers)
    if user_response.status_code == 200:
        user_data = user_response.json()
        username = user_data['login']

        # 获取当前登录用户关注的人列表
        followings_response = requests.get(f'https://api.github.com/users/{username}/following', headers=headers)
        if followings_response.status_code == 200:
            followings_data = followings_response.json()

            # 遍历关注的人，获取其仓库信息并保存到本地文件
            with open('followings_repos.json', 'w') as file:
                for following in followings_data:
                    following_username = following['login']
                    repos_response = requests.get(f'https://api.github.com/users/{following_username}/repos',
                                                  headers=headers)
                    if repos_response.status_code == 200:
                        repos_data = repos_response.json()
                        json.dump({following_username: repos_data}, file, indent=2)
                    else:
                        print(f"Failed to fetch repositories for {following_username}")
        else:
            print("Failed to fetch followings data")
    else:
        print("Failed to fetch user data")


if __name__ == "__main__":
    your_token = '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'

    get_followings_repos(your_token)
